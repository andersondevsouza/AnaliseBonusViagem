import pandas as pd
from twilio.rest import Client

def enviar_sms(vendedor, vendas, mensagem):
    # Your Account SID from twilio.com/console
    account_sid = "Your Account SID"
    # Your Auth Token from twilio.com/console
    auth_token = "Your Account Token"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+5516XXXXXXXXX", # celular de destino do sms
        from_="+16XXXXXXXXX", # numero gerado pelo twilio
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