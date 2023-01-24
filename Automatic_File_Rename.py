# This script automatically changes the name of the each file in the current folder
# It gets hold of the first 14 words in each file to rename it
# It works with *.docx , *.md, *.txt files

import os
import docx
import re

# specify the directory where the files are located
directory = os.getcwd()

# loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt') or filename.endswith('.docx') or filename.endswith('.md'):
        # open the file
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as f:
                first_line = f.readline()
        elif filename.endswith('.docx'):
            doc = docx.Document(os.path.join(directory, filename))
            first_line = doc.paragraphs[0].text
        elif filename.endswith('.md'):
            with open(os.path.join(directory, filename), 'r') as f:
                first_line = f.readline()
        # extract the first 14 words
        first_14_words = first_line.split()[:14]
        new_filename = '_'.join(re.findall(r'\b\w+\b', ' '.join(first_14_words))) + filename[-4:]
        # rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

print("All DONE BABY!")
