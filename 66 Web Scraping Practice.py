from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://elcatalacomcal.blogspot.com/2008/03/sentir-i-escoltar.html"
)
catala_com_cal_web_page = response.text

soup = BeautifulSoup(catala_com_cal_web_page, "html.parser")

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.get("class"))

articles = soup.find_all(name="span", style="color: #cc0000;")
article_texts = []
article_links = []

# print(articles)

for article in articles:
    text = article.getText()
    article_texts.append(text)

print(article_texts)
