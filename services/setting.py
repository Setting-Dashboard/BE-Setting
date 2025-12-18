from bson import ObjectId
from typing import List, Dict, Any
from models.setting import Setting
from services.crud_base import CrudBase


class SettingService(CrudBase):
    model = Setting

    @classmethod
    def update(cls, updates: List[Dict[str, Any]]):
        """
        Bulk update
        Body: {
            updates = [
                {
                    "id": "<setting_id>",
                    "data": { ...update fields... }
                }
            ]
        }
        """
        col = cls._col()
        results = []

        for item in updates:
            setting_id = item.get("id")
            data = item.get("data")

            if not setting_id or not data:
                continue

            result = col.update_one(
                {"_id": ObjectId(setting_id)},
                {"$set": data}
            )

            results.append({
                "id": setting_id,
                "matched": result.matched_count,
                "modified": result.modified_count
            })

        return {
            "updated_count": len(results),
            "results": results
        }