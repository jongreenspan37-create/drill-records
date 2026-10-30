from sqlalchemy import Identity, false
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    is_admin: Mapped[bool] = mapped_column(server_default=false())


class Rank(Base):
    __tablename__ = "ranks"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
