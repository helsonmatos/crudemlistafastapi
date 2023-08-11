from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: Optional[str]
    senha: str



lista = [
    Usuario(id=1, nome='neymar', senha='senha1'),
    Usuario(id=2, nome='ronaldo', senha='senha2'),
    Usuario(id=3, nome='romario', senha='senha3'),
    Usuario(id=4, nome='rivaldo', senha='senha4'),
    Usuario(id=5, nome='kaka', senha='senha5'),
]

@app.post('/usuario')
def main(usuario: Usuario):
    lista.append(usuario)
    return usuario

@app.get('/usuarioListar')
def main():
    return lista
