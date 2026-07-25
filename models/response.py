from pydantic import BaseModel

class TripResponse(BaseModel):
    destination: str
    hotel: str
    estimated_cost: float
    itinerary: list[str]