from selenium import webdriver
import smtplib
from email.message import EmailMessage
import time
import os

"""SISTEMA DE ALERTA DE COMPARAÇÃO DE PREÇO"""
#preço alvo do produto
precoalvo=3499.00

#abrir o navegador
navegador=webdriver.Chrome()

#vai para pagina do ps5
link="https://www.amazon.com.br/s?k=ps5&adgrpid=126573007645&hvadid=596028639242&hvdev=c&hvexpln=0&hvlocphy=9222782&hvnetw=g&hvocijid=4147642922322881022--&hvqmt=e&hvrand=4147642922322881022&hvtargid=kwd-299883671737&hydadcr=14247_13413229&mcid=c5a3d9fe178a355287c1f861abb7cc5d&tag=hydrbrgk-20&ref=pd_sl_8efa39ozsq_e"
navegador.get(link)
time.sleep(10)

#pegar o preço do ps5 mais barato
preco=navegador.find_element("class name","a-price-whole").text
print(preco,'R$')
preco=preco.replace(".","").replace(",",".")
preco=float(preco)

#senha e email
usuario=os.getenv('EMAIL_USUARIO')
senha=os.getenv('EMAIL_SENHA')

#condição para enviar uma mensagem no meu email
if preco<=precoalvo:
    email=EmailMessage()
    email['Subject']='Alerta de preço'
    email['From']=usuario
    email['To']=usuario
    email.set_content(f'o ps5 abaixou para {preco}.\n confira agora!')


    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(usuario,senha)
        smtp.send_message(email)
    print('email enviado')
else:
    print('preço ainda não chegou no preço alvo')

time.sleep(10)