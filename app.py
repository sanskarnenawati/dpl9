import streamlit as st
from predict_cost import predict
import numpy as np
import pandas as pd
df= pd.read_csv("rent.csv")
st.title('Home price prediction')

st.write('---')

# area of the house
area = st.slider('Area of the house', 1000, 5000, 1500)

# no. of bedrooms in the house
bedroom = st.number_input('No. of bedrooms')

# no. of balconies in the house
status = st.radio('enter furnishing status', ('furnished',"unfurnished","semifurnished"))

# location = df['location'].drop_duplicates()
p = dict()
loc_list = df["location"].unique().tolist()
for ind, loc in enumerate(loc_list):
    p[loc] = ind
location = st.selectbox(label = "Choose location", options = loc_list)
if st.button('Predict House Price'):
    cost = predict(np.array([area, p[location], status, bedroom]))
    st.text(cost[0])

