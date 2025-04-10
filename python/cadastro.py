from PySimpleGUI import PySimpleGUI as sg
import requests

url = 'http://localhost:5000/api/usuarios/cadastrar'

#layout cadastro
sg.theme('Reddit')
layout = [
    [sg.Text('Nome de usuário:', font=('monospace',15)), sg.Input(key='nome', size=(15, 1), font=('monospace',15))],
    [sg.Text('Data de nascimento\n(mês/dia/ano):', font=('monospace',15)), sg.InputText(key='data', size=(20, 1), font=('monospace',15)), sg.CalendarButton("Selecionar Data", target="data", format='%m/%d/%y', font=('monospace',15))],
    [sg.Text('Email:', font=('monospace',15)), sg.Input(key='email', size=(20, 1), font=('monospace',15))],
    [sg.Text('Senha:', font=('monospace',15)), sg.Input(key='senha', password_char='*', size=(20, 1), font=('monospace',15))],
    [sg.Button('Cadastrar', key='cadastrar', font=('monospace',15))]
]

janela = sg.Window('Cadastro', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break;
    else:
        print(valores)
        nome, data, botao, email, senha = valores.values()
        print(data)
        if evento == 'cadastrar' and len(nome) == 0 or len(data) == 0 or len(email) == 0 or len(senha) == 0:
            sg.popup('Preencha todos os campos', title='Aviso', text_color='white', background_color='red')
        else:
            dados = {'nome': nome, 'data': data, 'email': email, 'senha': senha}
            try:
                resposta = requests.post(url, json=dados, timeout=20)
                sg.popup(resposta.json()['mensagem'], title='Aviso', font=('monospace',15))
            except requests.exceptions.RequestException as e:
                print(f'Erro ao enviar dados: {e}')
        
