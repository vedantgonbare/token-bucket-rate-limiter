from pydantic import BaseModel, Field, ConfigDict
from typing import Literal
from uuid import UUID
from datetime import datetime
from decimal import Decimal


class ClientCreate(BaseModel):
    client_key: str = Field(..., min_length=1, max_length=255)
    algorithm: Literal["token_bucket", "sliding_window"] = "token_bucket"
    rate_per_second: Decimal = Field(..., gt=0)
    burst_size: int = Field(..., gt=0)


class ClientUpdate(BaseModel):
    algorithm: Literal["token_bucket", "sliding_window"] | None = None
    rate_per_second: Decimal | None = Field(None, gt=0)
    burst_size: int | None = Field(None, gt=0)


class ClientResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    client_key: str
    algorithm: str
    rate_per_second: Decimal
    burst_size: int
    created_at: datetime
    updated_at: datetime