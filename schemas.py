from typing import List, Annotated
from datetime import datetime

from pydantic import BaseModel, EmailStr, StringConstraints

from requests_enum import RequestType

NameType = Annotated[str, StringConstraints(min_length=2, max_length=50, pattern=r"^[A-Za-zА-Яа-яЁё\s-]+$")]
PhoneType = Annotated[str, StringConstraints(pattern=r"^\+?\d{1,15}$")]


class Report(BaseModel):
    first_name: NameType
    last_name: NameType
    birth_day: datetime
    phone: PhoneType
    email: EmailStr
    date_error_occurred: datetime
    request_reason: List[RequestType]
