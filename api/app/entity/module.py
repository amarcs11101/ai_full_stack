from sqlalchemy import Column  , String 
from entity.BasicFields import BasicFields

class Module(BasicFields):
    __tablename__ ="module", 
    name= Column(String , nullable=False),
    description = Column(String, nullable=True) 