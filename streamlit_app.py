import streamlit as st
import pandas as pd
from io import StringIO

st.title("📘 Grade Checker")

name = st.text_input("Student Name")
subject = st.text_input("Subject")
marks = st.number_input("Marks", 0, 100)

if st.button("Check"):
    status = "Pass" if marks >= 40 else "Fail"
    st.write(f"**{name}** has **{status}ed** in **{subject}** with **{marks}** marks.")

    df = pd.DataFrame([[name, subject, marks, status]],
                      columns=["Name", "Subject", "Marks", "Status"])
    st.dataframe(df)

    # Convert DataFrame to CSV for download
    csv = df.to_csv(index=False)
    
    st.download_button(
        label="Download result as CSV",
        data=csv,
        file_name='grade_result.csv',
        mime='text/csv',
    )

