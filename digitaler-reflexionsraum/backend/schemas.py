from pydantic import BaseModel


class FutureMessageSchema(BaseModel):
    message: str
    date: str


class GrowthEntrySchema(BaseModel):
    date: str
    progress: int
