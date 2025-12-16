from typing import Optional, List
from db.mongodb import get_collection
from models.setting import Setting, QuickAction
from services.crud_base import CrudBase
from bson import ObjectId
from datetime import datetime


class SettingService(CrudBase):
    model = Setting