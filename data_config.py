import pandas as pd

def load_datasets():
    ecological_datasets = {
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
    
    aquastat_datasets = {
        "Agricultural & Economic Indicators": pd.read_csv("data/AQUASTAT_Agriculture_reshaped.csv"),
        "Water Resources & Capacity": pd.read_csv("data/AQUASTAT_Water_resources_reshaped.csv"),
        "Water Usage & Efficiency": pd.read_csv("data/AQUASTAT_Water_use_reshaped.csv"),
        "Environmental Health": pd.read_csv("data/AQUASTAT_Environment_and_Health_reshaped.csv")
    }
    
    return {
        "Ecological Studies": ecological_datasets, 
        "Water & Agriculture (AQUASTAT)": aquastat_datasets
    }

# Dataset descriptions
dataset_descriptions = {
    # Ecological dataset descriptions
    "Beetles Density Study (density vs survival)": "Study examining the relationship between beetle population density and survival rates in controlled conditions.",
    "Ant Biomass Analysis (temporal data)": "Temporal analysis of ant biomass measurements across different months, showing seasonal variations.",
    "Rodent Species Analysis (habitat factors)": "Investigation of rodent species presence in relation to habitat characteristics including shrub coverage and distance factors.",
    "Crab Weight Study (morphometric data)": "Morphometric study comparing body weight and gill weight relationships in crabs.",
    "Forest & Bog Analysis (site comparison)": "Comparative analysis of species richness between forest and bog habitats across different locations and elevations.",
    "Green Site Analysis (site data)": "Site-specific study examining relationships between total mass and burrow counts across different locations.",
    "Biofilm Study (experimental data)": "Experimental study on biofilm development and its effects on serpulid recruitment.",
    "Humidity Analysis (environmental data)": "Investigation of the relationship between humidity levels and weight loss in controlled conditions.",
    "Climate & Vegetation Study (geographical data)": "Large-scale study of climate factors and vegetation patterns across different geographical locations.",
    "Species Area Relationship (ecological data)": "Analysis of species-area relationships, examining how species counts relate to surveyed area size.",
    "Mouse pH Study (physiological data)": "Physiological study measuring pH levels across different mouse populations with various sire and dam combinations.",
    "Island Ratio Analysis (spatial data)": "Spatial analysis of island characteristics and their relationships to presence/absence patterns.",
    "Treatment Length Study (experimental data)": "Experimental study comparing effects of different treatments on specimen length.",
    "Beetle & Plant Analysis (community data)": "Community ecology study examining relationships between beetles, guano, and plant coverage.",
    "Wildlife Mortality Study (survival data)": "Analysis of wildlife mortality patterns across different sex categories and environmental conditions.",
    "Population Treatment Study (temporal comparison)": "Temporal study comparing population responses to different treatments across multiple years.",
    
    # AQUASTAT dataset descriptions
    "Agricultural & Economic Indicators": "Comprehensive country-level data on agricultural GDP, land use, population, and economic indicators including HDI and gender inequality.",
    "Water Resources & Capacity": "Detailed metrics on water resources including precipitation, groundwater, surface water, dam capacity, and water dependencies by country.",
    "Water Usage & Efficiency": "Analysis of water use efficiency, stress levels, and agricultural water withdrawal across countries, including SDG 6.4 indicators.",
    "Environmental Health": "Environmental and health indicators including access to safe drinking water, flood occurrence, and water-related health issues by country."
}

def get_metric_categories(df):
    categories = {
        "Water Metrics": [col for col in df.columns if any(x in col.lower() for x in ['water', 'dam', 'irrigation'])],
        "Population & Demographics": [col for col in df.columns if any(x in col.lower() for x in ['population', 'capita', 'rural', 'urban'])],
        "Economic Indicators": [col for col in df.columns if any(x in col.lower() for x in ['gdp', 'gva', 'economic', 'value'])],
        "Environmental Metrics": [col for col in df.columns if any(x in col.lower() for x in ['area', 'land', 'environment'])],
        "Health & Safety": [col for col in df.columns if any(x in col.lower() for x in ['health', 'disease', 'safe'])],
        "Development Indices": [col for col in df.columns if any(x in col.lower() for x in ['index', 'sdg', 'development'])]
    }
    return {k: v for k, v in categories.items() if any(col in df.columns for col in v)}