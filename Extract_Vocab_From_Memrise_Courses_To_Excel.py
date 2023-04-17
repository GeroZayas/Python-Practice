def extract_vocab(link):
    """Extracts two lists of vocabulary (1st column Language 1, 2nd column Language 2) from a valid link to a Memrise Course.
    Creates folder to save the corresponding ** EXCEL **  files from the lists of vocabulary.
    """

    from bs4 import BeautifulSoup
    import requests
    import csv
    import os

    # ----------------------
    # TO CREATE EXCEL FILE:
    import xlsxwriter

    # ----------------------

    WEB = link

    # ******* GET Number of Levels ********
    # Getting the response from the website.
    response = requests.get(f"{WEB}")

    # Getting the text from the response.
    data = response.text

    # Parsing the data from the website.
    soup = BeautifulSoup(data, "html.parser")

    # Finding all the divs with the class level-index.
    level_number = soup.find_all(name="div", attrs={"class": "level-index"})

    level_number_list = [level.getText() for level in level_number]
    LEVELS = int(level_number_list[-1])

    CURRENT_PATH = os.getcwd()

    print(CURRENT_PATH)

    progress_bar = "*"
    col = 0

    # A progress bar.
    for counter_level, _ in enumerate(range(LEVELS), start=1):
        # ***** Progress Bar *****

        os.system("cls")
        extract_vocab.percentage = (counter_level / LEVELS) * 100
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

        # Finding all the divs with the class col_a col text and col_b col text.
        first_language = soup.find_all(name="div", attrs={"class": "col_a col text"})
        second_language = soup.find_all(name="div", attrs={"class": "col_b col text"})

        first_language_list = [word.get_text() for word in first_language]
        second_language_list = [word.get_text() for word in second_language]
        # print(len(second_language_list))

        # how to put two lists into a dictionary
        words_dict = dict(zip(first_language_list, second_language_list))

        # Replacing the "/" and ":" characters in the course name with "-" because the "/" and ":" characters
        # are not allowed in file names.
        course_name_string = course_name.get_text().strip()
        if "/" in course_name_string:
            course_name_string = course_name_string.replace("/", "-")
        elif ":" in course_name_string:
            course_name_string = course_name_string.replace(":", "-")

        # Checking if the folder with the course name exists. If it doesn't exist, it creates it.
        if not os.path.exists(f"{CURRENT_PATH}\{course_name_string}"):
            os.makedirs(f"{course_name_string}")

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(
            f"{course_name_string}/{course_name_string}_{counter_level}.xlsx"
        )
        worksheet = workbook.add_worksheet()

        # Iterate over the data and write it out row by row.
        for row, (item, cost) in enumerate(words_dict.items()):
            worksheet.write(row, col, item)
            worksheet.write(row, col + 1, cost)
        workbook.close()

    print("DONE")


if __name__ == "__main__":
    link = input("Insert Valid Memrise Course Link: ")

    extract_vocab(link=link)
