from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome="Brabo Lustosa", idade=33)
    pessoa.save()
    print(pessoa)

def consulta_pessoas():
    # busca uma pessoa
    pessoa = Pessoas.query.filter_by(nome="Cosmo Lustosa").first()
    return pessoa


if __name__ == "__main__":
    
    # insere_pessoas()
    print("====")
    consulta_pessoas() 
