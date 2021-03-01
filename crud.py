import sqlite3
from time import sleep

conn = sqlite3.connect("storage.db")

db_cursor = conn.cursor()

db_cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email REAL NOT NULL
);
""")

# Funções interface

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mDigite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mInterrompido pelo usuário.\033[m')
            print('Saindo...')
            break
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt(f'\033[32mSua Opção:\033[m ')
    return opc

# Interação com o banco de dados

def selecionar_registros():
    db_cursor.execute("SELECT * FROM pessoas;")
    for line in db_cursor.fetchall():
        print(line)

def inserir_registro():
    db_cursor.execute("INSERT INTO pessoas(nome, email) VALUES (?, ?)",(nome, email))
    conn.commit()
    print('Registro inserido com sucesso!')

def atualizar_nome():
    db_cursor.execute("UPDATE pessoas SET nome = ? WHERE id = ?",(novo_nome, identificador))
    conn.commit()
    print('Registro atualizado com sucesso!')

def atualizar_email():
    db_cursor.execute("UPDATE pessoas SET nome = ? WHERE id = ?",(novo_email, identificador))
    conn.commit()
    print('Registro atualizado com sucesso!')

def deletar_registro():
    db_cursor.execute("DELETE FROM pessoas WHERE id = ?",(identificador,))
    conn.commit()
    print("Deleção realizada com sucesso!")

# Interface

while True:
    resposta = menu(['Ver Registros','Novo Registro', 'Atualizar Nome', 'Atualizar Email', 'Deletar Registro', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('VER REGISTROS')
        selecionar_registros()
    elif resposta == 2:
        cabecalho('NOVO REGISTRO')
        nome = input('Nome: ')
        email = input('Email: ')
        inserir_registro()
    elif resposta == 3:
        identificador = int(input('Insira o id da pessoa cadastrada: '))
        cabecalho('ATUALIZAR NOME')
        novo_nome = input('Novo Nome: ')
        atualizar_nome()
    elif resposta == 4:
        cabecalho('ATUALIZAR EMAIL')
        identificador = int(input('Insira o id da pessoa cadastrada: '))
        novo_email = input('Novo Email: ')
        atualizar_email()
    elif resposta == 5:
        cabecalho('DELETAR REGISTRO')
        identificador = int(input('Insira o id do registro a ser deletado: '))
        deletar_registro()
    elif resposta == 6:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        cabecalho(f'\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

