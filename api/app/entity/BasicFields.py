from sqlalchemy import Column  , String  , Boolean , DateTime
from sqlalchemy.orm import Base 

class BasicFields(Base):  
    __abstract__ = True  # To prevent a table from being created for BasicFields  
    id = Column(String, primary_key=True, index=True,nullable=False),
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)