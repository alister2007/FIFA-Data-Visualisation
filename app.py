import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_data
def load_data():
    df = pd.read_excel("data/data.xlsx")
    df['Date']=pd.to_datetime(df['Date'])
    return df
df=load_data()
st.title("FIFA Data Visualisation")

matches=df['Date'].nunique()
col1,col2,col3=st.columns(3)
col1.metric("Total Matches",matches)
col2.metric("Total Goals",df['Goals'].sum())
col3.metric("Total Assists",df['Assists'].sum())

st.markdown("##Top Player Ranking")
table_data=df.groupby(['Player','Team'],as_index=False)[['Goals','xG']].sum().nlargest(10,'Goals')
st.dataframe(table_data,use_container_width=True,hide_index=True)
