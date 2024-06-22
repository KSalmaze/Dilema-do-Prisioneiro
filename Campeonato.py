import axelrod as axl
from axelrod import ResultSet


def gerar_campeonatos():
    print("Gerando campeonatos")

    estretagias = (axl.Cooperator(), axl.Alternator(), axl.TitForTat())
    campeonato = axl.Tournament(estretagias)
    resultado = campeonato.play()
    salvar_resultado(resultado)


def salvar_resultado(resultados: ResultSet):
    print("Salvar os arquivos")
