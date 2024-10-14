from typing import Annotated

from app.database import get_db_session
from fastapi import Depends
from sqlalchemy.orm import Session

DBSessionDep = Annotated[Session, Depends(get_db_session)]
