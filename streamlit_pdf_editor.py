import streamlit as st
from pypdf import PdfReader, PdfWriter

st.title("Personal PDF Editor")
uploadedfile = st.file_uploader("Choose a PDF file")

with open("2.pdf", "rb") as pdf:
    byte = pdf.read()
    st.download_button("Download PDF", byte, file_name="2.pdf", mime="application/pdf")

# if uploadedfile is not None:
#     with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
#         f.write(uploadedfile.getbuffer())
    
# doc = pymupdf.open(uploaded_files)
# st.write(uploaded_files.name.removesuffix(".pdf"))
# name = uploaded_files.name.removesuffix(".pdf")
# for pg_no in range(len(doc)):
#     doc[pg_no].insert_image(pymupdf.Rect(353, 87, 560, 106), filename = "./Picture1.png")
# doc.save(f"{name}_e.pdf")
# doc.close()
# with open(f"{name}_e.pdf", "rb") as f:
#     pdf_byte = f.read()
#     st.download_button("Download PDF", pdf_byte, file_name=f"{name}_e.pdf", mime="application/pdf")
