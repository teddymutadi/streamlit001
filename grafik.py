import streamlit as st
import matplotlib.pyplot as plt

st.title("Demo Matplotlib + Streamlit")
st.write("Grafik ini dibuat dengan Matplotlib")

# Contoh data
x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 6, 8]

# Buat grafik matplotlib
fig, ax = plt.subplots()
ax.plot(x, y, marker="o")

ax.set_title("Grafik Garis")
ax.set_xlabel("Pupuk")
ax.set_ylabel("Hasil Panen")

# Tampilkan di Streamlit
st.pyplot(fig)

st.success("✅ Grafik Matplotlib berhasil ditampilkan di Streamlit!")




