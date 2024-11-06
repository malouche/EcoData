import streamlit as st

def show_contact_info():
    st.title("Contact Information")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        📧 **Email**: dhafer.malouche@qu.edu.qa  
        🌐 **Website**: https://dhafermalouche.net  
        💼 **LinkedIn**: https://linkedin.com/in/dhafer-malouche-b54629b/
        """)
    
    st.write("### About This App")
    st.write("""
        This application is designed to facilitate accessing two types of datasets:

        **Ecological & Biological Data**: Most of these datasets are from the book: *Biostatistical Design and Analysis Using R: A Practical Guide* by Murray Logan (2010), Wiley-Blackwell. ISBN: 978-1-405-19008-4. These datasets cover various ecological studies including beetle populations, ant biomass, rodent species, and more.

        **AQUASTAT Data**: AQUASTAT is FAO's (Food and Agriculture Organization) global water information system, providing comprehensive data on:
            - Water resources and their use
            - Agricultural water management
            - Water and food security
            - Environmental sustainability

            
        For any questions or suggestions about this app's functionality, please don't hesitate to reach out through any of the channels above.

    """)
