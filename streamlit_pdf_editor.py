import streamlit as st
import pymupdf

st.title("Personal PDF Editor")
st.image("./Picture1.png")
uploaded_files = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_files:
    st.write(uploaded_files.name.removesuffix(".pdf"))
    name = uploaded_files.name.removesuffix(".pdf")
    doc = pymupdf.open(uploaded_files)
    for pg_no in range(len(doc)):
        doc[pg_no].insert_image(pymupdf.Rect(353, 87, 560, 106), filename = "./Picture1.png")
    doc.save(f"{name}_e.pdf")
    doc.close()
    with open(f"{name}_e.pdf", "rb") as f:
        pdf_byte = f.read()
        st.download_button("Download PDF", pdf_byte, file_name=f"{name}_e.pdf", mime="application/pdf")
