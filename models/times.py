from core.configs import settings
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class TimesModel(settings.DBBaseModel):
    __tablename__ = 'times'

    id = Column(Integer, primary_key=True, autoincrement= True)
    nome = Column(String(45),nullable= False)

    jogadores = relationship("JogadorModel",back_populates="time")

