contadores = {}

def gerar_matricula(curso):
    if curso not in contadores:
        contadores[curso] = 0

    contadores[curso] += 1
    return f"{curso}{contadores[curso]}"
