import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.1"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.ti_data

collection = database.get_collection("TI_2016.Country Representation")


# helpers
def dota_helper(dota) -> dict:
    return {
        "_id": str(dota["_id"]),
        "Unnamed": dota["Unnamed"],
        "No. of Players": dota["No. of Players"],
        "Players": dota["Players"],
    }

# Retrieve all articles present in the database
async def retrieve_dotas():
    dotas = []
    async for dota in collection.find():
        dotas.append(dota_helper(dota))
    return dotas


# Add a new article into to the database
async def add_dota(data: dict) -> dict:
    dota = await collection.insert_one(data)
    new_dota = await collection.find_one({"_id": dota.inserted_id})
    return dota_helper(new_dota)


# Retrieve a article with a matching ID
async def retrieve_dota(id: str) -> dict:
    dota = await collection.find_one({"_id": ObjectId(id)})
    if dota:
        return dota_helper(dota)


# Update a article with a matching ID
async def update_dota(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    dota = await collection.find_one({"_id": ObjectId(id)})
    if dota:
        updated_dota = await collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_dota:
            return True
        return False


# Delete a article from the database
async def delete_dota(id: str):
    dota = await collection.find_one({"_id": ObjectId(id)})
    if dota:
        await collection.delete_one({"_id": ObjectId(id)})
        return True
    
