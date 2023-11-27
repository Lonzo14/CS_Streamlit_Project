# input_stage.py
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import requests

def get_location_from_address(address):
    """Convert an address to latitude and longitude using Maps.co Geocoding API."""
    base_url = "https://geocode.maps.co/search"
    params = {"q": address}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            # Assuming the first result is the most relevant
            latitude = data[0]["lat"]
            longitude = data[0]["lon"]
            return latitude, longitude
    return None, None

def input_stage():
    st.title("Business Locator - Input Stage")

    # Location input methods
    st.write("## Select Your Location")
    method = st.radio("Choose your method to input location:", ("Enter Coordinates", "Share Location", "Enter Address"))

    if method == "Enter Coordinates":
        lat = st.number_input("Enter Latitude", format="%.6f")
        lon = st.number_input("Enter Longitude", format="%.6f")
        user_location = (lat, lon)

    elif method == "Share Location":
        loc_button = Button(label="Get Location")
        loc_button.js_on_event("button_click", CustomJS(code="""
            navigator.geolocation.getCurrentPosition(
                (loc) => {
                    document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
                }
            )
            """))
        result = streamlit_bokeh_events(
            loc_button,
            events="GET_LOCATION",
            key="get_location",
            refresh_on_update=False,
            override_height=75,
            debounce_time=0)

        if result:
            if "GET_LOCATION" in result:
                lat, lon = result.get("GET_LOCATION").values()
                user_location = (lat, lon)
                st.write(f"Coordinates: {user_location}")
            else:
                user_location = (None, None)
        else:
            user_location = (None, None)

    elif method == "Enter Address":
        address = st.text_input("Enter your address")
        user_location = get_location_from_address(address)
        if user_location[0] is not None:
            st.write(f"Coordinates: {user_location}")

    # Business category selection
    business_category = st.selectbox("Select Business Category", ["Restaurant", "Cafe", "Retail", "Other"])

    return user_location, business_category
