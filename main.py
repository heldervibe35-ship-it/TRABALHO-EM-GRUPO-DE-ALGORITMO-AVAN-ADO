import random

def funcao_objetivo(x):
    return x ** 2

def pso():
    numero_particulas = 30
    iteracoes = 100
    w = 0.7
    c1 = 1.5
    c2 = 1.5
    limite_inferior = -10
    limite_superior = 10

    posicoes = [
        random.uniform(limite_inferior, limite_superior)
        for _ in range(numero_particulas)
    ]
    velocidades = [
        random.uniform(-1, 1)
        for _ in range(numero_particulas)
    ]

    pbest = posicoes.copy()
    indice = min(
        range(numero_particulas),
        key=lambda i: funcao_objetivo(pbest[i])
    )
    gbest = pbest[indice]

    for _ in range(iteracoes):
        for i in range(numero_particulas):
            r1 = random.random()
            r2 = random.random()

            velocidades[i] = (
                w * velocidades[i]
                + c1 * r1 * (pbest[i] - posicoes[i])
                + c2 * r2 * (gbest - posicoes[i])
            )

            posicoes[i] += velocidades[i]

            if posicoes[i] < limite_inferior:
                posicoes[i] = limite_inferior
                velocidades[i] = 0
            elif posicoes[i] > limite_superior:
                posicoes[i] = limite_superior
                velocidades[i] = 0

            if funcao_objetivo(posicoes[i]) < funcao_objetivo(pbest[i]):
                pbest[i] = posicoes[i]

        indice = min(
            range(numero_particulas),
            key=lambda i: funcao_objetivo(pbest[i])
        )
        gbest = pbest[indice]

    return gbest, funcao_objetivo(gbest)

if __name__ == "__main__":
    melhor_x, melhor_valor = pso()
    print("Melhor solução encontrada:", melhor_x)
    print("Valor da função objetivo:", melhor_valor)
