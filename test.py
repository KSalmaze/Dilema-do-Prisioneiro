import axelrod as axl
import json
import csv

# Definir as estratégias
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

# Gerar campeonatos (rever a logica dps)
for noise in noise_levels:
    tournament = axl.Tournament(strategies, repetitions=5, noise=noise)
    results = tournament.play()
    # Armazenar resultados
    summary = results.summarise()
    scores_sum = {}
    for entry in summary:
        strategy_name = entry[1]  # Ajuste para acessar o nome da estratégia por índice
        if strategy_name not in scores_sum:
            print(strategy_name)
            scores_sum[strategy_name] = 0
        scores_sum[strategy_name] += entry[2]

        tournament_results[f'Noise_{noise}'] = scores_sum
    
    for strategy in strategies:
        if strategy.name not in scores_sum:
            scores_sum[strategy.name] = 0

# Salvar resultados em um arquivo JSON
# with open('tournament_results.json', 'w') as f:
#     json.dump(tournament_results, f)

# Salvar em csv
with open('tournament_results.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Strategy'] + list(tournament_results.keys()))
    for strategy in strategies:
        row = [strategy.name]
        for noise in noise_levels:
            row.append(tournament_results[f'Noise_{noise}'][strategy.name])
        writer.writerow(row)
