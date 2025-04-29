# Especificação Funcional 

<h2>Calculadora Financeira</h2>
Professor: Diego Possamai <br>
Alunas: Amanda Korczagin e Flavia Antonieli <br>

Sistema simples de operação lógica realizando na linguagem Python  com as seguintes funções determinadas. <br>

Execução das seguintes operações: <br>

- Juros compostos <br>  
  M = C.(1-i)^n <br>
  Montante = capital inicial, vezes 1 menos a taxa de juros elevado pelo tempo aplicado <br>

- Juros Simples <br>
  J = C . i <br>
  Juros = capital inicial, vezes  a taxa <br>

- Porcentagem de desconto na compra de um produto <br>
  R = V.(i/100) <br>
  Resultado = valor do produto . (porcentagem /100) <br>

- Conversão de moedas <br>
real, euro e dolar, bitcoin <br>
real: 5,72 <br>
dolar: 1 <br>
euro: 0,88 <br>
bitcoin: 0,000011 <br>

- Investimento CDI <br>
a taxa atual do CDI é de 11,28 <br>
Rendimento diário = CDI anual / 252 <br>
Rendimento mensal = soma de todas as taxas diárias de um mês, dividido pelo número de dias úteis. <br>

- Impostos INSS <br>
Valor retido = salario.alíquota-dedução <br>
Exemplo: valor retido = 3000.11%-165 <br>

<h2>Tecnologias Utilizadas</h2>
Para a execução do sistema você deve ter instalado em sua máquina: <br>
VS code: Download Visual Studio Code - Mac, Linux, Windows <br>
Extensão e biblioteca (Microsoft) Python: https://marketplace.visualstudio.com/items/?itemName=ms-python.python <br>
Linguagem Python: Download Python | Python.org  (selecione a opção de Add Python on Patch na instalação) <br>

<h2>Observações Adicionais</h2>
O programa é voltado para ambientes Windows (por conta do comando cls). As taxas de conversão de moedas são fixas e podem ser atualizadas manualmente no código. <br>
Os cálculos do INSS consideram a tabela vigente no momento do desenvolvimento. O fluxo é baseado em menus interativos no terminal (CLI - Command Line Interface). <br>
Para executar o código no VSCode, utilizar a opção “Run Python File in Terminal” após clicar com o botão direito no código. <br>

<h2>Plano de Testes</h2>

- Teste 1: Juros Compostos <br>
  Entrada: <br>
    Capital: 1000 <br>
    Taxa: 0.05 (5%) <br>
    Tempo: 2 períodos <br>
  Fórmula esperada: <br>
  Montante = 1000 * (1 + 0.05)² = 1102.50 <br>
  Resultado esperado: <br>
  R$1102.50 <br>

- Teste 2: Conversão de Moeda (Dólar → Real) <br>
  Entrada: <br>
    Valor: 10 dólares <br>
    Moeda destino: real <br>
    Taxa usada no código: 1 dólar = 5.72 reais <br>
  Resultado esperado: <br>
    10 * 5.72 = 57.20 reais <br>

- Teste 3: INSS (Salário dentro da 2ª faixa) <br>
  Entrada: <br>
    Salário: R$2000,00 <br>
  Cálculo esperado: <br>
    Alíquota: 9% (0.09) <br>
    Dedução: R$19,80 <br>
    Valor retido: 2000 * 0.09 - 19.80 = R$160.20 <br>
  Resultado esperado: <br>
    Valor retido do INSS: R$160.20 <br>








