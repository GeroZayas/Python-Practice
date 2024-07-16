import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __():
    import requests
    from bs4 import BeautifulSoup
    return BeautifulSoup, requests


@app.cell
def __():
    url = "https://jamesclear.com/3-2-1/august-29-2019"
    return url,


@app.cell
def __(requests, url):
    response_1 = requests.get(url)
    return response_1,


@app.cell
def __(BeautifulSoup, response_1):
    soup_1 = BeautifulSoup(response_1.text, 'html.parser')
    return soup_1,


@app.cell
def __(soup_1):
    paragraphs = soup_1.find_all('p')
    for p in paragraphs:
        print(p.text)
    return p, paragraphs


@app.cell
def __(BeautifulSoup, requests):
    # URL de la página central del blog
    central_page_url = 'https://jamesclear.com/3-2-1/'

    response = requests.get(central_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encuentra todos los enlaces a los artículos
    article_links = [a['href'] for a in soup.find_all('a', href=True) if 'https://jamesclear.com/3-2-1' in a['href']]
    return article_links, central_page_url, response, soup


@app.cell
def __():
    # for article_url in article_links:
    #     response_article = requests.get(article_url)
    #     soup_article = BeautifulSoup(response_article.text, 'html.parser')

    #     paragraphs = soup_article.find_all('p')
    #     for p in paragraphs:
    #         print(p.text.strip())

    #     # Buscar la sección "1 QUESTION FOR YOU"
    #     start_section = soup.find('h2', string='1 QUESTION FOR YOU')

    #     if start_section:
    #         # Buscar hacia adelante desde la sección "1 QUESTION FOR YOU" hasta encontrar "Until next week,"
    #         end_section = start_section.find_next_sibling('h2', string='Until next week,')

    #         if end_section:
    #             # Extraer todo el contenido desde la sección "1 QUESTION FOR YOU" hasta "Until next week,"
    #             content_between_sections = start_section.find_next_sibling().decompose()

    #             # Ahora, content_between_sections contiene todo el contenido entre ambas secciones
    #             # Puedes procesar este contenido como necesites
    #             print(content_between_sections.text.strip())
    return


@app.cell
def __():
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
