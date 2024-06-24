import json
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split


def processar_resultados():
    # Carregar dados de um arquivo JSON
    with open('output/tournament_results.json', 'r') as file:
        data = json.load(file)

    all_data = []
    for noise_level, entries in data.items():
        for entry in entries:
            rates = {
                "Cooperation_rating": entry["Cooperation_rating"],
                "Initial_C_rate": entry["Initial_C_rate"],
                "CC_rate": entry["CC_rate"],
                "CD_rate": entry["CD_rate"],
                "DC_rate": entry["DC_rate"],
                "DD_rate": entry["DD_rate"],
                "CC_to_C_rate": entry["CC_to_C_rate"],
                "CD_to_C_rate": entry["CD_to_C_rate"],
                "DC_to_C_rate": entry["DC_to_C_rate"],
                "DD_to_C_rate": entry["DD_to_C_rate"],
                "Median_score": entry["Median_score"]
            }
            all_data.append(rates)

    # Converter dados em um DataFrame do Pandas
    df = pd.DataFrame(all_data)

    # Separar características (features) e resultado (target)
    x = df.drop(columns=["Median_score"])
    y = df["Median_score"]

    # Dividir os dados em conjuntos de treino e teste
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    # Treinar o modelo de árvore de decisão
    # Treinar o modelo
    arvore = DecisionTreeRegressor(random_state=42)
    arvore.fit(x_train, y_train)

    # Identificar as features mais importantes
    features_importancia = arvore.feature_importances_
    features_nome = x.columns

    exibir_importancias(features_nome, features_importancia)


def exibir_importancias(nomes, importancia):

    data_frame = pd.DataFrame({'Feature': nomes, 'Importancia': importancia})
    data_frame = data_frame.sort_values(by='Importancia', ascending=False)

    print(data_frame)


if __name__ == "__main__":
    processar_resultados()
