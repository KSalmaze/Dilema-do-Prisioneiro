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
                "DC_rate": entry["DC_rate"]
                # "CC_to_C_rate": entry["CC_to_C_rate"]
            }
            cluster_data.append(rates)

    # Converter dados em um DataFrame do Pandas
    df = pd.DataFrame(cluster_data)

    # Aplicar K-Means com k=3
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(df)

    # Visualizar os ‘clusters’
    plt.scatter(df['CD_rate'], df['DC_rate'], c=df['Cluster'], cmap='viridis')
    plt.xlabel('CD_rate')
    plt.ylabel('DC_rate')
    plt.title('Clusters K-Means (k=3)')
    plt.colorbar(label='Cluster')
    plt.show()

    # Exibir os dados clusterizados
    print(df)


if __name__ == "__main__":
    rodar_kmeans()
