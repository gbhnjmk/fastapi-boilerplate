from typing import Any
from bson.objectid import ObjectId
from pymongo.database import Database
from pymongo.results import DeleteResult, UpdateResult


# from ..utils.security import hash_password


class ShanyraqRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyraq(self, user_id: str, data: dict[str, Any]):
        data["user_id"] = ObjectId(user_id)
        shanyraq = self.database["shanyraq"].insert_one(data)
        return shanyraq.inserted_id

    def get_shanyraq(self, shanyraq_id: str):
        return self.database["shanyraq"].find_one({"_id": ObjectId(shanyraq_id)})

    def update_shanyraq(
            self, shanyraq_id: str, user_id: str, data: dict[str, Any]) -> UpdateResult:
        return self.database["shanyraq"].update_one(
            filter={"_id": ObjectId(shanyraq_id), "user_id": ObjectId(user_id)},
            update={
                "$set": data,
            },
        )

    def delete_shanyraq(self, shanyraq_id: str, user_id: str) -> DeleteResult:
        return self.database["shanyraq"].delete_one(
            {"_id": ObjectId(shanyraq_id), "user_id": ObjectId(user_id)}
        )