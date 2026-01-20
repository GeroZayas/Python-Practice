import sqlite3
from pathlib import Path
from typing import AnyStr
import logging
from models.models import ItemData
from services.sql import (
    insert_statement,
    read_statement,
    create_table,
    delete_statement,
    read_item_statement,
    update_statment,
)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)


logger = logging.getLogger(__name__)

# ------------------------------------------------------------------------------
# PATHS
# ------------------------------------------------------------------------------
ROOT_DIR = Path(__file__).parent.parent

DB_PATH = ROOT_DIR / "services" / "my.db"

string = str


def add_data(idea: str, note: str):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            exec_statement = cursor.execute(
                insert_statement.format(idea_=idea, note_=note)
            )
            print("ADDED {idea} and {note}".format(idea=idea, note=note))
    except sqlite3.OperationalError as e:
        print("Failed to write to database:", e)
        return {"status": "ERROR Writing Data"}


def get_all_data():
    all_data_dict = {}
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            exec_statement = cursor.execute(read_statement)
            all_data = exec_statement.fetchall()
            for index, elem in enumerate(all_data, 1):
                print("IDEA:", elem[1], "NOTE:", elem[2])
                all_data_dict[index] = {
                    "id": elem[0],
                    "idea": elem[1],
                    "note": elem[2],
                }
            return all_data_dict

    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
        return {"status": "ERROR Fetching Data"}

def get_item_data(id: int):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            exec_statement = cursor.execute(read_item_statement.format(id=id))
            logger.info("Calling `results`")
            results = exec_statement.fetchall()
            logger.debug(f"RESULTS: {results}")
            id, idea, notes, _ = results[0]
            item_data = ItemData(id=id, idea=idea, notes=notes)
            return item_data

    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
        return {"status": "ERROR Fetching Data"}


def update_item_data(id: int, idea: str, note: str):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            exec_statement = cursor.execute(
                update_statment.format(id=id, idea_=idea, note_=note)
            )
            conn.commit()

            print("UPDATED {idea} and {note}".format(idea=idea, note=note))
    except sqlite3.OperationalError as e:
        print("Failed to write to database:", e)
        return {"status": "ERROR Writing Data"}


all_data_dict = get_all_data()
