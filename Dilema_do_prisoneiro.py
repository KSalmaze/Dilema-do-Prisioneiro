import os
import axelrod as axl
import json


def rodar_campeonato(noise_levels = [0.0, 0.1, 0.2, 0.3, 0.4]):
    # Ensure the directory exists
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    # Define strategies
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

    # Dictionary to store the results
    tournament_results = {}

    # Generate tournaments
    for noise in noise_levels:
        tournament = axl.Tournament(strategies, repetitions=5, turns=100, noise=noise)
        results = tournament.play()
        # Store results
        summary = results.summarise()

        # Process summary to ensure integer values for victories and losses
        processed_summary = []
        for entry in summary:
            new_entry = entry._asdict()
            processed_summary.append(new_entry)

        tournament_results[f'Noise_{noise}'] = processed_summary

    # Save results to a JSON file
    json_file_path = os.path.join(output_dir, 'tournament_results.json')
    with open(json_file_path, 'w') as f:
        json.dump(tournament_results, f, indent=4)
