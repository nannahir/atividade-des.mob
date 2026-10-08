from fastapi import FastAPI

app = FastAPI(title="API do IFMA Campus Timon")

# Questão 9 :
alunos = [
    {"id": 101, "nome": "Mateus Henrique Lima", "curso": "Sistemas para Internet", "turno": "Matutino", "situacao_academica": "Matriculado"},
    {"id": 102, "nome": "Fernanda Ribeiro", "curso": "Informática", "turno": "Vespertino", "situacao_academica": "Matriculado"},
    {"id": 103, "nome": "Carlos Eduardo Rocha", "curso": "Administração", "turno": "Noturno", "situacao_academica": "Matriculado"},
    {"id": 104, "nome": "Juliana Martins", "curso": "Sistemas para Internet", "turno": "Matutino", "situacao_academica": "Trancado"},
    {"id": 105, "nome": "Rafael Barbosa", "curso": "Eletromecânica", "turno": "Vespertino", "situacao_academica": "Concluído"},
    {"id": 106, "nome": "Camila Araujo", "curso": "Edificações", "turno": "Matutino", "situacao_academica": "Matriculado"}
]

# Questão 8:
@app.get("/")
def inicio():
    return {"mensagem": "API do IFMA Campus Timon está funcionando perfeitamente!"}

# Questão 9:
@app.get("/alunos")
def listar_alunos():
    return alunos

# Questão 10:
@app.get("/resumo")
def obter_resumo():
    cursos_unicos = list(set(aluno["curso"] for aluno in alunos))
    turnos_unicos = list(set(aluno["turno"] for aluno in alunos))
    
    return {
        "total_alunos": len(alunos),
        "quantidade_cursos": len(cursos_unicos),
        "turnos_disponiveis": turnos_unicos
    }