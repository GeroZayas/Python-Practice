import marimo

__generated_with = "0.6.0"
app = marimo.App()


@app.cell
def __():
    from sqlalchemy import create_engine, Column, Integer, String, Sequence, inspect

    return Column, Integer, Sequence, String, create_engine, inspect


@app.cell
def __():
    from sqlalchemy.orm import sessionmaker, declarative_base

    return declarative_base, sessionmaker


@app.cell
def __(create_engine):
    engine = create_engine("sqlite:///tutorial.db")
    return (engine,)


@app.cell
def __(declarative_base):
    Base = declarative_base()
    return (Base,)


@app.cell
def __(engine, sessionmaker):
    Session = sessionmaker(bind=engine)
    session = Session()
    return Session, session


@app.cell
def __(engine, inspect):
    inspector = inspect(engine)
    return (inspector,)


@app.cell
def __(inspector):
    tables = inspector.get_table_names()
    return (tables,)


@app.cell
def __(tables):
    print("Tables in the database:")
    for table_name in tables:
        print(table_name)

    return (table_name,)


@app.cell
def __():
    the_table_name = "people"
    return (the_table_name,)


@app.cell
def __(inspector, the_table_name):
    columns = inspector.get_columns(the_table_name)
    return (columns,)


@app.cell
def __(columns, the_table_name):
    print(f"Columns in table '{the_table_name}':")
    for column in columns:
        print(f"  {column['name']} ({column['type']})")
    return (column,)


if __name__ == "__main__":
    app.run()
