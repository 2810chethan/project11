import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Graphs Dashboard", layout="wide")

st.title("📊 Streamlit Graph Dashboard")

# Upload file
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found")
    else:

        st.sidebar.title("Graph Settings")

        graph_type = st.sidebar.selectbox(
            "Choose Graph",
            [
                "Line Chart",
                "Bar Chart",
                "Scatter Plot",
                "Histogram",
                "Box Plot",
                "Pie Chart",
                "Area Chart",
                "Heatmap"
            ]
        )

        x_col = st.sidebar.selectbox("Select X-axis", df.columns)
        y_col = st.sidebar.selectbox("Select Y-axis", numeric_cols)

        # LINE CHART
        if graph_type == "Line Chart":

            st.subheader("📈 Line Chart")

            fig = px.line(df, x=x_col, y=y_col)

            st.plotly_chart(fig, use_container_width=True)

        # BAR CHART
        elif graph_type == "Bar Chart":

            st.subheader("📊 Bar Chart")

            fig = px.bar(df, x=x_col, y=y_col)

            st.plotly_chart(fig, use_container_width=True)

        # SCATTER PLOT
        elif graph_type == "Scatter Plot":

            st.subheader("⚪ Scatter Plot")

            fig = px.scatter(df, x=x_col, y=y_col)

            st.plotly_chart(fig, use_container_width=True)

        # HISTOGRAM
        elif graph_type == "Histogram":

            st.subheader("📉 Histogram")

            fig = px.histogram(df, x=y_col)

            st.plotly_chart(fig, use_container_width=True)

        # BOX PLOT
        elif graph_type == "Box Plot":

            st.subheader("📦 Box Plot")

            fig = px.box(df, y=y_col)

            st.plotly_chart(fig, use_container_width=True)

        # PIE CHART
        elif graph_type == "Pie Chart":

            st.subheader("🥧 Pie Chart")

            fig = px.pie(df, names=x_col, values=y_col)

            st.plotly_chart(fig, use_container_width=True)

        # AREA CHART
        elif graph_type == "Area Chart":

            st.subheader("🌊 Area Chart")

            fig = px.area(df, x=x_col, y=y_col)

            st.plotly_chart(fig, use_container_width=True)

        # HEATMAP
        elif graph_type == "Heatmap":

            st.subheader("🔥 Heatmap")

            corr = df[numeric_cols].corr()

            fig, ax = plt.subplots(figsize=(10, 6))

            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

            st.pyplot(fig)

else:
    st.info("Please upload a CSV or Excel file")