# Função que checa se existem elementos em R que possuem seu x igual ao y do par dado
def checar_se_y1_e_igual_a_x2(R, y):
    elementos_que_satisfazem = []
    for r in R:
        if y == r[0]:
            elementos_que_satisfazem.append(r)
    
    # Retorna os elementos que satisfazem a condição ou None, caso não haja nenhum
    return elementos_que_satisfazem if len(elementos_que_satisfazem) > 0 else None

# Checa se a Relação R é transitiva
def transitiva(R):
    e_transitiva = True
    pares_necessarios = []
    # Percorre todos os elementos de R
    for r in R:
        # Se x = y, então não precisa checar
        if r[0] == r[1]:
            continue

        # Checa se existem elementos em R que possuem seu x igual ao y do par atual
        elementos = checar_se_y1_e_igual_a_x2(R, r[1])
        # Se não existir, continua o loop
        if not elementos:
            continue
        
        for b in elementos:
            # Checa se R contém o par necessário para que a relação seja transitiva
            par_necessario = (r[0], b[1])
            if not par_necessario in R:
                # Se não existir, a relação não é transitiva
                if par_necessario not in pares_necessarios: pares_necessarios.append(par_necessario)
                e_transitiva = False
    
    # Retorna uma lista com uma variavel que diz se a relação é transitiva ou não
    # e uma tupla com os pares necessários para que a relação seja transitiva (vazia caso seja transitiva)
    return [e_transitiva, pares_necessarios]

