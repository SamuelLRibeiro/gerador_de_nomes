import random

nomes_masculinos = ['Brandon', 'Hank', 'Torn']
nomes_femininos = ['Ada', 'Solace', 'Candace']
sobrenomes = ['Stark', 'Potter', 'Harris']

def gerar_nome(genero):
    if genero == "masculino":
        nome = random.choice(nomes_masculinos) + " " + random.choice(sobrenomes)
        return nome
    elif genero == "feminino":
        nome = random.choice(nomes_femininos) + " " + random.choice(sobrenomes)
        return nome
    else:
        return None

genero = input('Digite o gênero a ser gerado o nome: ').strip().lower()
nome_gerado = gerar_nome(genero)
print('Nome gerado: ', nome_gerado)