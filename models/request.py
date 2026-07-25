from pydantic import BaseModel, Field

class TripRequest(BaseModel):
    destination: str = Field(description="Travel destination")
    days: int = Field(gt=0, le=30)
    budget: float = Field(gt=0)
    travel_style: str = Field(default="Balanced")