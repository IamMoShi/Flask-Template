from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


# pylint: disable=too-few-public-methods
class TimestampMixin:
    """
    Cette classe doit être utilisée par les modèles
    de données lorsqu'un suivi par date de modification
    veut être fait.

    L'héritage à cette classe ajoute une ensemble de
    colonne pour permettre le suivi des modifications
    des objets dans le temps.
    """

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
