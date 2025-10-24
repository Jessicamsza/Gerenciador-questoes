from fastapi import APIRouter
from ..schemas.card_schema import Card, CardCreate, CardUpdate
from ..schemas.quiz_schema import QuizCreate, QuizRetrieve
from datetime import datetime



router = APIRouter(
    prefix="/cards", # Todas as rotas aqui começam com /cards
    tags=["Cards"]   # Agrupa no /docs do FastAPI
)

# ======== rotas essenciais da aplicação ========

#POST para criar dados
# envia um JSON no corpo da requisição formatado de acordo com o schema CardCreate.
@router.post("/", response_model=Card)
def create_card(card: CardCreate):
    #TODO: service. save_card(card)
    # return card_saved

    #MOCK
    mock_data = card.model_dump()
    #adiciona os dados que bd faria automaticamente
    mock_data["id"] = 101 
    mock_data["created_at"] = datetime.now() 
    print(f"MOCK: Criando card com body: {mock_data['body']}")
    return mock_data

#POST para fazer uma solicitação complexa, 
#envia os parâmetros formatados via JSON, faz um processamento de multiplos passos,
#e retorna um outro objeto JSON.
@router.post("/quiz/", response_model=QuizRetrieve)
def generate_quiz(quiz_request: QuizCreate):
    # TODO:
    # 'quiz_request' é um objeto QuizCreate com a lista de filtros.
    # filters_list = quiz_request.filters (do tipo Filter em quiz_schemas.py)
    # cards_list = service.get_cards_from_filters(filters_list)
    # return {"cards": cards_list} # O Pydantic monta o QuizRetrieve

    #MOCK
    mock_card_1 = {
        "id": 901, "body": "Card de teste 1", "alternatives": "a)b)c)",
        "answer": "a", "block": "I", "subject": "Mock",
        "espec_subject": "Teste", "created_at": datetime.now()
    }
    mock_card_2 = {
        "id": 902, "body": "Card de teste 2", "alternatives": "d)e)f)",
        "answer": "e", "block": "II", "subject": "Mock",
        "espec_subject": "Teste2", "created_at": datetime.now()
    }
    print(f"MOCK: Gerando quiz com {len(quiz_request.filters)} filtros")
    # Retorna no formato do QuizRetrieve
    return {"cards": [mock_card_1, mock_card_2]}

# ======== demais rotas operacionais ========

#UPDATE, usa PATCH para atualizações parciais
@router.patch("/{card_id}", response_model=Card)
def update_card(card_id: int, data_to_uptade: CardUpdate):
    #'card_id' vem da URL
    #'card_update' é o objeto CardUpdate que veio do body JSON
    #TODO:
    #updated_card = service.update_card(original_card=db_card, update=data_to_uptade)
    #return updated_card

    #MOCK
    update_data = data_to_update.dict(exclude_unset=True) 
    print(f"MOCK: Atualizando card {card_id} com dados: {update_data}")
    # Retorna um card "atualizado" falso
    return {
        "id": card_id,
        "body": f"Card {card_id} foi atualizado",
        "alternatives": "a,b,c", "answer": "c", "block": "III",
        "subject": "Atualizado", "espec_subject": "Mock",
        "created_at": datetime.now()
    }

#DELETE para remover um card
@router.delete("/{card_id}", response_model=Card)
def delete_card(card_id: int):
    #TODO:
    # service.delete_card(id=card_id)


    print(f"MOCK: Deletando card {card_id}")
    # Retorna o card que "foi deletado"
    return {
        "id": card_id,
        "body": f"Card {card_id} foi DELETADO",
        "alternatives": "...", "answer": "a", "block": "I",
        "subject": "Deletado", "espec_subject": "Mock",
        "created_at": datetime.now()
    }

#GET, lista cards mais recentemente adicionados
@router.get("/", response_model=list[Card])
def get_all_cards():
    #TODO:
    #recent_added_cards = service.get_recent_cards()
    pass