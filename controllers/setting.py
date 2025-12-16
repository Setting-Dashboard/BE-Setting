from fastapi import APIRouter, HTTPException
from typing import List
from services.setting import SettingService
from models.setting import Setting

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.post("/", summary="Create setting")
def create_setting(payload: Setting):
    try:
        setting_id = SettingService.create(payload)
        return {"id": setting_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{setting_id}", summary="Get setting by id")
def get_setting(setting_id: str):
    setting = SettingService.get(setting_id)
    if not setting:
        raise HTTPException(status_code=404, detail="Setting not found")
    return setting


@router.get("/", summary="List settings")
def list_settings():
    return SettingService.list()


@router.delete("/{setting_id}", summary="Delete setting")
def delete_setting(setting_id: str):
    success = SettingService.delete(setting_id)
    if not success:
        raise HTTPException(status_code=404, detail="Setting not found")
    return {"message": "deleted"}
