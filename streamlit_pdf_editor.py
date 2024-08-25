import streamlit as st
from pypdf import PdfReader, PdfWriter

st.title("Personal PDF Editor")
uploadedfile = st.file_uploader("Choose a PDF file")

if uploadedfile is not None:
    name = uploadedfile.name.removesuffix(".pdf")

    reader_pg = PdfReader(uploadedfile).pages[0]
    writer = PdfWriter(clone_from="stamp.pdf")

    writer.pages[0].merge_page(reader_pg, over=False)

    writer.write(f"{name}_e.pdf")
    with open(f"{name}_e.pdf", "rb") as pdf:
        byte = pdf.read()
        st.download_button("Download PDF", byte, file_name=f"{name}_e.pdf", mime="application/pdf")