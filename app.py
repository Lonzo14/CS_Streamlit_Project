import streamlit as st
import Input_stage
import Output_stage


def main():
    st.title("Business Locator Application")

    # Calling the input stage function
    user_location, business_category = Input_stage.input_stage()

    # Display the results from the input stage
    st.write("### Selected Location and Category")
    st.write(f"Location: {user_location}")
    st.write(f"Category: {business_category}")



    # User inputs
    lat = st.number_input('Latitude', value=40.7128)  # Default values as an example
    lon = st.number_input('Longitude', value=-74.0060)
    radius_km = st.number_input('Radius in km', value=5)
    business_type = st.selectbox('Business Type', ['Restaurant', 'Cafe', 'Retail'])

    # Button to perform action
    if st.button('Find Businesses'):
        user_coordinates = (lat, lon)
        # Assuming 'data' is your dataset
        results = businesses_in_radius(user_coordinates, radius_km, business_type, data)
        
        if results:
            # Prepare DataFrame for st.map
            df = pd.DataFrame({
                'lat': [res['coordinates'][0] for res in results],
                'lon': [res['coordinates'][1] for res in results]
            })
            st.map(df)
            # Optionally display details in a table
            st.write(results)
        else:
            st.write("No businesses found within the specified radius.")


if __name__ == "__main__":
    main()



