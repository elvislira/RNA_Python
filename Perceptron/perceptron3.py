import numpy as np


entradas = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
saidas = np.array([
    0,
    0,
    0,
    1
])
pesos = np.array([0.0, 0.0])
taxa_aprendizagem = 0.1


def funcao_soma(entrada, peso):
    return entrada.dot(peso)


def funcao_ativacao(s):
    if s >= 1:
        return 1
    
    return 0


def treinar():
    erro_total = 1

    while erro_total != 0:
        erro_total = 0

        for i in range(len(saidas)):
            saida_calculada = funcao_soma(np.array(entradas[i]), pesos)
            ativacao = funcao_ativacao(saida_calculada)
            erro = abs(saidas[i] - ativacao)
            erro_total += erro

            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxa_aprendizagem * entradas[i][j] * erro)
            
            print(f'Peso atualizado: {pesos}')

        print(f'Total de erros: {erro_total}')

treinar()