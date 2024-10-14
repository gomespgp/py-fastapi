from fastapi import Response

from app.api.dependencies.core import DBSessionDep
from app.operations.bookings import get_airbnb_bookings, post_airbnb_bookings
from app.schemas.bookings import AirbnbBookings
from app.schemas.http import Ok200, Created201
from app.schemas.responses import BaseError
from fastapi import APIRouter


router = APIRouter(
    prefix="/bookings",
    tags=["bookings"],
    responses={404: {"description": "Not found"}},
)


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
    response_model=Created201 | BaseError,
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
