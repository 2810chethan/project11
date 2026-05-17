import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# PAGE CONFIG
st.set_page_config(
    page_title="Graphs Dashboard",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #141E30, #243B55);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 2px solid #374151;
}

/* Titles */
h1 {
    color: #00E5FF;
    text-align: center;
    font-size: 45px;
    font-weight: bold;
}

h2, h3, h4 {
    color: white;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background-color: #1F2937;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #4B5563;
}

/* Buttons */
.stButton>button {
    background-color: #00E5FF;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background-color: #00B8D4;
    color: white;
}

/* Select Boxes */
div[data-baseweb="select"] {
    background-color: #1F2937;
    border-radius: 10px;
    color: white;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("📊 Streamlit Graph Dashboard")

# FILE UPLOADER
uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

# IF FILE UPLOADED
if uploaded_file is not None:

    # READ FILE
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # SHOW DATA
    st.subheader("📁 Dataset Preview")
    st.dataframe(df)

    # SELECT NUMERIC COLUMNS
    numeric_cols = df.select_dtypes(
        include=['int64', 'float64']
    ).columns

    # CHECK NUMERIC COLUMNS
    if len(numeric_cols) == 0:
        st.warning("No numeric columns found")

    else:

        # SIDEBAR
        st.sidebar.title("⚙️ Graph Settings")

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

        x_col = st.sidebar.selectbox(
            "Select X-axis",
            df.columns
        )

        y_col = st.sidebar.selectbox(
            "Select Y-axis",
            numeric_cols
        )

        # COMMON PLOTLY STYLE
        plot_bg = dict(
            paper_bgcolor="#141E30",
            plot_bgcolor="#141E30",
            font=dict(color="white")
        )

        # LINE CHART
        if graph_type == "Line Chart":

            st.subheader("📈 Line Chart")

            fig = px.line(df, x=x_col, y=y_col)

            fig.update_layout(**plot_bg)

            st.plotly_chart(fig, use_container_width=True)

        # BAR CHART
        elif graph_type == "Bar Chart":

            st.subheader("📊 Bar Chart")

            fig = px.bar(df, x=x_col, y=y_col)

            fig.update_layout(**plot_bg)

            st.plotly_chart(fig, use_container_width=True)

        # SCATTER PLOT
        elif graph_type == "Scatter Plot":

            st.subheader("⚪ Scatter Plot")

            fig = px.scatter(df, x=x_col, y=y_col)

            fig.update_layout(**plot_bg)

            st.plotly_chart(fig, use_container_width=True)

        # HISTOGRAM
        elif graph_type == "Histogram":

            st.subheader("📉 Histogram")

            fig = px.histogram(df, x=y_col)

            fig.update_layout(**plot_bg)

            st.plotly_chart(fig, use_container_width=True)

        # BOX PLOT
        elif graph_type == "Box Plot":

            st.subheader("📦 Box Plot")

            fig = px.box(df, y=y_col)

            fig.update_layout(**plot_bg)

            st.plotly_chart(fig, use_container_width=True)

        # PIE CHART
        elif graph_type == "Pie Chart":

            st.subheader("🥧 Pie Chart")

            fig = px.pie(df, names=x_col, values=y_col)

            fig.update_layout(**plot_bg)

            st.plotly_chart(fig, use_container_width=True)

        # AREA CHART
        elif graph_type == "Area Chart":

            st.subheader("🌊 Area Chart")

            fig = px.area(df, x=x_col, y=y_col)

            fig.update_layout(**plot_bg)

            st.plotly_chart(fig, use_container_width=True)

        # HEATMAP
        elif graph_type == "Heatmap":

            st.subheader("🔥 Heatmap")

            corr = df[numeric_cols].corr()

            fig, ax = plt.subplots(figsize=(10, 6))

            fig.patch.set_facecolor("#141E30")
            ax.set_facecolor("#141E30")

            sns.heatmap(
                corr,
                annot=True,
                cmap="coolwarm",
                ax=ax
            )

            st.pyplot(fig)

else:
    st.info("Please upload a CSV or Excel file")