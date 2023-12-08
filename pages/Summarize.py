# Import necessary  libraries

import streamlit as st
from langchain.document_loaders import PyPDFLoader

from sphere.summarization_manager import main as summarization_manager


def get_documents(url):
    return PyPDFLoader(url, extract_images=True)


st.set_page_config(page_title=" Optim Assistant", layout="wide")


st.title("Résume")
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Choose your .pdf file", type="pdf")

    txt = st.text_area("Enter your text here")
with col2:
    if uploaded_file is not None:
        with st.spinner("Indexation en cours..."):
            # save uploaded file on file "data"
            with open(f"data/{uploaded_file.name}", "wb") as f:
                f.write(uploaded_file.getbuffer())

            pdf_reader = get_documents(f"data/{uploaded_file.name}")
            df = summarization_manager(file=pdf_reader, file_type="pdf")
        st.write(df)
    if txt:
        with st.spinner("Indexation en cours..."):
            df = summarization_manager(file=txt, file_type="txt")
        st.write(df)
