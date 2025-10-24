import enum
from pydantic import BaseModel
from .card_schema import Card

class type_enum(str, enum.Enum):
    all = "all"
    block = "block"
    subject = "subject"
    espec_subject = "espec_subject"

class Filter(BaseModel):
    type: type_enum
    text: str | None = None
    qtd: int

class QuizCreate(BaseModel): # para criar os dados, recebe uma lista de filtro
    filters: list[Filter]

class QuizRetrieve(BaseModel): # para enviar os dados, envia uma lista de Cards
    cards: list[Card]
    class Config:
        orm_mode = True # Permite que o Pydantic leia os dados diretamente do modelo do SQLAlchemy
