from enum import Enum


class RequestType(Enum):
    network_access = "нет доступа к сети"
    phone_working = "не работает телефон"
    emails_coming = "не приходят письма"
