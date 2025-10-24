import streamlit as st

st.title("My First Streamlit App")
st.subheader("Hello, Streamlit!")
st.header("Welcome to my app")
st.text("This is a simple Streamlit application.")

st.markdown("**Hello, Streamlit!**")
st.markdown("---")
st.caption("This is a caption text.")
st.latex(r"E = mc^2")
st.markdown("---")

json_data = {"name": "Streamlit", "type": "App"}
st.json(json_data)
st.markdown("---")

code = """
print('Hello, Streamlit!')
def func():
    return "This is a function"
"""

st.code(code, language="python")
