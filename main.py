from fastapi import FastAPI

app = FastAPI(title="API da Biblioteca")

livros = [
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano": 1899,
        "categoria": "Romance"
    },
    {
        "id": 2,
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "ano": 1943,
        "categoria": "Infantil"
    },
    {
        "id": 3,
        "titulo": "1984",
        "autor": "George Orwell",
        "ano": 1949,
        "categoria": "Ficção"
    },
    {
        "id": 4,
        "titulo": "A Hora da Estrela",
        "autor": "Clarice Lispector",
        "ano": 1977,
        "categoria": "Romance"
    }
]


# Rota inicial
@app.get("/")
def inicio():
    return {
        "mensagem": "API do IFMA Campus Timon está funcionando."
    }


# Listar todos os livros
@app.get("/livros")
def listar_livros():
    return {
        "livros": livros
    }


# Buscar livro pelo ID
@app.get("/livros/{id}")
def buscar_livro(id: int):
    for livro in livros:
        if livro["id"] == id:
            return livro

    return {
        "erro": "Livro não encontrado"
    }


# Listar autores
@app.get("/autores")
def listar_autores():
    autores = sorted(
        set(livro["autor"] for livro in livros)
    )

    return {
        "autores": autores
    }


# Listar categorias
@app.get("/categorias")
def listar_categorias():
    categorias = sorted(
        set(livro["categoria"] for livro in livros)
    )

    return {
        "categorias": categorias
    }


# Buscar livros por autor
@app.get("/busca/autor/{nome}")
def buscar_por_autor(nome: str):
    resultado = [
        livro
        for livro in livros
        if nome.lower() in livro["autor"].lower()
    ]

    return {
        "livros": resultado
    }


# Buscar livros por ano
@app.get("/exercicio/ano/{ano}")
def buscar_por_ano(ano: int):
    resultado = [
        livro
        for livro in livros
        if livro["ano"] == ano
    ]

    return {
        "ano": ano,
        "livros": resultado
    }