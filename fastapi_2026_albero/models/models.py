from pydantic import BaseModel, Field


class ItemData(BaseModel):
    id: int = Field(description="The id of the item in the database")
    idea: str = Field(description="The main idea")
    notes: str = Field(description="Some notes about the idea")
