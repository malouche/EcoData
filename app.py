import streamlit as st
import pandas as pd
from data_config import load_datasets, dataset_descriptions, get_metric_categories
from styles import load_css
from contact_info import show_contact_info

# Set page config
st.set_page_config(
    page_title="Research Data Browser",
    page_icon="🌿",
    layout="wide"
)

# Load custom CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Create tabs
tab1, tab2 = st.tabs(["Data Analysis", "Contact"])

with tab1:
    # Main content
    st.title("Research Data Browser")
    st.markdown("""
    This application provides access to two major categories of data:
    - 🌿 **Ecological Studies**: Data from various ecological and biological research projects
    - 💧 **Water & Agriculture (AQUASTAT)**: Global data covering:
        - Agricultural economics and land use
        - Water resources and infrastructure
        - Water usage efficiency and SDG indicators
        - Environmental health and access to water
    """)
    
    try:
        # Sidebar for dataset selection
        st.sidebar.title("Dataset Selection")
        datasets = load_datasets()
        
        category = st.sidebar.radio(
            "Select data category:",
            list(datasets.keys()),
            format_func=lambda x: f"📊 {x}"
        )
        
        dataset_name = st.sidebar.radio(
            f"Select a dataset from {category}:",
            list(datasets[category].keys()),
            format_func=lambda x: f"• {x}"
        )

        if dataset_name:
            st.header(dataset_name)
            st.info(dataset_descriptions[dataset_name])
            
            df = datasets[category][dataset_name]
            
            if category == "Water & Agriculture (AQUASTAT)":
                st.markdown("### Data Exploration")
                
                # Country selection
                selected_countries = st.multiselect(
                    "Select Countries to Compare:",
                    options=sorted(df['Area'].unique()),
                    default=[]
                )
                
                # Metric category selection
                metric_categories = get_metric_categories(df)
                selected_category = st.selectbox(
                    "Select Metric Category:",
                    options=list(metric_categories.keys())
                )
                
                # Metric selection within category
                selected_metrics = st.multiselect(
                    "Select Metrics to Display:",
                    options=sorted(metric_categories[selected_category]),
                    default=[]
                )
                
                # Filter data based on selections
                if selected_countries:
                    display_df = df[df['Area'].isin(selected_countries)]
                else:
                    display_df = df
                    
                if selected_metrics:
                    display_df = display_df[['Area'] + selected_metrics]
                
                # Handle NA values
                st.markdown("### Data Display Options")
                na_handling = st.radio(
                    "How to handle missing values:",
                    ["Show as NA", "Hide rows with missing values"],
                    horizontal=True
                )
                
                if na_handling == "Hide rows with missing values":
                    display_df = display_df.dropna()
                
                # Display the dataframe
                st.dataframe(
                    display_df.reset_index(drop=True),
                    use_container_width=True,
                    hide_index=True
                )
                
            else:
                # Display regular ecological datasets
                st.dataframe(
                    df.reset_index(drop=True),
                    use_container_width=True,
                    hide_index=True
                )
                            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please check your data files and configurations.")

with tab2:
    show_contact_info()