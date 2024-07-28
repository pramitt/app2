import streamlit as st
import pandas as pd

st.title("Marketing Data Analysis App")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset")
    st.write("First 5 rows of the dataset:")
    st.write(df.head())

    # Display basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Select columns for visualization
    st.subheader("Visualizations")
    st.write("Select columns for visualization")

    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

    if numerical_columns:
        st.write("Numerical Columns")
        num_column = st.selectbox("Select Numerical Column", numerical_columns)

        # Histogram
        st.write(f"Histogram of {num_column}")
        st.bar_chart(df[num_column].value_counts())

        # Boxplot
        st.write(f"Boxplot of {num_column}")
        st.write(df[[num_column]].boxplot())

    if categorical_columns:
        st.write("Categorical Columns")
        cat_column = st.selectbox("Select Categorical Column", categorical_columns)

        # Bar chart
        st.write(f"Bar Chart of {cat_column}")
        st.bar_chart(df[cat_column].value_counts())

    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    if len(numerical_columns) > 1:
        corr = df[numerical_columns].corr()
        st.write(corr.style.background_gradient(cmap='coolwarm'))

    # Pairplot
    st.subheader("Pairplot")
    if len(numerical_columns) > 1:
        st.write("Pairplot of numerical columns")
        st.write(pd.plotting.scatter_matrix(df[numerical_columns], figsize=(10, 10)))

