from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from datetime import date


app = FastAPI()


class Todo(BaseModel):
    
    tarefa: str
    realizada: bool
    prazo: Optional[date]


lista = []
    

@app.post("/inserir")
def inserir(todo: Todo):
    try:
        lista.append(todo)
        return {'msg':'Cadastro feito com Sucesso'}
    except:
        return {'msg':'Erro'}


@app.post("/listar")
def listar(opcao: int = 0):
    if opcao == 0:
        return lista
    elif opcao == 1:
        return list(filter(lambda x:x.realizada == False, lista))
    elif opcao == 2:
        return list(filter(lambda x:x.realizada == True, lista))


@app.post("/listar/{id}")
def listar(id: int):
    try:
        return lista[id]
    except:
        return {'erro':'não existe'}


@app.post("/alterarStatus/{id}")
def alterarStatus(id: int):
    try:
        lista[id].realizada = not lista[id].realizada
        return lista[id]
    except:
        return {'erro':'não deu'}

@app.post("/excluir")
def excluir(id: int):
    try:
        del lista[id]
        return {'msg':'sucesso'}
    except:
        return {'msg':'erro'}
        



        
