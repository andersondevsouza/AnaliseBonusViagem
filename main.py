import pandas as pd
from twilio.rest import Client

def enviar_sms(vendedor, vendas, mensagem):
    # Your Account SID from twilio.com/console
    account_sid = "ACeb419a9684b41bafe213c3d3094e0161"
    # Your Auth Token from twilio.com/console
    auth_token = "205ba8ed12b19659cb6e46d6a1998736"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+5516992875188",
        from_="+16894076022",
        body=mensagem)
    print(message.sid)

def verificar_bonus_meta():
    lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

    for mes in lista_meses:
        tabela_vendas = pd.read_excel(f'{mes}.xlsx')
        if (tabela_vendas['Vendas'] > 55000).any():
            vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
            vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
            mensagem = f'No mês {mes} alguém bateu a meta. Vendedor = {vendedor}, Vendas: {vendas}'
            enviar_sms(vendedor, vendas, mensagem)

verificar_bonus_meta()