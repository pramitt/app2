import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample marketing data
data = {
    'Campaign': ['Campaign A', 'Campaign B', 'Campaign C', 'Campaign D'],
    'Impressions': [1500, 2500, 1800, 3000],
    'Clicks': [100, 150, 130, 180],
    'Conversions': [10, 20, 15, 25]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Title of the app
st.title("Marketing Dashboard")

# Display the raw data
st.subheader("Marketing Campaign Data")
st.dataframe(df)

# Filter the data based on Campaign
campaign = st.selectbox("Select Campaign", df['Campaign'].unique())
filtered_data = df[df['Campaign'] == campaign]

st.subheader(f"Data for {campaign}")
st.dataframe(filtered_data)

# Visualizations
st.subheader("Visualizations")

# Impressions vs Clicks
fig, ax = plt.subplots()
ax.bar(df['Campaign'], df['Impressions'], label='Impressions')
ax.bar(df['Campaign'], df['Clicks'], bottom=df['Impressions'], label='Clicks')
ax.set_ylabel('Count')
ax.set_title('Impressions and Clicks by Campaign')
ax.legend()
st.pyplot(fig)

# Conversions
fig, ax = plt.subplots()
ax.pie(df['Conversions'], labels=df['Campaign'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# Additional Metrics
st.subheader("Metrics")
total_impressions = df['Impressions'].sum()
total_clicks = df['Clicks'].sum()
total_conversions = df['Conversions'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Impressions", total_impressions)
col2.metric("Total Clicks", total_clicks)
col3.metric("Total Conversions", total_conversions)

# Run the app
if __name__ == '__main__':
    st.run()
