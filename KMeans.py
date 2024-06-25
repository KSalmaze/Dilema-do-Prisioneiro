from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt


def rodar_kmeans(n_clusters=2):


    with open('output/tournament_results.json', 'r') as file:
        data = json.load(file)

    # Preparar os dados
    cluster_data = []
    for noise_level, entries in data.items():
        for entry in entries:
            rates = {
                "CD_rate": entry["CD_rate"],
                "DC_rate": entry["Median_score"]
                # "CC_to_C_rate": entry["CC_to_C_rate"]
            }
            cluster_data.append(rates)

    # Converter dados em um DataFrame do Pandas
    df = pd.DataFrame(cluster_data)

    # Aplicar K-Means com k=3
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(df)

    # Visualizar os ‘clusters’
    plt.scatter(df['CD_rate'], df['Median_score'], c=df['Cluster'], cmap='viridis')
    plt.xlabel('CD_rate')
    plt.ylabel('Median_score')
    plt.title(f'Clusters K-Means (k={n_clusters})')
    plt.colorbar(label='Cluster')
    plt.show()

    # Exibir os dados clusterizados
    print(df)

def rodar_kmeans(noise_levels, n_clusters=3):
    # Carregar dados de um arquivo JSON
    with open('output/tournament_results.json', 'r') as file:
        data = json.load(file)

    for noise_level in noise_levels:
        # Preparar os dados para o nível de ruído atual
        if f"Noise_{noise_level}" in data:
            cluster_data = []
            for entry in data[f"Noise_{noise_level}"]:
                rates = {
                    "Name": entry["Name"],
                    "CD_rate": entry["CD_rate"],
                    # "DC_rate": entry["DC_rate"],
                    "Median_score": entry["Median_score"],
                    # "CC_to_C_rate": entry["CC_to_C_rate"]
                }
                cluster_data.append(rates)

            # Converter dados em um DataFrame do Pandas
            df = pd.DataFrame(cluster_data)

            # Aplicar K-Means com k=3
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            df['Cluster'] = kmeans.fit_predict(df[['CD_rate', 'Median_score']])

            # Visualizar os clusters
            plt.scatter(df['CD_rate'], df['Median_score'], c=df['Cluster'], cmap='viridis')
            plt.xlabel('CD_rate')
            plt.ylabel('Median_score')
            plt.title(f'Clusters K-Means (k={n_clusters}) - Noise {noise_level}')
            plt.colorbar(label='Cluster')

            for i, txt in enumerate(df['Name']):
                plt.annotate(txt, (df['CD_rate'][i], df['Median_score'][i]), fontsize=8, alpha=0.75)

            # Salvar o gráfico
            plt.savefig(f'kmeans_clusters_noise_{noise_level}.png')
            plt.show()
            plt.close()

            # Exibir os dados clusterizados
            print(f'Dados clusterizados para Noise {noise_level}:')
            print(df)
        else:
            print(f'No data available for Noise {noise_level}')


if __name__ == "__main__":
    rodar_kmeans()
