import marimo

__generated_with = "0.6.0"
app = marimo.App()


@app.cell
def __():
    import requests
    return requests,


@app.cell
def __(requests):
    url = "https://best-english-resources-api.onrender.com/resources"
    response = requests.get(url)
    return response, url


@app.cell
def __(response):
    response.headers
    return


@app.cell
def __(response):
    response.json()
    return


@app.cell
def __(response):
    top_cat = response.json()
    return top_cat,


@app.cell
def __(top_cat):
    top_cat_name_url= [(e["name"], e["url"]) for e in top_cat if e["category"] == "top"] 
    return top_cat_name_url,


@app.cell
def __(top_cat_name_url):
    top_cat_name_url
    return


@app.cell
def __(top_cat):
    CAE_cat_name_url= [(e["name"], e["url"]) for e in top_cat if e["category"] == "CAE"] 
    return CAE_cat_name_url,


@app.cell
def __(CAE_cat_name_url):
    CAE_cat_name_url
    return


if __name__ == "__main__":
    app.run()
