from datetime import date

def obter_informacoes_validas():
    """Obtém do usuário nome e ano de nascimento válidos."""

    while True:
        nome = input("Digite seu nome completo: ")
        if not nome:
            print("Nome inválido. Por favor, digite seu nome completo.")
            continue

        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return nome, ano_nascimento
            else:
                print("Ano de nascimento fora do intervalo permitido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o ano de nascimento.")

def calcular_idade(ano_nascimento):
    """Calcula a idade com base no ano de nascimento e no ano atual."""
    ano_atual = date.today().year
    return ano_atual - ano_nascimento

if __name__ == "__main__":
    nome, ano_nascimento = obter_informacoes_validas()
    idade = calcular_idade(ano_nascimento)

    print(f"\n{nome}, você completou ou completará {idade} anos em 2024.")
