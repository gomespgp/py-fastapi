from fastapi import APIRouter, Response
from typing import Union

from app.api.dependencies.core import DBSessionDep
from app.operations.bookings import (
    get_airbnb_bookings,
    post_airbnb_bookings,
    get_bookingcom_bookings,
    post_bookingcom_bookings
)
from app.schemas.bookings import AirbnbBookings, BookingcomBookings
from app.schemas.http import Ok200, Created201
from app.schemas.responses import BaseError


router = APIRouter(
    prefix="/bookings",
    tags=["bookings"],
    responses={404: {"description": "Not found"}},
)


# Airbnb Bookings
@router.get(
    path="/airbnb",
    response_model=Ok200,
)
def airbnb_bookings(
    db_session: DBSessionDep,
    response: Response,
):
    """
    Get all Airbnb bookings
    """
    result = get_airbnb_bookings(db_session)
    response.status_code = result.status

    return result


@router.post(
    path="/airbnb",
    response_model=Union[Created201, BaseError],
)
def airbnb_bookings(
    db_session: DBSessionDep,
    bookings: AirbnbBookings,
    response: Response,
):
    """
    Create Airbnb bookings
    """
    bookings = bookings.items()
    result = post_airbnb_bookings(db_session, bookings)
    response.status_code = result.status

    return result

# Booking.com Bookings
@router.get(
    path="/bookingcom",
    response_model=Ok200,
)
def bookingcom_bookings(
    db_session: DBSessionDep,
    response: Response,
):
    """
    Get all Booking.com bookings
    """
    result = get_bookingcom_bookings(db_session)
    response.status_code = result.status

    return result


@router.post(
    path="/bookingcom",
    response_model=Union[Created201, BaseError],
)
def bookingcom_bookings(
    db_session: DBSessionDep,
    bookings: BookingcomBookings,
    response: Response,
):
    """
    Create Booking.com bookings
    """
    bookings = bookings.items()
    result = post_bookingcom_bookings(db_session, bookings)
    response.status_code = result.status

    return result
