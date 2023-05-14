import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd

def get_spacecraft_location():
    # Get the spacecraft location from the backend API
    response_get_isslocation = requests.get(f"http://backend:8000/isslocation") 
    location = response_get_isslocation.json()
    location_df = pd.DataFrame({"latitude": [float(location["latitude"])], "longitude": [float(location["longitude"])]})
           
    return location_df

def refresh():
    """Function to refresh the Streamlit script."""
    components.html("<script>location.reload();</script>")

# Streamlit app
def app():
    st.title("Spacecraft Trajectory Visualization")

    location = get_spacecraft_location()

    # Display the spacecraft location on a map using streamlit-leaflet
    if not location.empty:
        st.map(location ,zoom=3)
    
    if st.button("Update"):
        refresh()
      
if __name__ == '__main__':
    app()