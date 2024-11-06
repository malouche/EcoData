def load_css():
    return """
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
    """
