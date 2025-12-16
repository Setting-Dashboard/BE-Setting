from bson import ObjectId
from typing import Type, Optional, Dict, Any


class CrudBase:
    model: Type  # BaseModel (ex: Setting)

    @classmethod
    def _col(cls):
        return cls.model.get_collection()

    @classmethod
    def create(cls, data) -> str:
        result = cls._col().insert_one(data.dict())
        return str(result.inserted_id)

    @classmethod
    def get(cls, doc_id: str):
        doc = cls._col().find_one({"_id": ObjectId(doc_id)})
        return cls.model(**doc) if doc else None

    @classmethod
    def list(cls, filters: Optional[Dict[str, Any]] = None):
        filters = filters or {}
        docs = cls._col().find(filters)

        results = []
        for doc in docs:
            doc["_id"] = str(doc["_id"])  # 🔥 핵심
            results.append(cls.model(**doc))

        return results

    @classmethod
    def update(cls, doc_id: str, data: Dict[str, Any]) -> bool:
        result = cls._col().update_one(
            {"_id": ObjectId(doc_id)},
            {"$set": data}
        )
        return result.modified_count > 0

    @classmethod
    def delete(cls, doc_id: str) -> bool:
        result = cls._col().delete_one({"_id": ObjectId(doc_id)})
        return result.deleted_count > 0
