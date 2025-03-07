import streamlit as st

def length_convertor(value, from_unit, to_unit):
    conversion_factors = {
        'Meters': 1,
        'Kilometers': 0.001,
        'Miles': 0.000621371,
        'Feet': 3.28084
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def weight_convertor(value, from_unit, to_unit):
    conversion_factors = {
        'Kilograms': 1,
        'Grams': 1000,
        'Pounds': 2.20462,
        'Ounces': 35.274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    return value

st.title("📏 Unit Convertor")

category = st.selectbox("Select Category:", ["Length", "Weight", "Temperature"])

if category == "Length":
    units = ["Meters", "Kilometers", "Miles", "Feet"]
    convert_function = length_convertor
elif category == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    convert_function = weight_convertor
else:
    units = ["Celsius", "Fahrenheit"]
    convert_function = temperature_convertor

value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit:", units)
to_unit = st.selectbox("To Unit:", units)

if st.button("Convert"):
    result = convert_function(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
