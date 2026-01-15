from fastapi import FastAPI, status, HTTPException
from scalar_fastapi import get_scalar_api_reference
from services.db import all_data_dict, add_data, get_item_data

app = FastAPI(title="App ALBERO")

@app.get("/home")
@app.get("/", status_code=status.HTTP_200_OK)
async def home():
    return {"message": "hello world"} 


@app.get("/database", status_code=status.HTTP_200_OK)
async def get_data():
    try:
        return {"ideas": all_data_dict} 
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bad Request")


@app.get("/database/item", status_code=status.HTTP_200_OK)
async def get_an_item_data(id:int):
    try:
        data = get_item_data(id)
        return {"data": data}
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bad Request")

@app.post("/database", status_code=status.HTTP_200_OK)
async def add_idea_to_database(idea: str, note: str):
    try:
        add_data(idea=idea, note=note)
        return {"status": "SUCCESS"}
    except Exception as e:
        return {"status": "ERROR: {e}".format(e=e)}

@app.put("/database", status_code=status.HTTP_200_OK)
async def update_idea_in_database(idea: str, note: str):
    try:
        add_data(idea=idea, note=note)
        return {"status": "SUCCESS"}
    except Exception as e:
        return {"status": "ERROR: {e}".format(e=e)}

# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )