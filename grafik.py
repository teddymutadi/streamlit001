import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Demo Seaborn + Streamlit")
st.write("Aplikasi ini menampilkan contoh grafik scatterplot menggunakan dataset bawaan Seaborn (`tips`).")

# Ambil dataset bawaan seaborn
df = sns.load_dataset("tips")

# Tampilkan dataframe
st.subheader("Dataset: Tips")
st.dataframe(df.head(10))

# Buat grafik seaborn
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", style="smoker", ax=ax)

# Tampilkan grafik di Streamlit
st.subheader("Scatterplot: Total Bill vs Tip")
st.pyplot(fig)

# Tambahkan catatan
st.success("✅ Grafik Seaborn berhasil ditampilkan di Streamlit!")
