import streamlit as st
from markdownify import markdownify as md
from bs4 import BeautifulSoup
import emoji
import re

# Function to beautify HTML and convert it to Markdown
def beautify_html_to_markdown(html_content):
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove unwanted tags or content
    for script in soup(["script", "style"]):
        script.decompose()

    # Convert the cleaned-up HTML to markdown
    markdown_content = md(str(soup))

    # Beautify the markdown: Add emojis and proper formatting
    markdown_content = add_emoji_to_headings(markdown_content)

    return markdown_content

# Function to add emojis based on sections
def add_emoji_to_headings(content):
    # Define emojis for common topics
    emoji_dict = {
        "Python": "🐍",
        "JavaScript": "📜",
        "Web Development": "🌐",
        "Courses": "🎓",
        "Resources": "📚",
        "Deployment": "🚀",
        "Design Patterns": "🔧",
    }
    
    for key, value in emoji_dict.items():
        content = re.sub(f"(#{key})", f"{value} \\1", content, flags=re.IGNORECASE)
    
    return content

# Streamlit UI
st.title("HTML to Beautified Markdown Converter")

# Upload HTML file
uploaded_file = st.file_uploader("Upload an HTML file", type="html")

if uploaded_file is not None:
    # Read the uploaded file content
    html_content = uploaded_file.read().decode("utf-8")

    # Beautify the HTML content
    beautified_markdown = beautify_html_to_markdown(html_content)

    # Display the beautified markdown content
    st.subheader("Beautified Markdown")
    st.markdown(beautified_markdown)

    # Download button for the beautified markdown
    st.download_button(
        label="Download Beautified Markdown",
        data=beautified_markdown,
        file_name="beautified_markdown.md",
        mime="text/markdown"
    )
