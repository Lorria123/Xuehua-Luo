import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')


st.title('Exploratory Analysis about Coffee')
st.subheader('by Xuehua Luo & Peiyuan Wang')


df = pd.read_csv('coffee-listings-from-all-walmart-stores.csv')

fig,ax = plt.subplot(figsize=(20,5))
ax = sns.heatmap(df.corr(), annot=True, cmap='Blues')
ax.set_title('Correlation between variables')
plt.show()
st.pyplot(fig)




