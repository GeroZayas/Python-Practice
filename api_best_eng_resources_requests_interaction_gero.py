import marimo

__generated_with = "0.6.19"
app = marimo.App()


@app.cell
def __():
    import requests

    return (requests,)


@app.cell
def __(requests):
    url_top_resources = "https://api-english-resources.up.railway.app/resources/top"
    response = requests.get(url_top_resources)
    return response, url_top_resources


@app.cell
def __(response):
    response.headers
    return


@app.cell
def __(response):
    response
    return


@app.cell
def __(response):
    json_top_resources = response.json()
    return (json_top_resources,)


@app.cell
def __(json_top_resources):
    json_top_resources
    return


@app.cell
def __(json_top_resources):
    type(json_top_resources)
    return


@app.cell
def __(json_top_resources):
    len(json_top_resources)
    return


@app.cell
def __(json_top_resources):
    for _ in json_top_resources:
        print(_)
    return


@app.cell
def __(json_top_resources):
    len(json_top_resources[0])
    return


@app.cell
def __(json_top_resources):
    for _ in json_top_resources[0]:
        print(_)
    return


@app.cell
def __(json_top_resources):
    type(json_top_resources[0])
    return


@app.cell
def __(json_top_resources):
    for key, value in json_top_resources[0].items():
        print(f"{key:15}", "->", f"{value}")
    return key, value


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
