def get_RTVE_news_to_txt_file():
    from bs4 import BeautifulSoup
    import requests

    response = requests.get("https://www.rtve.es/noticias/")
    noticias_rtve = response.text

    soup = BeautifulSoup(noticias_rtve, "html.parser")

    maintitle = soup.find_all(name="span", attrs={"class": "maintitle"})

    # for title in maintitle:
    #     if "Telediario" in title.text:
    #         break
    #     print(title.text + "\n\n")

    with open("news_scraped/news_from_rtve.txt", "w") as file:
        for title in maintitle:
            # This IF takes care of the problem of having the same line repeated on the txt file
            if "Telediario" in title.text:
                break
            file.write(title.get_text() + "\n\n")

    print("DONE")


if __name__ == "__main__":
    get_RTVE_news_to_txt_file()
