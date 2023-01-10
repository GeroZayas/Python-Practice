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
    response = requests.get(f"{WEB}")

    data = response.text

    soup = BeautifulSoup(data, "html.parser")

    level_number = soup.find_all(name="div", attrs={"class": "level-index"})

    level_number_list = []

    for level in level_number:
        level_number_list.append(level.getText())

    LEVELS = int(level_number_list[-1])

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

        first_language = soup.find_all(name="div", attrs={"class": "col_a col text"})
        second_language = soup.find_all(name="div", attrs={"class": "col_b col text"})

        first_language_list = []
        second_language_list = []

        for word in first_language:
            first_language_list.append(word.get_text())

        for word in second_language:
            second_language_list.append(word.get_text())

        # print(len(second_language_list))

        # how to put two lists into a dictionary
        words_dict = dict(zip(first_language_list, second_language_list))

        course_name_string = course_name.get_text().strip()
        if "/" in course_name_string:
            course_name_string = course_name_string.replace("/", "-")
        elif ":" in course_name_string:
            course_name_string = course_name_string.replace(":", "-")

        if not os.path.exists(CURRENT_PATH + f"\{course_name_string}"):
            os.makedirs(f"{course_name_string}")

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(
            f"{course_name_string}/{course_name_string}_{counter_level}.xlsx"
        )
        worksheet = workbook.add_worksheet()

        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0

        # Iterate over the data and write it out row by row.
        for item, cost in words_dict.items():
            worksheet.write(row, col, item)
            worksheet.write(row, col + 1, cost)
            row += 1

        workbook.close()

    print("DONE")


if __name__ == "__main__":
    link = input("Insert Valid Memrise Course Link: ")

    extract_vocab(link=link)
