def extract_vocab(link):
    """Extracts two lists of vocabulary (1st column Language 1, 2nd column Language 2) from a valid link to a Memrise Course.
    Creates folder to save the corresponding txt files from the lists of vocabulary.

    Args:
        link (str): a valid link from a Memrise course
    """

    from bs4 import BeautifulSoup
    import requests
    import csv
    import os

    # https://app.memrise.com/course/57117/angles-intermig/ -> EXAMPLE

    # WEB = input("Insert valid Memrise Course link: ")
    WEB = link

    # LEVELS = int(input("Insert number of levels: ")) -> not necessary anymore

    # ******* GET Number of Levels ********
    response = requests.get(f"{WEB}")

    data = response.text

    soup = BeautifulSoup(data, "html.parser")

    level_number = soup.find_all(name="div", attrs={"class": "level-index"})

    level_number_list = []

    for level in level_number:
        level_number_list.append(level.getText())

    LEVELS = int(level_number_list[-1])

    # print(LEVELS)

    # ********* END -> GET Number of Levels ******************

    counter_level = 0

    CURRENT_PATH = os.getcwd()

    print(CURRENT_PATH)

    for time in range(LEVELS):

        counter_level += 1

        # ***** Progress Bar *****

        os.system("cls")
        extract_vocab.percentage = (counter_level / LEVELS) * 100
        progress_bar = "*"
        print(
            progress_bar * counter_level
            + " " * (LEVELS - counter_level)
            + f" {extract_vocab.percentage:.1f}%"
        )

        # ***** END Progress Bar *****

        response = requests.get(f"{WEB}{counter_level}/")

        words = response.text

        soup = BeautifulSoup(words, "html.parser")

        course_name = soup.find(name="h1", attrs={"class": "course-name"})

        catalan_words = soup.find_all(name="div", attrs={"class": "col_a col text"})
        english_words = soup.find_all(name="div", attrs={"class": "col_b col text"})

        catalan_words_list = []
        english_words_list = []

        for cat in catalan_words:
            # print(cat.get_text())
            catalan_words_list.append(cat.get_text())

        # print(catalan_words_list)

        for eng in english_words:
            # print(eng.get_text())
            english_words_list.append(eng.get_text())

        print(len(english_words_list))

        # how to put two lists into a dictionary
        words_dict = dict(zip(catalan_words_list, english_words_list))

        # print(words_dict)

        course_name_string = course_name.get_text().strip()
        if "/" in course_name_string:
            course_name_string = course_name_string.replace("/", "-")
        # level_string = level.get_text().strip()

        if not os.path.exists(CURRENT_PATH + f"\{course_name_string}"):
            os.makedirs(f"{course_name_string}")

        with open(
            f"{course_name_string}/{course_name_string}_{counter_level}.txt",
            "w",
            encoding="utf-8",
        ) as file:
            file.write("Course: " + course_name_string + "\n\n")
            file.write("Level: " + str(counter_level) + "\n\n")
            for cat in words_dict:
                file.write(f"{cat}\n")
            file.write("****" * 10 + "\n")
            for eng in words_dict.values():
                file.write(f"{eng}\n")

    print("DONE")


if __name__ == "__main__":
    extract_vocab()
