import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')


st.title('Exploratory Analysis about Coffee')
st.subheader('by Xuehua Luo & Peiyuan Wang')


df = pd.read_csv('coffee-listings-from-all-walmart-stores.csv')

ax = sns.heatmap(df.corr(), annot=True, cmap='Blues')
ax.set_title('Correlation between variables')


st.subheader('The Most Rating:')
st.write(df.query('rating == rating.max()')[['title', 'rating', 'reviews']].sort_values(
    by='reviews', ascending=False
).style.hide(axis='index').background_gradient(cmap='Greens'))


st.subheader('The Most Reviews:')
st.write(df.query('reviews == reviews.max()')[['title', 'reviews']])


st.subheader('The Most Popular seller:')
fig,ax = plt.subplots(1,5,figsize=(20,5))
ax = df['seller_name'].value_counts().head(10).sort_values().plot.hist(kind='barh')
ax.bar_label(ax.containers[0])
ax.set_title('Most Popular Coffee Seller on Walmart')



st.subheader('The Most Frequent Coffee Weight: 300-500g')
sns.jointplot(data=df, x='price', y='weight_formatted_to_gramms', kind='hex')

g = sns.PairGrid(df[['price', 'weight_formatted_to_gramms']], height=4)
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot, fill=True)
g.map_diag(sns.histplot, kde=True)

st.pyplot(fig)