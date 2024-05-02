from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_dota,
    delete_dota,
    retrieve_dota,
    retrieve_dotas,
    update_dota,
)
from apimongo.server.models.dota import (
    ErrorResponseModel,
    ResponseModel,
    ArticleSchema,
    UpdateArticleModel,
)

router = APIRouter()

@router.post("/", response_description="Article data added into the database")
async def add_dota_data(dota: ArticleSchema = Body(...)):
    dota = jsonable_encoder(dota)
    new_dota = await add_dota(dota)
    return ResponseModel(new_dota, "Article added successfully.")


@router.get("/", response_description="Dotas retrieved")
async def get_dotas():
    dotas = await retrieve_dotas()
    if dotas:
        return ResponseModel(dotas, "Articles data retrieved successfully")
    return ResponseModel(dotas, "Empty list returned")


@router.get("/{id}", response_description="Article data retrieved")
async def get_dota_data(id):
    article = await retrieve_dota(id)
    if article:
        return ResponseModel(article, "Article data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Article doesn't exist.")

@router.put("/{id}")
async def update_dota_data(id: str, req: UpdateArticleModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_dota = await update_dota(id, req)
    if updated_dota:
        return ResponseModel(
            "dota with ID: {} name update is successful".format(id),
            "dota name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the dota data.",
    )

@router.delete("/{id}", response_description="dota data deleted from the database")
async def delete_dota_data(id: str):
    deleted_dota = await delete_dota(id)
    if deleted_dota:
        return ResponseModel(
            "Article with ID: {} removed".format(id), "Article deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Article with id {0} doesn't exist".format(id)
    )