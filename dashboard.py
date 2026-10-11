#!/usr/bin/env python3
"""
Toronto Tech Events Dashboard
Interactive Streamlit dashboard for analyzing tech events in Toronto.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Toronto Tech Events Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .header {
        color: #1f77b4;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data(csv_path):
    """Load and prepare event data."""
    df = pd.read_csv(csv_path)

    # Prepare time data
    df['start_time_obj'] = pd.to_datetime(df['start_time'], format='%H:%M').dt.time
    df['end_time_obj'] = pd.to_datetime(df['end_time'], format='%H:%M').dt.time
    df['start_hour'] = pd.to_datetime(df['start_time'], format='%H:%M').dt.hour
    df['end_hour'] = pd.to_datetime(df['end_time'], format='%H:%M').dt.hour

    # Order days of week
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['day_of_week'] = pd.Categorical(
        df['day_of_week'],
        categories=day_order,
        ordered=True
    )

    return df

def hour_to_12h_format(hour):
    """Convert 24-hour format to 12-hour AM/PM format."""
    if hour == 0:
        return "12:00 AM"
    elif hour < 12:
        return f"{hour}:00 AM"
    elif hour == 12:
        return "12:00 PM"
    else:
        return f"{hour - 12}:00 PM"

def create_day_chart(df):
    """Create day distribution chart."""
    day_counts = df['day_of_week'].value_counts().sort_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['#2E86AB' if count >= day_counts.quantile(0.75) else '#A23B72'
              for count in day_counts.values]

    bars = ax.bar(range(len(day_counts)), day_counts.values, color=colors, edgecolor='black', linewidth=1.2)

    ax.set_xlabel('Day of Week', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Events', fontsize=12, fontweight='bold')
    ax.set_title('Tech Events Distribution by Day of Week', fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(range(len(day_counts)))
    ax.set_xticklabels(day_counts.index, rotation=45, ha='right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontweight='bold', fontsize=11)

    plt.tight_layout()
    return fig

def create_time_chart(df):
    """Create time distribution chart."""
    start_hours = df['start_hour'].value_counts().sort_index()
    end_hours = df['end_hour'].value_counts().sort_index()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Start times
    ax1.bar(start_hours.index, start_hours.values, color='#F18F01', edgecolor='black', linewidth=1.2)
    ax1.set_xlabel('Hour of Day', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Number of Events', fontsize=11, fontweight='bold')
    ax1.set_title('Event Start Times', fontsize=12, fontweight='bold', pad=15)
    ax1.set_xticks(range(int(start_hours.index.min()), int(start_hours.index.max()) + 1))
    ax1.set_xticklabels([hour_to_12h_format(h) for h in range(int(start_hours.index.min()), int(start_hours.index.max()) + 1)],
                         rotation=45, ha='right')
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    ax1.set_axisbelow(True)

    for i, v in enumerate(start_hours.values):
        ax1.text(start_hours.index[i], v, f'{int(v)}', ha='center', va='bottom', fontweight='bold', fontsize=10)

    # End times
    ax2.bar(end_hours.index, end_hours.values, color='#C1121F', edgecolor='black', linewidth=1.2)
    ax2.set_xlabel('Hour of Day', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Number of Events', fontsize=11, fontweight='bold')
    ax2.set_title('Event End Times', fontsize=12, fontweight='bold', pad=15)
    ax2.set_xticks(range(int(end_hours.index.min()), int(end_hours.index.max()) + 1))
    ax2.set_xticklabels([hour_to_12h_format(h) for h in range(int(end_hours.index.min()), int(end_hours.index.max()) + 1)],
                         rotation=45, ha='right')
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    ax2.set_axisbelow(True)

    for i, v in enumerate(end_hours.values):
        ax2.text(end_hours.index[i], v, f'{int(v)}', ha='center', va='bottom', fontweight='bold', fontsize=10)

    plt.tight_layout()
    return fig

def create_category_chart(df):
    """Create category distribution chart."""
    category_counts = df['category'].value_counts()

    fig, ax = plt.subplots(figsize=(10, 6))
    colors_cat = ['#2E86AB', '#A23B72', '#F18F01', '#C1121F']
    bars = ax.barh(category_counts.index, category_counts.values, color=colors_cat[:len(category_counts)], edgecolor='black', linewidth=1.2)

    ax.set_xlabel('Number of Events', fontsize=12, fontweight='bold')
    ax.set_title('Events by Category', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_axisbelow(True)

    for bar in bars:
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
                f'{int(width)}',
                ha='left', va='center', fontweight='bold', fontsize=11, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()
    return fig

def main():
    """Main dashboard application."""

    # Load data
    csv_path = Path(__file__).parent / 'data' / 'toronto_tech_events_synthetic.csv'

    if not csv_path.exists():
        st.error(f"Dataset not found at {csv_path}")
        return

    df = load_data(csv_path)

    # Header
    st.markdown("# 📊 Toronto Tech Events Dashboard")
    st.markdown("**Interactive analysis of AI and tech events in Toronto**")
    st.divider()

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Events", len(df), delta=None)

    with col2:
        peak_day = df['day_of_week'].value_counts().idxmax()
        peak_count = df['day_of_week'].value_counts().max()
        st.metric("Peak Day", peak_day, delta=f"{peak_count} events")

    with col3:
        start_hour = df['start_hour'].value_counts().idxmax()
        st.metric("Most Common Start", hour_to_12h_format(start_hour), delta=None)

    with col4:
        end_hour = df['end_hour'].value_counts().idxmax()
        st.metric("Most Common End", hour_to_12h_format(end_hour), delta=None)

    st.divider()

    # Filters
    st.sidebar.header("🔍 Filters")

    selected_days = st.sidebar.multiselect(
        "Select Days of Week",
        options=df['day_of_week'].unique(),
        default=df['day_of_week'].unique()
    )

    selected_categories = st.sidebar.multiselect(
        "Select Event Categories",
        options=df['category'].unique(),
        default=df['category'].unique()
    )

    # Apply filters
    filtered_df = df[
        (df['day_of_week'].isin(selected_days)) &
        (df['category'].isin(selected_categories))
    ]

    st.sidebar.metric("Filtered Events", len(filtered_df))

    # Visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["📅 Day Distribution", "⏰ Time Windows", "📂 Categories", "📋 Data Table"])

    with tab1:
        st.subheader("Events by Day of Week")
        fig_day = create_day_chart(filtered_df)
        st.pyplot(fig_day)

        # Statistics
        col1, col2 = st.columns(2)
        with col1:
            day_counts = filtered_df['day_of_week'].value_counts().sort_index()
            st.write("**Day Distribution:**")
            st.dataframe(day_counts, use_container_width=True)

    with tab2:
        st.subheader("Event Time Windows")
        fig_time = create_time_chart(filtered_df)
        st.pyplot(fig_time)

        # Statistics
        col1, col2 = st.columns(2)
        with col1:
            start_dist = filtered_df['start_hour'].value_counts().sort_index()
            st.write("**Start Time Distribution:**")
            st.dataframe(start_dist, use_container_width=True)

        with col2:
            end_dist = filtered_df['end_hour'].value_counts().sort_index()
            st.write("**End Time Distribution:**")
            st.dataframe(end_dist, use_container_width=True)

    with tab3:
        st.subheader("Events by Category")
        fig_cat = create_category_chart(filtered_df)
        st.pyplot(fig_cat)

        col1, col2 = st.columns(2)
        with col1:
            cat_counts = filtered_df['category'].value_counts()
            st.write("**Category Distribution:**")
            st.dataframe(cat_counts, use_container_width=True)

    with tab4:
        st.subheader("Event Data")

        # Display options
        col1, col2 = st.columns(2)
        with col1:
            sort_by = st.selectbox("Sort by", options=['date', 'day_of_week', 'start_hour', 'category'])
        with col2:
            show_columns = st.multiselect(
                "Columns to display",
                options=filtered_df.columns,
                default=['event_name', 'category', 'date', 'day_of_week', 'start_time', 'end_time', 'venue']
            )

        # Display data
        display_df = filtered_df[show_columns].sort_values(sort_by)
        st.dataframe(display_df, use_container_width=True)

        # Download button
        csv = display_df.to_csv(index=False)
        st.download_button(
            label="📥 Download filtered data as CSV",
            data=csv,
            file_name="toronto_tech_events.csv",
            mime="text/csv"
        )

    # Key Insights
    st.divider()
    st.subheader("💡 Key Insights")

    day_counts = filtered_df['day_of_week'].value_counts().sort_values(ascending=False)
    start_hour = filtered_df['start_hour'].value_counts().idxmax()
    end_hour = filtered_df['end_hour'].value_counts().idxmax()

    insight_text = f"""
    Based on the filtered data of **{len(filtered_df)} events**:

    - **Peak Days:** {day_counts.head(2).index.tolist()} are the busiest days
    - **Typical Timing:** Most events run from {hour_to_12h_format(start_hour)} to {hour_to_12h_format(end_hour)}
    - **Best Attendance Strategy:** Plan to attend events on {day_counts.index[0]}s and {day_counts.index[1]}s between {hour_to_12h_format(start_hour)} and {hour_to_12h_format(end_hour)}
    """

    st.info(insight_text)

if __name__ == '__main__':
    main()