import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Create two column objects
col1, col2 = st.columns(2)

# Open the first column object and create an image object instance
with col1:
    col1.image("images/photo.png")

with col2:
    col2.title("Siddharth Vijay Sai")
    content = """
    Hi there! I'm Siddharth and I'm currently working as a Full Stack Engineer at Nimbly Technologies.
    I love to code and I've been meaning to develop a small portfolio website to showcase all the projects that I've worked on since I started learning to code!
    I'd love to connect and collaborate so feel free to connect with me on LinkedIn!
    """
    st.info(content)


st.text("Below are the projects I've worked on!")
data = pd.read_csv("data.csv", sep=";")

# Add an empty column to separate the projects
# The listg values contain the ratios of the widths of the coulmns
# Eg col3 is 3 times larger than empty_col
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# 20 projects
# First column (col3) will have the first 10 projects
# Second column (col4) will have the next 10 projects
with col3:
    for index, row in data[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        # st.write("[Source Code](https://github.com/SiddharthSai4701/forage-lyft-starter-repo)")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in data[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        # st.write("[Source Code](https://github.com/SiddharthSai4701/forage-lyft-starter-repo)")
        st.write(f"[Source Code]({row['url']})")