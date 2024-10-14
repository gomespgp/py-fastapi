from pydantic import BaseModel, Field, RootModel
from datetime import date
from typing import List


class AirbnbBooking(BaseModel):
    id: int
    host_id: int
    place_id: int
    start_date: date
    stays: int = Field(ge=1)


class AirbnbBookings(RootModel):
    root: List[AirbnbBooking]

    def items(self):
        return self.root


class BookingcomBooking(BaseModel):
    id: int
    host_id: int
    place_id: int
    start_date: date
    stays: int = Field(ge=1)


class BookingcomBookings(RootModel):
    root: List[BookingcomBooking]

    def items(self):
        return self.root
