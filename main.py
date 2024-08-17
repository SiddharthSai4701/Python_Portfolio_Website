import streamlit as st

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