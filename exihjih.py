filmes = {}

for i in range(3):
    codigo = input("Código do filme: ")
    titulo = input("Título: ")
    genero = input("Gênero: ")
    duracao = int(input("Duração em minutos: "))

    filmes[codigo] = {
        "titulo": titulo,
        "genero": genero,
        "duracao": duracao
    }

print("\nFilmes com duração superior a 120 minutos:")

for codigo in filmes:
    if filmes[codigo]["duracao"] > 120:
        print("Título:", filmes[codigo]["titulo"])
        print("Gênero:", filmes[codigo]["genero"])
        print("Duração:", filmes[codigo]["duracao"], "minutos")
        print()