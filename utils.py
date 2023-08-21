from models import (Pessoas,
                    Usuarios)


def insere_pessoas():
    pessoa = Pessoas(nome='Vinicius', idade=26)
    print(pessoa)
    pessoa.save()


def consulta_pessoa():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Marcus').first()
    print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Marcus').first()
    pessoa.idade = 21
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Marcus').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    # insere_usuario('marcus', '123')
    # insere_usuario('vinicius', '321')
    consulta_todos_usuarios()
