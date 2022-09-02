# Enunciado: Testando a biblioteca rich
# Programa Desenvolvido em Python 03
# Dashboard 

from rich import print
from rich.prompt import Prompt
from rich.progress import track
from rich.console import Console
from time import sleep
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel

console = Console()
prompt = Prompt()
continuar = True

print()
print('-='*40)
print(f'{"[blue][bold]Informe seu CPF para Validar o Financiamento":^80}[/][/]')
print('-='*40)
print()

while continuar == True:
    cpf = int(prompt.ask('[green] Digite seu [bold]CPF[/]: [/]'))
    resposta = prompt.ask(
        f' Você digitou [red]{cpf}[/], este número está correto? [s ou n]').strip().lower()
    if resposta.lower() in ('s', 'sim'):
        print('[blue][bold] Ótimo! Vamos Analisar: [/][/]')
        continuar = False
    elif resposta.lower() in ('n', 'não'):
        print('[green][bold] Reiniciando...[/][/]')
        sleep(1)
    else:
        print(' Digite apenas [red][bold]"s"[/][/] ou [red][bold]"n"[/][/]')
sleep(1)
def consultar_cpf():
    console.log(' CPF sem bloqueios;')
    sleep(2)
    console.log(' Sem multas em financiamentos;')
    sleep(2)
    console.log(' Nome não encontrado no Serasa;')
    sleep(2)
    console.log(' Dados validados com sucesso.')

print()
with console.status('[green]Preenchendo formulário[/]') as status:
    consultar_cpf()
print()
print('[green] Seu CPF está pronto para um financiamento![/]')

print()
table = Table(title=' Financiamentos Disponíveis.')
print()
table.add_column("Meses")
table.add_column("Valor")
table.add_column("Taxa de juros")

table.add_row('12x', 'R$1750,00', '7.5%')
table.add_row('36', 'R$560,00', '12.0%')
table.add_row('72x', 'R$360,00', '15.5%')

print(table)
print()
tipo_financiamento = prompt.ask(' [green][bold]Qual financiamento deseja contratar?[/][/]',
                                choices=['12x', '36x', '72x'])

print()
nome = str(input('\033[1;33m Digite seu nome para finalizar:\033[m ')).strip().upper()
print()
print(
    f'[on blue][black][bold] Parabéns [white]{nome}[/], você escolheu o financiamento de [green]{tipo_financiamento}[/][/][/][/]')

print()
print('-='*40)
print(f'{"[blue][bold]Programa Finalizado com Sucesso":^80}[/][/]')
print('-='*40)
print()
