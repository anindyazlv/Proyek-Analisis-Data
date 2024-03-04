import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_total_cnt_2011(df):
    total_cnt_2011 = df[df['yr'] == 2011].groupby(by=['season'])['cnt'].sum()
    return total_cnt_2011

def create_total_cnt_2012(df):
    total_cnt_2012 = df[df['yr'] == 2012].groupby(by=["season"])['cnt'].sum()
    return total_cnt_2012

def create_total_users_2011(df):
    total_casual_2011 = df[(df['yr'] == 2011)]['casual'].sum()
    total_registered_2011 = df[(df['yr'] == 2011)]['registered'].sum()
    return total_casual_2011, total_registered_2011

def create_total_users_2012(df):
    total_casual_2012 = df[(df['yr'] == 2012)]['casual'].sum()
    total_registered_2012 = df[(df['yr'] == 2012)]['registered'].sum()
    return total_casual_2012, total_registered_2012

day_df = pd.read_csv("/dashboard/main_data.csv")
st.header(':sparkles: Analisis Penyewaan Sepeda :sparkles:')
st.subheader("Hubungan Musim dengan Jumlah Penyewa Sepeda Tahun 2011 dan 2012")

with st.container():
    total_cnt_2011_values = create_total_cnt_2011(day_df)
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(
        x=total_cnt_2011_values.index,
        y=total_cnt_2011_values.values,
        color= '#00BFFF'
    )
    plt.title('Jumlah Penyewa Sepeda Berdasarkan Musim Tahun 2011', loc="center", fontsize=20)
    plt.xlabel('Musim', fontsize=20)
    plt.ylabel('Jumlah Total Penyewa', fontsize=20)
    st.pyplot(fig)

with st.container():
    total_cnt_2012_values = create_total_cnt_2012(day_df)  
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(
        x=total_cnt_2012_values.index,
        y=total_cnt_2012_values.values,
        color= '#00BFFF'
    )
    plt.title('Jumlah Penyewa Sepeda Berdasarkan Musim Tahun 2012', loc="center", fontsize=20)
    plt.xlabel('Musim', fontsize=20)
    plt.ylabel('Jumlah Total Penyewa', fontsize=20)
    st.pyplot(fig)

st.subheader("Distribusi Penyewa Sepeda pada Tahun 2011 dan 2012")

col1, col2 = st.columns(2)
with col1:
    total_casual_2011, total_registered_2011 = create_total_users_2011(day_df) 
    labels = ['Casual', 'Registered']
    colors = ['#87CEFA', '#00BFFF']
    explode = (0.1, 0)

    fig, ax = plt.subplots(figsize=(20, 10))
    ax.pie(
        x=[total_casual_2011, total_registered_2011],
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        explode=explode
    )
    ax.set_title('Distribusi Penyewa Sepeda pada Tahun 2011', loc='center', fontsize=30)
    st.pyplot(fig)

with col2:
    total_casual_2012, total_registered_2012 = create_total_users_2012(day_df) 
    labels = ['Casual', 'Registered']
    colors = ['#87CEFA', '#00BFFF']
    explode = (0.1, 0)

    fig, ax = plt.subplots(figsize=(20, 10))
    ax.pie(
        x=[total_casual_2012, total_registered_2012],
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        explode=explode
    )
    ax.set_title('Distribusi Penyewa Sepeda pada Tahun 2012', loc='center', fontsize=30)
    st.pyplot(fig)
