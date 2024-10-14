from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from app.database import Base


class AirbnbBooking(Base):
    __tablename__ = f"airbnb_bookings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    host_id: Mapped[int]
    place_id: Mapped[int]
    start_date: Mapped[date]
    stays: Mapped[int]
