import streamlit as st
import Input_stage
import Output_stage
import pandas as pd
import math


def main():
    st.title("Business Locator Application")

    # Calling the input stage function
    user_location, business_category = Input_stage.input_stage()

    # Display the results from the input stage
    st.write("### Selected Location and Category")
    st.write(f"Location: {user_location}")
    st.write(f"Category: {business_category}")

    # User inputs
    radius_km = st.number_input('Radius in km', value=5)
    business_type = st.selectbox('Business Type', ['Restaurant', 'Cafe', 'Retail'])

   # Example usage
    data = [
        {'name': 'Restaurant A', 'review': 'Excellent', 'type': 'Restaurant', 'latitude': 40.7128, 'longitude': -74.0060},
        {'name': 'Restaurant B', 'review': 'Good', 'type': 'Restaurant', 'latitude': 40.73, 'longitude': -74.0060},
        {'name': 'Restaurant C', 'review': 'Bad', 'type': 'Restaurant', 'latitude': 40.74, 'longitude': -74.0060},
        {'name': 'Cafe B', 'review': 'Very Good', 'type': 'Cafe', 'latitude': 40.7328, 'longitude': -74.0160},
        {'name': 'Retail C', 'review': 'Good', 'type': 'Retail', 'latitude': 40.7528, 'longitude': -74.0260}
        ]
    # Button to perform action
    if st.button('Find Businesses'):
        # Use user_location as the coordinates
        results = Output_stage.businesses_in_radius(user_location, radius_km, business_type, data)
        
        if results:
            # Prepare DataFrame for st.map
            df = pd.DataFrame({
                'lat': [res['coordinates'][0] for res in results],
                'lon': [res['coordinates'][1] for res in results],
                'name': [res['name'] for res in results],
                'review': [res['review'] for res in results]
            })
            st.map(df)
            # Optionally display details in a table
            st.write(results)
        else:
            st.write("No businesses found within the specified radius.")

if __name__ == "__main__":
    main()

