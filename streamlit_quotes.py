import streamlit as st

def read_file(file):
    return file.read().decode("utf-8")

def main():
    st.header("Quotes Viewer")
    st.sidebar.title("Upload files")
    uploaded_files = st.sidebar.file_uploader("---", type=["txt"], accept_multiple_files=True)
    # selected_file = st.sidebar.radio("Select a file", uploaded_files, format_func=lambda file: file.name if file is not None else "None")
    # select a file from the uploaded files and display it
    selected_file = st.selectbox("Select a file", uploaded_files, format_func=lambda file: file.name if file is not None else "None") # type: ignore
    if selected_file is not None:
        st.header(selected_file.name)
        
        file_contents = read_file(selected_file)
        st.write(file_contents)

if __name__ == "__main__":
    main()
