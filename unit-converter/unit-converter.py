import streamlit as st

def convert_units(value , unit_from, unit_to):

    conversions = {
           "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
           "kilometers_meters": 1000,  # 1 kilometer = 1000 meters
           "grams_kilograms": 0.001,  # 1 gram = 0.001 kilograms
           "kilograms_grams": 1000,  # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}" # generate a key based on the user input

    # Check if the units are the same
    if unit_from == unit_to:
        return value  # No conversion needed
    
    # Perform the conversion using the generated key and the conversions dictionary
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not available"
    

st.title("Unit Converter")
value = st.number_input("Enter the value you want to convert" , min_value=1.0 , step=1.0)
unit_from = st.selectbox("Convert From" , ["meters", "kilometers" , "grams", "kilograms"])
unit_to = st.selectbox("Convert To" , ["meters", "kilometers" , "grams", "kilograms"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"{value} {unit_from} is equal to {result} {unit_to}")