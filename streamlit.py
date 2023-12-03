# Preprocessing
import streamlit as st
import pandas as pd
df=pd.read_csv('instagram_data.csv')
import string
import datetime
def get_date(j):
    x=j.split("' ")[3][9:]
    last=x.find('media_type')
    date=j.split("' ")[3][9:last+7]
    date=date.replace("datetime.datetime(", "").replace(");", "").replace("tzinfo=datetime.timezone.utc", "")[:-2]
    if len(date)>=20:
        date=datetime.datetime.strptime(date,"%Y, %m, %d, %H, %M, %S")
    else:
        date=datetime.datetime.strptime(date,"%Y, %m, %d, %H, %M")
    return date
import re
def get_comment(j):
    start_com=j.split("' ")[4].find('comment_count')
    comment_count=int([''.join(re.findall('\d',j.split("' ")[4][start_com:].split()[0]))][0])
    return comment_count
def get_view(j):
    start_view=j.split("' ")[5].find('view_count')
    end_view=j.split("' ")[5].find('video_duration')
    view_count=int([''.join(re.findall('\d',j.split("' ")[5][start_view:end_view-1]))][0])
    return view_count
view_count=df['media_id'].apply(get_view)
post_date=df['media_id'].apply(get_date)
comment_count=df['media_id'].apply(get_comment)
df['view_count']=view_count
df['post_date']=post_date
df['comment_count']=comment_count
# Visualize
import plotly.express as px
fig1=px.line(df['post_date'].apply(lambda x:x.hour).value_counts().sort_index(),title='Comment Timeseries Daily')
fig2=px.pie(names=df['user_private'].value_counts().keys(),values=df['user_private'].value_counts().values,title='Private Account Comment Profile Proportion')
df['hour']=df['post_date'].apply(lambda x:x.hour)
df['view_count']=df['view_count'].astype('int')
fig3=px.line(df[['view_count','hour']].groupby('hour').mean(),title='View Count Timeseries Daily')
df.sort_values('view_count',ascending=False)
def caption_text(j):
    start=j.split("' ")[4].find('caption_text')+13
    caption=j.split("' ")[4][start:]
    return caption
df['caption']=df['media_id'].apply(caption_text)
top_5=df[['view_count','caption']].groupby('caption').mean().reset_index().sort_values('view_count',ascending=False).reset_index(drop=True).head()
top_5['caption']=top_5['caption'].apply(lambda x:x[0:100])
fig4=px.bar(y=top_5['caption'],x=top_5['view_count'],orientation='h',title='Top View Based on Caption')
from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = df['text'].values
text=[i.lower() for i in text]
k=['pak','keren','banget']
while(k in text):
    text.remove(k)
wordcloud = WordCloud().generate(str(text))
# Streamlit
st.set_page_config(layout='wide')
st.title('Andi Asmara Instagram Dashboard')
tab1,tab2=st.tabs(['Dashboard Instagram','Forms'])

with tab1:
    col1,col2=st.columns([7,3])
    with st.container():
        with col1:
            st.plotly_chart(fig1,use_container_width=True)
        with col2:
            st.plotly_chart(fig2,use_container_width=True)
    with st.container():
        st.plotly_chart(fig3,use_container_width=True)
    with st.container():
        st.plotly_chart(fig4,use_container_width=True)
with tab2:
    with st.form('Data Pendukung'):
        nama=st.text_input('Nama')
        alamat=st.text_input('Alamat')
        umur=st.number_input('Umur')
        pekerjaan=st.text_input('Pekerjaan')
        st.form_submit_button('Submit')
        
