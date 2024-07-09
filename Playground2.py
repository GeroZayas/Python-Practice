import streamlit as st
import pandas as pd
from io import StringIO


def get_markdown_from_uploaded_file(file):
    content = file.read()
    markdown = StringIO(content.decode("utf-8"))
    df = pd.read_csv(markdown, delimiter="|", engine="python")
    return df.iloc[0][0]


def main():
    st.title("Markdown Viewer")

    uploaded_file = st.file_uploader("Choose a Markdown file", type=["md"])

    if uploaded_file is not None:
        markdown_content = get_markdown_from_uploaded_file(uploaded_file)

        st.subheader("Markdown Content")
        st.write(markdown_content)


if __name__ == "__main__":
    main()
