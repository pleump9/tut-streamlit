import streamlit as st
import pandas as pd

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

st.markdown("---")
st.write("This is a simple write statement in Streamlit.")
st.metric(label="Sample Metric", value="120ms⁻¹ ", delta="+15ms⁻¹")
st.metric(label="Sample Metric", value="120ms⁻¹ ", delta="-14ms⁻¹")

st.markdown("---")
table = pd.DataFrame({"Column A": [1, 2, 3], "Column B": ["A", "B", "C"]})
st.table(table)
st.dataframe(table)

st.markdown("---")
st.image("assets/cat.webp")


def checkbox_on_change():
    print("Checkbox state changed!")


state = st.checkbox("Check me out!", on_change=checkbox_on_change)
if state:
    st.write("Checkbox is checked!")
else:
    pass

radio_btn = st.radio("Select an option:", options=("Option 1", "Option 2", "Option 3"))
print(radio_btn)


def btn_click():
    print("Button clicked!")


btn = st.button("Click Me!", on_click=btn_click)

select = st.selectbox("Choose an option:", options=["Option A", "Option B", "Option C"])
print(select)

multi_select = st.multiselect(
    "Select multiple options:", options=["Option X", "Option Y", "Option Z"]
)
st.write(multi_select)
