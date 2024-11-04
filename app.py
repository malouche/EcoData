import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Ecological Data Analysis",
    page_icon="🌿",
    layout="wide"
)

# Function to load all datasets
def load_datasets():
    datasets = {
        "Beetles Density Study": pd.read_csv("beetles.csv"),
        "Ant Biomass Analysis": pd.read_csv("ants.csv"),
        "Rodent Species Analysis": pd.read_csv("bolger.csv"),
        "Crab Weight Study": pd.read_csv("crabs.csv"),
        "Forest & Bog Analysis": pd.read_csv("gotelli.csv"),
        "Green Site Analysis": pd.read_csv("green.csv"),
        "Biofilm Study": pd.read_csv("keough.csv"),
        "Humidity Analysis": pd.read_csv("nelson.csv"),
        "Climate & Vegetation Study": pd.read_csv("paruelo.csv"),
        "Species Area Relationship": pd.read_csv("peake.csv"),
        "Mouse pH Study": pd.read_csv("ph.csv"),
        "Island Ratio Analysis": pd.read_csv("polis.csv"),
        "Treatment Length Study": pd.read_csv("purves.csv"),
        "Beetle & Plant Analysis": pd.read_csv("sanchez.csv"),
        "Wildlife Mortality Study": pd.read_csv("sinclair.csv"),
        "Population Treatment Study": pd.read_csv("taulman.csv")
    }
    return datasets

# Create tabs
tab1, tab2 = st.tabs(["Data Analysis", "Contact"])

with tab1:
    # Sidebar for dataset selection
    st.sidebar.title("Dataset Selection")
    datasets = load_datasets()
    selected_dataset = st.sidebar.selectbox(
        "Choose a dataset",
        list(datasets.keys())
    )

    # Main content
    st.title("Ecological Data Analysis Platform")
    st.header(selected_dataset)

    # Display the selected dataset
    df = datasets[selected_dataset]
    st.dataframe(df)

    # Show basic statistics
    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Suggest analyses based on the dataset
    st.subheader("Possible Analyses")

    analyses = {
        "Beetles Density Study": [
            "Regression analysis between density and survival rate",
            "ANOVA to compare survival rates across density groups",
            "Descriptive statistics of survival rates"
        ],
        "Ant Biomass Analysis": [
            "Time series analysis of biomass across months",
            "Monthly biomass comparison using box plots",
            "Statistical tests for seasonal effects"
        ],
        "Rodent Species Analysis": [
            "Logistic regression for rodent species presence",
            "Correlation analysis between variables",
            "Multiple regression for habitat factors"
        ],
        # Add suggestions for other datasets...
    }

    if selected_dataset in analyses:
        for analysis in analyses[selected_dataset]:
            st.write("• " + analysis)
    
    # Generate automatic visualization based on data types
    st.subheader("Quick Visualization")
    if len(df.columns) >= 2:
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        if len(numeric_cols) >= 2:
            x_col = st.selectbox("Select X axis", numeric_cols)
            y_col = st.selectbox("Select Y axis", numeric_cols)
            fig = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}")
            st.plotly_chart(fig)

with tab2:
    st.title("Contact Information")
    st.write("### Dhafer Malouche")
    st.write("This application was developed by Dhafer Malouche, a data scientist and ecological data analyst.")
    
    # Contact information
    st.write("#### Get in Touch")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        📧 **Email**: dhafer.malouche@example.com  
        🌐 **Website**: www.dhafermalouche.com  
        """)
    with col2:
        st.markdown("""
        💼 **LinkedIn**: linkedin.com/in/dhafermalouche  
        🐦 **Twitter**: @dhafermalouche  
        """)
    
    st.write("### About This App")
    st.write("""
    This application is designed to facilitate the analysis of ecological datasets. 
    It provides an interactive interface for exploring various ecological studies 
    and performing different types of statistical analyses.
    
    For any questions, suggestions, or collaboration opportunities, 
    please don't hesitate to reach out through any of the channels above.
    """)

# Add custom CSS
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #f5f5f5;
    }
</style>
""", unsafe_allow_html=True)