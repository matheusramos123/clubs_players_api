from core.configs import settings   
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship


class JogadorModel(settings.DBBaseModel):
    __tablename__ = 'jogador'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable= False)
    posicao = Column(String(45), nullable= False)

    time_id = Column(Integer, ForeignKey("times.id"), nullable=False)
    time = relationship("TimesModel",back_populates= "jogadores")

