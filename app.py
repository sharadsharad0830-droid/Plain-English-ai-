import streamlit as st

st.set_page_config(
    page_title="Plain English",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Plain English")
st.subheader("Complex documents. Simple answers.")

st.write(
    "Understand your medical reports, "
    "rental agreements and insurance policies "
    "with the help of AI."
)

st.divider()

st.header("Upload your document")

document_type = st.selectbox(
    "Select document type",
    [
        "Medical Report",
        "Rental Agreement",
        "Insurance Policy"
    ]
)

uploaded_file = st.file_uploader(
    "Choose your PDF or image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:
    st.success("Document uploaded successfully!")

    st.write("File name:", uploaded_file.name)

    if st.button("Analyze My Document"):
        st.info(
            "Your document is ready for AI analysis. "
            "We will connect the AI engine in the next step."
        )

st.divider()

st.caption(
    "Plain English AI | Making complex documents simple."
)

st.warning(
    "This tool provides explanations, not medical "
    "diagnoses or professional legal advice."
)
