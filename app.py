import streamlit as st
import Input_stage

def main():
    st.title("Business Locator Application")

    # Calling the input stage function
    user_location, business_category = Input_stage.input_stage()

    # Display the results from the input stage
    st.write("### Selected Location and Category")
    st.write(f"Location: {user_location}")
    st.write(f"Category: {business_category}")



if __name__ == "__main__":
    main()