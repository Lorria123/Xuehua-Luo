import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')


st.title('Exploratory Analysis about Coffee')
st.subheader('by Xuehua Luo & Peiyuan Wang')


df = pd.read_csv('coffee-listings-from-all-walmart-stores.csv')

st.subheader('Correlation between variables')
sns.heatmap(df.corr(), annot=True, cmap='Blues')
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

st.subheader('The Most Popular seller:')
fig2,ax2 = plt.subplots(figsize=(40,10))
ax2 = df.seller_name.value_counts().head(10).sort_values().plot(kind='barh')
ax2.bar_label(ax2.containers[0])
ax2.set_title('Most Popular Coffee Seller on Walmart')
st.pyplot(fig2)

df['rating_level'] = pd.cut(df['rating'],[0,1,2,3,4,5], labels=['0-1','1-2','2-3','3-4','4-5'])

rating_filter = st.sidebar.selectbox(
    'rating_level',
    df.rating_level.unique()
    )

df = df[df.raing_level == rating_filter]


st.subheader('What coffee title has the most rating?(on range)')
st.write(df.query('rating == rating.max()')[['rating','reviews','title']].sort_values(
    by='reviews', ascending=False
).head(20).style.hide(axis='index').background_gradient(cmap='Greens'))



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

fig3 = plt.figure(figsize=(15, 5))
if sd == "Total plot":
    sns.jointplot(data=df, x='price', y='weight_formatted_to_gramms', kind='hex')
    
elif sd == "Details plot":
    g = sns.PairGrid(df[['price', 'weight_formatted_to_gramms']], height=4)
    g.map_upper(sns.histplot)
    g.map_lower(sns.kdeplot, fill=True)
    g.map_diag(sns.histplot, kde=True)

plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()