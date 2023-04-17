# GOAL user inserts a word ->
# the program a) goes to wordreference.com catalan dictionary
# b) scrapes the info about the word
# c) creates a file with the info

# TODO -> use TYPER for CLI implementation

from bs4 import BeautifulSoup
import requests


def lookup_word_save_txt_file(word=None):
    """This functions receives an optional argument 'word'\n
    It looks up on www.wordreference.com Catalan dictionary the input word\n
    It adds the found definition to a txt file

    word: str

    """
    if word is None:
        # The User Inserts a word here

        print("Insert Catalan Word:\n")

        WORD = input()
    else:
        WORD = word

    response = requests.get(f"https://www.wordreference.com/definicio/{WORD}")

    # response = requests.get(f"https://www.wordreference.com/definicio/amor")

    word_definition = response.text
    soup = BeautifulSoup(word_definition, "html.parser")
    # print(soup.prettify)

    # word_definition = soup.find_all(name="div", attrs={"class": "entryLa trans clickable"})

    word_not_found = soup.find(name="div", attrs={"id": "noTransFound"})

    if word_not_found:
        print(f"Word -> '{WORD}' -> Not Found in Dictionary")
        return None

    words = soup.find_all("span", class_="lemmaLa main")
    word_list = []

    for word in words:
        word_list.append(word.text)

    # print("This is the word list->", word_list)

    word_definition = soup.find_all("ol", class_="olLa")

    word_definition_list = []

    for text in word_definition:
        word_definition_list.append(str(text.text.split(".")).strip("[]"))

    # for line in word_definition_list:
    #     print(line)

    with open("Looked Up Catalan words.txt", "a") as def_file:
        for word in word_list:
            def_file.write("***" + str(word).upper() + "***" + "\n")
        for line in word_definition_list:
            def_file.write(str(line) + "\n")
        def_file.write("-" * 70 + "\n\n")

    print("-- Done -- ")
    print("-- Word added to txt file -- ")


if __name__ == "__main__":
    lookup_word_save_txt_file()
