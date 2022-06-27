from pydantic import BaseModel
from typing import Optional


class PropertiesRequestModel(BaseModel):
    city: Optional[str] = None
    year: Optional[str] = None

