from pydantic import BaseModel
from typing import List

class PointInTime(BaseModel):
    date: str
    name: str
    snow: float

    def __repr__(self):
        return "-date " + self.date + "-name" + self.name + "-snow" + str(self.snow) + "\n"

class Data(BaseModel):
    year: str
    yearData: List[PointInTime]

