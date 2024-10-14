from typing import List
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.bookings import AirbnbBooking as AirbnbBookingDBModel
from app.schemas.bookings import AirbnbBooking
from app.schemas.http import Ok200, Created201
from app.schemas.responses import Duplicated409


def get_airbnb_bookings(db_session: Session):
    bookings = jsonable_encoder((db_session.scalars(select(AirbnbBookingDBModel))).all())
    if not bookings:
        raise HTTPException(status_code=404, detail="No bookings found")
    return Ok200(records=bookings)


def post_airbnb_bookings(db_session: Session, bookings: List[AirbnbBooking]):
    booking_models = [AirbnbBookingDBModel(**booking.model_dump()) for booking in bookings]
    try:
        db_session.add_all(booking_models)
        db_session.commit()
        return Created201(message=f"{len(bookings)} records created", records=bookings)
    except IntegrityError as e:
        return Duplicated409(detail=str(e))
