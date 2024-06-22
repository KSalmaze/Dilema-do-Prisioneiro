import axelrod as axl
import json

# Definir as estratégias corrigidas
strategies = [
    axl.Cooperator(),
    axl.Defector(),
    axl.TitForTat(),
    axl.Random(),
    axl.Grudger(),
    axl.WinStayLoseShift(),
    axl.TitFor2Tats(),
    axl.BackStabber(),
    axl.CyclerDDC(),
    axl.CyclerCCCD(),
    axl.ZDGTFT2(),
    axl.EvolvedLookerUp2_2_2(),
    axl.EvolvedANN(),
    axl.EvolvedFSM16(),
    axl.CyclerDC()
]

# Níveis de ruído para os campeonatos
noise_levels = [0.0, 0.1, 0.2, 0.3, 0.4]

# Dicionário para armazenar os resultados
tournament_results = {}

# Gerar campeonatos
for noise in noise_levels:
    tournament = axl.Tournament(strategies, repetitions=5, noise=noise)
    results = tournament.play()
    # Armazenar resultados
    tournament_results[f'Noise_{noise}'] = results.summarise()

# Salvar resultados em um arquivo JSON
with open('tournament_results.json', 'w') as f:
    json.dump(tournament_results, f)