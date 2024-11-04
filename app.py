import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Ecological Research Data Browser",
    page_icon="🌿",
    layout="wide"
)

# Function to load all datasets
def load_datasets():
    datasets = {
        "Beetles Density Study (density vs survival)": pd.read_csv("data/beetles.csv", index_col=False),
        "Ant Biomass Analysis (temporal data)": pd.read_csv("data/ants.csv", index_col=False),
        "Rodent Species Analysis (habitat factors)": pd.read_csv("data/bolger.csv", index_col=False),
        "Crab Weight Study (morphometric data)": pd.read_csv("data/crabs.csv", index_col=False),
        "Forest & Bog Analysis (site comparison)": pd.read_csv("data/gotelli.csv", index_col=False),
        "Green Site Analysis (site data)": pd.read_csv("data/green.csv", index_col=False),
        "Biofilm Study (experimental data)": pd.read_csv("data/keough.csv", index_col=False),
        "Humidity Analysis (environmental data)": pd.read_csv("data/nelson.csv", index_col=False),
        "Climate & Vegetation Study (geographical data)": pd.read_csv("data/paruelo.csv", index_col=False),
        "Species Area Relationship (ecological data)": pd.read_csv("data/peake.csv", index_col=False),
        "Mouse pH Study (physiological data)": pd.read_csv("data/ph.csv", index_col=False),
        "Island Ratio Analysis (spatial data)": pd.read_csv("data/polis.csv", index_col=False),
        "Treatment Length Study (experimental data)": pd.read_csv("data/purves.csv", index_col=False),
        "Beetle & Plant Analysis (community data)": pd.read_csv("data/sanchez.csv", index_col=False),
        "Wildlife Mortality Study (survival data)": pd.read_csv("data/sinclair.csv", index_col=False),
        "Population Treatment Study (temporal comparison)": pd.read_csv("data/taulman.csv", index_col=False)
    }
    return datasets

# Dataset descriptions
dataset_descriptions = {
    "Beetles Density Study (density vs survival)": "Study examining the relationship between beetle population density and survival rates in controlled environments.",
    "Ant Biomass Analysis (temporal data)": "Monthly measurements of ant biomass across different time periods, showing seasonal variations in ant populations.",
    "Rodent Species Analysis (habitat factors)": "Analysis of rodent species presence in relation to habitat characteristics including shrub coverage and distance metrics.",
    "Crab Weight Study (morphometric data)": "Morphometric study comparing body weight and gill weight relationships in crabs.",
    "Forest & Bog Analysis (site comparison)": "Comparative study of species richness between forest and bog habitats across different latitudes and elevations.",
    "Green Site Analysis (site data)": "Site-specific study measuring total mass and burrow counts across different locations.",
    "Biofilm Study (experimental data)": "Experimental study examining biofilm development under different treatment conditions.",
    "Humidity Analysis (environmental data)": "Investigation of the relationship between humidity levels and weight loss in biological samples.",
    "Climate & Vegetation Study (geographical data)": "Large-scale study of climate variables and vegetation patterns across different geographical locations.",
    "Species Area Relationship (ecological data)": "Study examining the relationship between area size and species diversity/individual counts.",
    "Mouse pH Study (physiological data)": "Physiological study measuring pH levels in mice across different experimental conditions.",
    "Island Ratio Analysis (spatial data)": "Analysis of ecological ratios across different islands and their relationship with species presence.",
    "Treatment Length Study (experimental data)": "Experimental study comparing different treatment effects on specimen length.",
    "Beetle & Plant Analysis (community data)": "Community ecology study examining relationships between beetles, guano, and plant coverage.",
    "Wildlife Mortality Study (survival data)": "Analysis of wildlife mortality patterns across different demographic groups and conditions.",
    "Population Treatment Study (temporal comparison)": "Temporal study comparing population responses to different treatments over multiple years."
}

# Create tabs
tab1, tab2 = st.tabs(["Data Analysis", "Contact"])

with tab1:
    # Main content
    st.title("Ecological Research Data Browser")
    
    # Sidebar for dataset selection
    st.sidebar.title("Dataset Selection")
    datasets = load_datasets()
    
    # Create radio buttons for dataset selection
    dataset_name = st.sidebar.radio(
        "Select a dataset to analyze:",
        list(datasets.keys()),
        format_func=lambda x: f"• {x}"
    )

    # Display selected dataset
    if dataset_name:
        st.header(dataset_name)
        
        # Display dataset description
        st.info(dataset_descriptions[dataset_name])
        
        df = datasets[dataset_name]
        st.write("Variables in the dataset:", ", ".join(df.columns))
        
        # Display the dataframe with full width and no index
        st.dataframe(
            df.reset_index(drop=True),
            use_container_width=True,
            hide_index=True
        )

with tab2:
    st.title("Contact Information")
    st.write("### Dhafer Malouche")
    st.write("This application was developed by  Dhafer Malouche.")
    
    # Contact information
    st.write("#### Get in Touch")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        📧 **Email**: dhafer.malouche@qu.edu.qa  
        🌐 **Website**: https://dhafermalouche.net  
        💼 **LinkedIn**: https://linkedin.com/in/dhafer-malouche-b54629b/
        """)
    
    st.write("### About This App")
    st.write("""
                    This application is designed to facilitate accessing datasets for statistical analysis in biology. 
                    Most of the data are from the book:*Biostatistical Design and Analysis Using R: A Practical Guide* by Murray Logan (2010), Wiley-Blackwell. ISBN: 978-1-405-19008-4

                    This interactive interface allows users to explore various ecological and biological datasets used in the book's examples and exercises.

                    For any questions or suggestions about this app's functionality, please don't hesitate to reach out through any of the channels above.
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
    /* Make the dataframe use full width */
    .stDataFrame {
        width: 100%;
    }
    /* Style the radio buttons */
    .stRadio > label {
        font-size: 14px;
        margin-left: 10px;
    }
</style>
""", unsafe_allow_html=True)