from typing import Optional

from pydantic import BaseModel, Field


class ArticleSchema(BaseModel):

    Unnamed: int = Field(...)
    Country: str = Field(...)
    NoPlayers: str = Field(...)
    Players: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Unnamed": 1,
                "Country": "test_Country",
                "NoPlayers": "222",
                "Players" : "test_Players",
            }
        }


class UpdateArticleModel(BaseModel):

    Unnamed: int = Field(...)
    Country: str = Field(...)
    NoPlayers: str = Field(...)
    Players: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Unnamed": 1,
                "Country": "test_Country",
                "NoPlayers": "222",
                "Players" : "test_Players",
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}