import os

# Classe com funções financeiras
class CalculadoraFinanceira:

    # Juros Compostos
    @staticmethod
    def calcular_juros_compostos(capital, taxa, tempo):
        montante = capital * (1 + taxa) ** tempo  # Fórmula 
        return montante

    # Juros Simples
    @staticmethod
    def calcular_juros_simples(capital, taxa):
        juros = capital * taxa  # Fórmula 
        return juros

    # Desconto de um produto
    @staticmethod
    def calcular_desconto(valor, porcentagem):
        desconto = valor * (porcentagem / 100)  # Fórmula 
        return desconto

    # Valor retido do INSS baseado no salário
    @staticmethod
    def calcular_inss(salario):
        # O valor do salário define a alíquota
        if salario <= 1320:
            aliquota = 0.075
            deducao = 0
        elif salario <= 2571.29:
            aliquota = 0.09
            deducao = 19.80
        elif salario <= 3856.94:
            aliquota = 0.12
            deducao = 96.94
        elif salario <= 7507.49:
            aliquota = 0.14
            deducao = 174.08
        else:
            return "Salário acima do teto do INSS."  # Caso o salário seja maior que o teto

        valor_retido = (salario * aliquota) - deducao  # Fórmula do INSS
        return valor_retido

    # Rendimento de investimento no CDI
    @staticmethod
    def calcular_rendimento_cdi():
        cdi_anual = 11.28  # Taxa anual do CDI
        # Cálculo do rendimento diário, considerando 252 dias úteis 
        rendimento_diario = cdi_anual / 252  
        print(f"Rendimento diário: {rendimento_diario:.2f}%")
        opcao = input("Quer calcular o rendimento mensal? (s/n): ").lower()
        if opcao == 's':
            # Cálculo mensal, considerando 21 dias úteis
            rendimento_mensal = rendimento_diario * 21  
            print(f"Rendimento mensal aproximado: {rendimento_mensal:.2f}%")
        else:
            print("Ok, cálculo encerrado.")


# Classe para conversão de moedas
class ConversorMoeda:

    # Taxas para conversão
    taxas = {
        'real': 5.72,
        'dolar': 1.0,
        'euro': 0.88,
        'bitcoin': 0.000011
    }

    # Converter moeda
    @classmethod
    def converter(cls, valor, moeda_destino):
        if moeda_destino in cls.taxas:
            convertido = valor * cls.taxas[moeda_destino]  # Conversão 
            return convertido
        else:
            return None  # Caso a moeda não esteja disponível 


# Menu da calculadora
def main():
    while True:
        os.system('cls')  # Limpa o terminal
        print("=== Calculadora Financeira ===")
        print("Escolha a operação:")
        print("1. Juros Compostos")
        print("2. Juros Simples")
        print("3. Desconto em Produto")
        print("4. Conversão de Moeda")
        print("5. Investimento CDI")
        print("6. Cálculo de INSS")
        print("0. Sair")

        escolha = input("Digite o número da operação desejada: ")

        # Juros Compostos 
        if escolha == "1":
            capital = float(input("Digite o capital inicial: "))
            taxa = float(input("Digite a taxa de juros (ex: 0.05 para 5%): "))
            tempo = int(input("Digite o tempo (número de períodos): "))
            montante = CalculadoraFinanceira.calcular_juros_compostos(capital, taxa, tempo)
            print(f"Montante final: R${montante:.2f}")

        # Juros Simples 
        elif escolha == "2":
            capital = float(input("Digite o capital inicial: "))
            taxa = float(input("Digite a taxa de juros (ex: 0.05 para 5%): "))
            juros = CalculadoraFinanceira.calcular_juros_simples(capital, taxa)
            print(f"Juros: R${juros:.2f}")

        # Desconto em produto 
        elif escolha == "3":
            valor = float(input("Digite o valor do produto: "))
            porcentagem = float(input("Digite a porcentagem de desconto: "))
            desconto = CalculadoraFinanceira.calcular_desconto(valor, porcentagem)
            print(f"Valor do desconto: R${desconto:.2f}")

        # Conversão de moeda 
        elif escolha == "4":
            valor = float(input("Digite o valor em dólares: "))
            moeda_destino = input("Digite a moeda destino (real, euro, bitcoin): ").lower()
            convertido = ConversorMoeda.converter(valor, moeda_destino)
            if convertido:
                print(f"Valor convertido: {convertido:.2f} {moeda_destino}")
            else:
                print("Moeda não encontrada.")

        # Rendimento em CDI 
        elif escolha == "5":
            CalculadoraFinanceira.calcular_rendimento_cdi()

        # Valor retido no INSS
        elif escolha == "6":
            salario = float(input("Digite o salário bruto: "))
            inss = CalculadoraFinanceira.calcular_inss(salario)
            if isinstance(inss, str):
                print(inss)
            else:
                print(f"Valor retido do INSS: R${inss:.2f}")

        # Encerrar o programa 
        elif escolha == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")

        # Pergunta se deseja continuar
        continuar = input("\nDeseja fazer outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Programa encerrado.")
            break


# Execução do programa
if __name__ == "__main__":
    main()
