import streamlit as st


def main():
    st.title("Markdown Viewer")

    uploaded_file = st.file_uploader("Choose a Markdown file", type=["md"])

    if uploaded_file is not None:
        # Read the file as a string
        markdown_content = uploaded_file.read().decode("utf-8")

        st.subheader("Markdown Content")
        st.markdown(markdown_content)


if __name__ == "__main__":
    main()
