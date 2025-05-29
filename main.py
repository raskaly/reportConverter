import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="SAP Report to CSV Converter", layout="centered")
st.title("📄 SAP Report to CSV Converter")

uploaded_files = st.file_uploader(
    "Upload one or more SAP reports (.xlsx, .xls, .csv, .txt)",
    type=["xlsx", "xls", "csv", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        base_name = os.path.splitext(file.name)[0]

        try:
            # Load file into DataFrame
            if file_ext == '.xlsx':
                df = pd.read_excel(file)
            elif file_ext == '.xls':
                df = pd.read_excel(file)
            elif file_ext == '.txt':
                df = pd.read_csv(file, delimiter='\t')
            elif file_ext == '.csv':
                df = pd.read_csv(file)
            else:
                st.warning(f"Unsupported file type: {file.name}")
                continue

            st.success(f"✅ Converted: {file.name}")

            # Preview first rows
            with st.expander(f"🔍 Preview: {file.name}"):
                st.dataframe(df.head(10))

            # Download CSV
            csv_bytes = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=f"⬇️ Download CSV for {file.name}",
                data=csv_bytes,
                file_name=f"{base_name}.csv",
                mime='text/csv'
            )

        except Exception as e:
            st.error(f"❌ Error processing {file.name}: {e}")
