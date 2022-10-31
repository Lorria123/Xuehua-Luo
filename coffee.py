import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')


st.title('Exploratory Analysis about Coffee')
st.subheader('by Xuehua Luo & Peiyuan Wang')


df = pd.read_csv('coffee-listings-from-all-walmart-stores.csv')

st.subheader('The Most Popular seller:')
fig1,ax = plt.subplots(2,1,figsize=(20,5))
ax[0] = df.seller_name.value_counts().head(10).sort_values().plot(kind='barh')
ax[0].bar_label(ax.containers[0])
ax[0].set_title('Most Popular Coffee Seller on Walmart')

ax[1] = sns.heatmap(df.corr(), annot=True, cmap='Blues')
ax[1].set_title('Correlation between variables')

st.pyplot()



st.subheader('The Most Rating:')
st.write(df.query('rating == rating.max()')[['title', 'rating', 'reviews']].sort_values(
    by='reviews', ascending=False
).head(10).style.hide(axis='index').background_gradient(cmap='Greens'))


st.subheader('The Most Reviews:')
st.write(df.query('reviews == reviews.max()')[['title', 'reviews']])



st.subheader('The Most Frequent Coffee Weight: 300-500g')

sd = st.selectbox(
    "Select a Plot", #Drop Down Menu Name
    [
    "Total plot", #First option in menu
    "Details plot"   #Seconf option in menu
    ]
)

fig2 = plt.figure(figsize=(15, 5))
if sd == "Total plot":
    sns.jointplot(data=df, x='price', y='weight_formatted_to_gramms', kind='hex')
    
elif sd == "Details plot":
    g = sns.PairGrid(df[['price', 'weight_formatted_to_gramms']], height=4)
    g.map_upper(sns.histplot)
    g.map_lower(sns.kdeplot, fill=True)
    g.map_diag(sns.histplot, kde=True)

plt.show()
st.pyplot()

