import streamlit as st

def show_contact_info():
    st.title("Contact Information")
    st.write("### Dhafer Malouche")
    st.write("This application was developed by Dhafer Malouche.")
    
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
        Most of the data are from the book: *Biostatistical Design and Analysis Using R: A Practical Guide* by Murray Logan (2010), Wiley-Blackwell. ISBN: 978-1-405-19008-4
        
        This interactive interface allows users to explore various ecological and biological datasets used in the book's examples and exercises.
        
        For any questions or suggestions about this app's functionality, please don't hesitate to reach out through any of the channels above.
    """)
