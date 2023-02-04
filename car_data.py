import streamlit as st 
import pandas as pd
import numpy as np 
from datetime import time

used_car_data = "Nigerian_Car_Prices.csv"
data_import = pd.read_csv(used_car_data)
df = data_import.copy()

st.title("Used Nigerian Cars Data")
# Drops rows that have nissing values as well as a redundant Index column
df = df.dropna(axis=0)
df.drop(["Index"], axis=1, inplace=True)
# Fixes the Indeces thet were messed up after dropping rows
num = range(len(df))
index = []
for i in num:
    index.append(i)
df.index = index
# Turns any column with float numbers to int
def to_int(list):
    if df[list].array:
        index = []
        for i in df[list].array:
            index.append(int(i))
    return index

df['Year of manufacture'] = to_int("Year of manufacture")
df["Mileage"] = to_int('Mileage')
df['Engine Size'] = to_int('Engine Size')
# df["Price"] = to_int('Price')
# df['Mileage'] = int(i) for i in df['Mileage']
st.dataframe(df)
# This creates a sidebar that can be used to select the different car makes and Price in order to query the data
st.sidebar.header("Query data")
sorted_make = df.Make.unique()
selected_make = st.sidebar.multiselect("Select car Make",options=sorted_make)

sorted_price = df.Price.sort_values(ascending=False).unique()
selected_price = st.sidebar.selectbox("Select car price", options=sorted_price)

sorted_condition = df.Condition.sort_values().unique()
selected_condition = st.sidebar.selectbox("Select Condition of Car", options=sorted_condition)


st.subheader("Search by Make")
def get_make(sel_make):
    make = []
    index = []
    for i in df.Make:
        if i in sel_make:
            make.append(i)
    for j in pd.Series(make).unique():
        dfs = df[df.Make == j]
        index.append(dfs)
    if len(index) < 1:
        st.write("select car make")
    else:
        # d = pd.concat((index)).reindex(df.Make.index)
        # d = pd.DataFrame(index)
        st.dataframe(index)
        # st.dataframe(d)
get_make(selected_make)


st.subheader("Search by Price")
def get_price(price):
    for i in df.Price:
        if i == price:
            return df[df.Price == price]
st.dataframe(get_price(selected_price))

st.subheader("Search by Condition")
def get_condition(condition):
    for i in df.Condition:
        if i == condition:
            return df[df.Condition == condition]
st.dataframe(get_condition(selected_condition))

# def query_data(make, condition, price):
#     if selected_condition && selected_price && selected_make:
#         st.dataframe(
#             df[df["Price"] = selected_price && df['Make'] = selected_make, &&]
#             )