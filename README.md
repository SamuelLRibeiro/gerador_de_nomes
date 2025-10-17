# Gerador de Nomes de NPC

Um **gerador de nomes para NPCs (Personagens Não Jogáveis)** voltado para **mestres de RPG de mesa** que desejam criar personagens rapidamente, com nomes únicos e memoráveis.  
Feito em **Python**, este projeto combina nomes masculinos e femininos com sobrenomes aleatórios, e está sendo expandido semanalmente com novas funcionalidades.

---

## Funcionalidades Atuais

- Geração de nomes aleatórios  
- Opção de gênero: **masculino** ou **feminino**  
- Combinação de **primeiro nome + sobrenome**  
- Execução contínua até o usuário decidir parar  
- Validação de entradas do usuário (garante digitação correta)

---

## Funcionalidades em Desenvolvimento

🟡 **Histórico de nomes gerados**  
> Armazena os nomes criados e evita repetições na mesma sessão.

🟡 **Sistema de persistência (arquivo TXT/CSV)**  
> Permite salvar e carregar nomes já utilizados entre execuções.

🟡 **Consulta de nomes usados**  
> O usuário poderá verificar se um nome já foi gerado antes.

🟡 **Interface amigável no terminal (CLI)**  
> Menu interativo com atalhos para gerar, buscar e listar nomes.

🟡 **Integração futura com planilhas e apps de RPG**  
> Facilitar uso em fichas, campanhas e geradores automáticos de personagens.

---

## Como Usar

1. Certifique-se de ter o **Python 3.10+** instalado.  
2. Clone este repositório ou baixe o arquivo `script.py`.  
3. Execute no terminal:
   ```bash
   python script.py
