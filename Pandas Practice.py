import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    import pandas as pd
    return pd,


@app.cell
def __(pd):
    df_facturas_sept = pd.read_csv("Gastos y Facturas Casa Maca & Tigre 2024 - SEPTIEMBRE 2024.csv")
    return df_facturas_sept,


@app.cell
def __(df_facturas_sept):
    df_facturas_sept
    return


@app.cell
def __(df_facturas_sept):
    clean_df_facturas_sept = df_facturas_sept.drop(["Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 7", "Total", "Nota", "Unnamed: 9", "Unnamed: 10"], axis=1)
    return clean_df_facturas_sept,


@app.cell
def __(clean_df_facturas_sept):
    clean_df_facturas_sept
    return


@app.cell
def __(clean_df_facturas_sept):
    df = clean_df_facturas_sept
    return df,


@app.cell
def __(df):
    df
    return


@app.cell
def __(df):
    columns = df.columns
    return columns,


@app.cell
def __(columns):
    columns
    return


@app.cell
def __(df):
    unique_values = list()
    for column in df.columns:
        unique_values.append(f"{column} " + f"{df[column].unique()}")
    return column, unique_values


@app.cell
def __(unique_values):
    unique_values
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
