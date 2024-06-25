import Dilema_do_prisoneiro
import ProcessarResultados
import KMeans

noise_levels = [0.0, 0.1, 0.2, 0.3, 0.4]

Dilema_do_prisoneiro.rodar_campeonato(noise_levels)

ProcessarResultados.processar_resultados()

KMeans.rodar_kmeans(noise_levels, 4)
