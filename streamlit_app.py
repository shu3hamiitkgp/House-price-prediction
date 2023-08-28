import streamlit as st
import os
import requests
from server import utils



st.title("Predicting house prices in Bengaluru")
    
location_list=utils.get_location_names()

location = st.selectbox("Select the location",location_list)
bhk=st.selectbox("Select the number of bedrooms",['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11','12','13'])
bath=st.selectbox("Select the number of bathrooms",['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11','12','13'])
balcony=st.selectbox("Select the number of balconies",['0','1', '2', '3'])
area= st.text_input("Enter the total square feet area (Suggested range 300-12000 sqft)",placeholder='eg. 1000')

if st.button("Get the price"):
    price=utils.get_estimated_price(location,area,bhk,balcony,bath)
    st.markdown("The estimated price of the house is **{}** lakhs".format(price))
