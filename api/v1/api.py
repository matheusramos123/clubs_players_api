from fastapi import APIRouter
from api.v1.endpoints import times
from api.v1.endpoints import jogador

api_router = APIRouter()

api_router.include_router(times.router,tags=['times'])

api_router.include_router(jogador.router,tags= ['jogadores'])
