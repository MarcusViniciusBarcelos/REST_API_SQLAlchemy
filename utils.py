from models import Pessoas


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


if __name__ == '__main__':
    insere_pessoas()

