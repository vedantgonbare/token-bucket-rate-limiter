from sqlalchemy import Column, String, Integer, Numeric, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    client_key = Column(String(255), unique=True, nullable=False, index=True)
    algorithm = Column(String(20), nullable=False, default="token_bucket")
    rate_per_second = Column(Numeric(10, 2), nullable=False)
    burst_size = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )