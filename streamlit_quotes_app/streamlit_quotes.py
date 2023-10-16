import streamlit as st

# Define custom color palette
custom_primary = "#003049"  # Dark blue
custom_secondary = "#D62828"  # Red
custom_background = "#F8F9FA"  # Light gray

def read_file(file):
    return file.read().decode("utf-8")

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Quotes Viewer",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state="auto",
    )
    
    
    st.header("Quotes Viewer")
    st.sidebar.title("Upload files")
    uploaded_files = st.sidebar.file_uploader("---", type=["txt"], accept_multiple_files=True)

    # Select a file from the uploaded files and display it
    selected_file = st.selectbox("Select a file", uploaded_files, format_func=lambda file: file.name if file is not None else "None") # type: ignore
    if selected_file is not None:
        st.header(selected_file.name)

        file_contents = read_file(selected_file)
        st.markdown(file_contents)

if __name__ == "__main__":
    main()
