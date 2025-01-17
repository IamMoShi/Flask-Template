from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from flask_app.models.CRUD import CRUD
from flask_app.extensions.database import constants


class ExampleModel(CRUD):
    __tablename__ = "example_model"
    __filename__ = "example_model.csv"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(constants["NAME_LENGTH"]), nullable=False, default="Untitled")
    description: Mapped[str] = mapped_column(String(constants["DESCRIPTION_LENGTH"]), nullable=True, default="")
