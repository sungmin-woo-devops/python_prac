from datetime import datetime

from sqlalchemy import Column, DATETIME
from sqlalchemy.orm import declarative_mixin

@declarative_mixin
class Timestamp:
    created_at = Column(DATETIME, default=datetime.utcnow, nullable=False)
    updated_at = Column(DATETIME, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)