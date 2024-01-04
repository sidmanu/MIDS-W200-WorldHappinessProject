import streamlit as st
import pandas as pd


# to run locally, execute: `streamlit run st_test.py`
st.set_page_config(layout="wide")

st.subheader('WHR Life Ladder Scores - Country by Year')
ll_ay_scores_df = pd.read_csv("./data/processed/WHR_LifeLadder_20052022.csv", index_col="Country name")
st.dataframe(ll_ay_scores_df[["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]])

st.subheader('WHR Life Ladder Scores - Year by Country')
ll2_ay_scores_df = pd.read_csv("./data/processed/WHR_LifeLadder_T_20052022.csv", index_col="Year")
st.write(ll2_ay_scores_df)
