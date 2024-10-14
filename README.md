# py-fastapi
This is just a simple Python and FastAPI API.

This is, at first, heavily inspired in [this](https://github.com/ThomasAitken/demo-fastapi-async-sqlalchemy) code.

The codebase is split into domains. In each domain has a file for each component in this API.

# How to add endpoint
For this tutorial, take as example the `bookings` domain.
In order to add one endpoint(s), it is required to add/create the following components:
1. [Schema](#schema)
2. [Model](#model)
3. [Route/Endpoint](#routeendpoint)
4. [Operation](#operation)

Here is a [PR](https://github.com/gomespgp/py-fastapi/pull/4) that adds new endpoints. Take it as example.

## Schema
Schemas are responsible for defining and validating Input and Output of the API.

Schemas are located in [/py-fastapi/server/app/schemas](/server/app/schemas).

Add a new Python file with the name of the domain (e.g `bookings.py`) and add the schema(s).

example:
```python
class AirbnbBooking(BaseModel):
    id: int
    host_id: int
    place_id: int
    start_date: date
    stays: int = Field(ge=1)
```

## Model
Models are representation of the database tables.

Models are located in [/py-fastapi/server/app/models](/server/app/models).

Add a new Python file with the name of the domain (e.g `bookings.py`) and add the model(s).

example:
```python
class AirbnbBooking(Base):
    __tablename__ = f"airbnb_bookings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    host_id: Mapped[int]
    place_id: Mapped[int]
    start_date: Mapped[date]
    stays: Mapped[int]
```

## Route/Endpoint
The routers/endpoints is where we define logic table will be applied to each endpoint.

Routers are located in [/py-fastapi/server/app/api/routers](/server/app/api/routers).

Add a new Python file with the name of the domain (e.g `bookings.py`) and add the endpoint(s).

example:
```python
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
```

## Operation
Operations are the functions where business logic applied to routers/endpoint is defined.

Operations are located in [/py-fastapi/server/app/operations](/server/app/operations).

Add a new Python file with the name of the domain (e.g `bookings.py`) and add the operation(s).

example:
```python
def get_airbnb_bookings(db_session: Session):
    bookings = jsonable_encoder((db_session.scalars(select(AirbnbBookingDBModel))).all())
    if not bookings:
        raise HTTPException(status_code=404, detail="No bookings found")
    return Ok200(records=bookings)
```

# TODO
* Add alembic to manage database migrations
* Add Oauth2 authentication
