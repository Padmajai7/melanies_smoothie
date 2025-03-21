# Import python packages
import streamlit as st
 # Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write("Choose the fruits you want in your custom Smoothie!")
from snowflake.snowpark.functions import col

cnx=st.connection("snowflake")
session=cnx.session()

 
