import streamlit as st
from drug_similarity import get_similar_drugs

st.set_page_config(page_title="Drug Name Similarity Finder", page_icon="💊")

st.title("💊 Drug Name Similarity Finder")
st.write("Find correct medicine names even if you misspell or type partial names.")

user_input = st.text_input("Enter a drug name")

if st.button("Find Similar Names"):
    if user_input.strip() == "":
        st.warning("Please enter a drug name.")
    else:
        matches = get_similar_drugs(user_input)
        if matches:
            st.success("Did you mean:")
            for m in matches:
                st.write(f"👉 {m}")
        else:
            st.error("No similar drug names found.")
