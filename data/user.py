import dataclasses


@dataclasses.dataclass
class User:
    LOGIN: str
    PASSWORD: str
    WEB_URL: str


user = User(LOGIN="hw_18@python.ru", PASSWORD="12344321",
            WEB_URL="https://demowebshop.tricentis.com/",
            )
