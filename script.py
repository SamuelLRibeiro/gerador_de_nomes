import random

def jogar():
    continuar = True
    nomes_masculinos = ['Brandon', 'Hank', 'Torn']
    nomes_femininos = ['Ada', 'Solace', 'Candace']
    sobrenomes = ['Stark', 'Potter', 'Harris']
    ## função escolha de genero
    def gerar_nome(genero):
        if genero == 1:
            nome = random.choice(nomes_masculinos) + " " + random.choice(sobrenomes)
            return nome
        elif genero == 2:
            nome = random.choice(nomes_femininos) + " " + random.choice(sobrenomes)
            return nome
        else:
            return None
        
    while continuar == True:
        
        ## input do usuário para escolha de gênero com validação de resposta
        genero = int(input('Digite o gênero a ser gerado o nome: [1] Masculino [2] Feminino '))
        while genero != 1 and genero != 2:
            print('Resposta inválida ')
            genero = int(input('Digite o gênero a ser gerado o nome: [1] Masculino [2] Feminino '))
        nome_gerado = gerar_nome(genero)
        print('Nome gerado: ', nome_gerado)
        ## input do usuário se ele deseja continuar utilizando o script ou não com validação de resposta
        continuar = int(input('Você deseja continuar? [1] Sim [2] Não '))
        while continuar != 1 and continuar != 2:
            print('Resposta inválida ')
            continuar = int(input('Você deseja continuar? [1] Sim [2] Não '))
        if continuar == 2:
            continuar = False
        else: continuar = True
    return

if __name__ == "__main__":
    jogar()

    