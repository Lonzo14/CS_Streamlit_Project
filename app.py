import streamlit as st
import input_stage  # Importing the input_stage module

def main():
    st.title("Business Locator Application")

    # Calling the input stage function
    user_location, business_category = input_stage.input_stage()

    # Display the results from the input stage
    st.write("### Selected Location and Category")
    st.write(f"Location: {user_location}")
    st.write(f"Category: {business_category}")

    # Here you can add further steps like API_stage and Output_stage

if __name__ == "__main__":
    main()