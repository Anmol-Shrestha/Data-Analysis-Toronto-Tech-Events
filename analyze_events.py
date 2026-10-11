#!/usr/bin/env python3
"""
Toronto Tech Events Analysis
Analyzes AI/tech events to identify optimal days and time windows for attending.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from datetime import datetime
import numpy as np


class EventAnalyzer:
    """Analyzes tech events dataset for patterns in scheduling."""

    def __init__(self, csv_path):
        """Initialize analyzer with event data."""
        self.df = pd.read_csv(csv_path)
        self._prepare_data()

    def _prepare_data(self):
        """Clean and prepare data for analysis."""
        # Convert time columns to datetime objects for easier manipulation
        self.df['start_time_obj'] = pd.to_datetime(self.df['start_time'], format='%H:%M').dt.time
        self.df['end_time_obj'] = pd.to_datetime(self.df['end_time'], format='%H:%M').dt.time

        # Extract hour from start and end times
        self.df['start_hour'] = pd.to_datetime(self.df['start_time'], format='%H:%M').dt.hour
        self.df['end_hour'] = pd.to_datetime(self.df['end_time'], format='%H:%M').dt.hour

        # Define day order for proper sorting
        self.day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.df['day_of_week'] = pd.Categorical(
            self.df['day_of_week'],
            categories=self.day_order,
            ordered=True
        )

    def analyze_day_distribution(self):
        """Analyze event distribution by day of week."""
        day_counts = self.df['day_of_week'].value_counts().sort_index()
        return day_counts

    def analyze_time_windows(self):
        """Analyze most common start and end times."""
        start_time_dist = self.df['start_hour'].value_counts().sort_index()
        end_time_dist = self.df['end_hour'].value_counts().sort_index()
        return start_time_dist, end_time_dist

    def get_event_summary_stats(self):
        """Calculate summary statistics for the narrative."""
        day_counts = self.analyze_day_distribution()
        most_common_day = day_counts.idxmax()
        most_common_day_count = day_counts.max()

        start_hours, end_hours = self.analyze_time_windows()
        most_common_start = start_hours.idxmax()
        most_common_end = end_hours.idxmax()

        return {
            'most_common_day': most_common_day,
            'most_common_day_count': most_common_day_count,
            'most_common_start_hour': most_common_start,
            'most_common_end_hour': most_common_end,
            'total_events': len(self.df),
        }

    def _hour_to_12h_format(self, hour):
        """Convert 24-hour format to 12-hour AM/PM format."""
        if hour == 0:
            return "12:00 AM"
        elif hour < 12:
            return f"{hour}:00 AM"
        elif hour == 12:
            return "12:00 PM"
        else:
            return f"{hour - 12}:00 PM"

    def plot_day_distribution(self, output_path='day_distribution.png'):
        """Create visualization for day-of-week distribution."""
        day_counts = self.analyze_day_distribution()

        fig, ax = plt.subplots(figsize=(12, 6))

        # Create bar chart with color highlighting top days
        colors = ['#2E86AB' if count >= day_counts.quantile(0.75) else '#A23B72'
                  for count in day_counts.values]

        bars = ax.bar(range(len(day_counts)), day_counts.values, color=colors, edgecolor='black', linewidth=1.2)

        # Customize plot
        ax.set_xlabel('Day of Week', fontsize=12, fontweight='bold')
        ax.set_ylabel('Number of Events', fontsize=12, fontweight='bold')
        ax.set_title('Tech Events Distribution by Day of Week', fontsize=14, fontweight='bold', pad=20)
        ax.set_xticks(range(len(day_counts)))
        ax.set_xticklabels(day_counts.index, rotation=45, ha='right')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)

        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontweight='bold', fontsize=11)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_path}")
        return fig

    def plot_time_distribution(self, output_path='time_distribution.png'):
        """Create visualization for event time windows."""
        start_hours, end_hours = self.analyze_time_windows()

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # Start times
        ax1.bar(start_hours.index, start_hours.values, color='#F18F01', edgecolor='black', linewidth=1.2)
        ax1.set_xlabel('Hour of Day', fontsize=11, fontweight='bold')
        ax1.set_ylabel('Number of Events', fontsize=11, fontweight='bold')
        ax1.set_title('Event Start Times', fontsize=12, fontweight='bold', pad=15)
        ax1.set_xticks(range(int(start_hours.index.min()), int(start_hours.index.max()) + 1))
        ax1.set_xticklabels([self._hour_to_12h_format(h) for h in range(int(start_hours.index.min()), int(start_hours.index.max()) + 1)],
                             rotation=45, ha='right')
        ax1.grid(axis='y', alpha=0.3, linestyle='--')
        ax1.set_axisbelow(True)

        # Add value labels
        for i, v in enumerate(start_hours.values):
            ax1.text(start_hours.index[i], v, f'{int(v)}', ha='center', va='bottom', fontweight='bold', fontsize=10)

        # End times
        ax2.bar(end_hours.index, end_hours.values, color='#C1121F', edgecolor='black', linewidth=1.2)
        ax2.set_xlabel('Hour of Day', fontsize=11, fontweight='bold')
        ax2.set_ylabel('Number of Events', fontsize=11, fontweight='bold')
        ax2.set_title('Event End Times', fontsize=12, fontweight='bold', pad=15)
        ax2.set_xticks(range(int(end_hours.index.min()), int(end_hours.index.max()) + 1))
        ax2.set_xticklabels([self._hour_to_12h_format(h) for h in range(int(end_hours.index.min()), int(end_hours.index.max()) + 1)],
                             rotation=45, ha='right')
        ax2.grid(axis='y', alpha=0.3, linestyle='--')
        ax2.set_axisbelow(True)

        # Add value labels
        for i, v in enumerate(end_hours.values):
            ax2.text(end_hours.index[i], v, f'{int(v)}', ha='center', va='bottom', fontweight='bold', fontsize=10)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✓ Saved: {output_path}")
        return fig

    def print_summary(self):
        """Print key findings to console."""
        stats = self.get_event_summary_stats()
        day_counts = self.analyze_day_distribution()
        start_hours, end_hours = self.analyze_time_windows()

        print("\n" + "="*60)
        print("TORONTO TECH EVENTS ANALYSIS - KEY FINDINGS")
        print("="*60)

        print(f"\nTotal Events Analyzed: {stats['total_events']}")

        print("\n📅 Day Distribution:")
        for day, count in day_counts.items():
            print(f"  {day:12} : {count:3} events")

        print(f"\n🏆 Most Common Days: {day_counts.nlargest(2).index.tolist()}")

        print("\n⏰ Time Windows:")
        print(f"  Most common start hour: {self._hour_to_12h_format(stats['most_common_start_hour'])}")
        print(f"  Most common end hour  : {self._hour_to_12h_format(stats['most_common_end_hour'])}")

        print("\n💡 NARRATIVE FOR YOUR MANAGER:")
        print(f"  After analyzing {stats['total_events']} tech events, the data shows that")
        print(f"  {day_counts.nlargest(2).index[0]} and {day_counts.nlargest(2).index[1]} are the")
        print(f"  peak days for tech events, with most events running from")
        print(f"  {self._hour_to_12h_format(stats['most_common_start_hour'])} to {self._hour_to_12h_format(stats['most_common_end_hour'])}.")

        print("\n" + "="*60 + "\n")


def main():
    """Run the analysis."""
    # Find the CSV file
    csv_path = Path(__file__).parent / 'data' / 'toronto_tech_events_synthetic.csv'

    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset not found at {csv_path}")

    # Initialize analyzer
    analyzer = EventAnalyzer(csv_path)

    # Print summary statistics
    analyzer.print_summary()

    # Generate visualizations
    output_dir = Path(__file__).parent / 'visualizations'
    output_dir.mkdir(exist_ok=True)

    print("📊 Generating visualizations...")
    analyzer.plot_day_distribution(output_dir / 'day_distribution.png')
    analyzer.plot_time_distribution(output_dir / 'time_distribution.png')

    print("\n✨ Analysis complete! Charts saved to ./visualizations/")


if __name__ == '__main__':
    main()
