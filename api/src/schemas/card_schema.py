#checar restrições antes de salvar no banco de dados
import enum
from pydantic import BaseModel
from datetime import datetime

#validação
class answer_enum(str, enum.Enum):
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
class block_enum(str, enum.Enum):
    I = "I"
    II = "II"
    III = "III"

class CardBase(BaseModel):
    body: str
    image_path: str | None = None
    alternatives: str
    answer: answer_enum
    block: block_enum
    subject: str
    espec_subject: str

class CardCreate(CardBase):
    pass

class Card(CardBase):
    id: int 
    created_at: datetime
    
    class Config:
        orm_mode = True

class CardUpdate(CardBase):
    #Todos os campos são opcionais
    body: str | None = None
    image_path: str | None = None
    alternatives: str | None = None
    answer: answer_enum | None = None
    block: block_enum | None = None
    subject: str | None = None
    espec_subject: str | None = None



