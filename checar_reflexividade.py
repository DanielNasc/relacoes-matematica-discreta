def reflexiva_S_em_S(S, R):
    # Cria uma lista com os elementos de S, tal que para todo x em S, é criado um par (x, x)
    pares_necessarios = []
    for e in S:
        pares_necessarios.append((e, e))

    # Verifica se os todos os pares (x, x) existem em R
    pares_faltando = checar_pares_necessarios(R, pares_necessarios)

    # Se R é uma relação reflexiva, então retorna um dict com 'reflexiva' como True e 'pares_faltando' como uma lista vazia
    # Caso contrário, retorna um dict com 'reflexiva' como False e 'pares_faltando' como a lista de pares que faltam
    return {
        "reflexiva": len(pares_faltando) == 0,
        'pares_faltando': pares_faltando
    }

def reflexiva_S_em_T(S, T, R):

    # Cria uma lista com os elementos iguais de S e T, tal que para todo x em S e T, é criado um par (x, x)
    pares_necessarios = []
    for e in S:
        if e in T:
            pares_necessarios.append((e, e))
    
    # Verifica se os todos os pares (x, x) existem em R
    pares_faltando = checar_pares_necessarios(R, pares_necessarios)

    # Se R é uma relação reflexiva, então retorna um dict com 'reflexiva' como True e 'pares_faltando' como uma lista vazia
    # Caso contrário, retorna um dict com 'reflexiva' como False e 'pares_faltando' como a lista de pares que faltam
    return {
        "reflexiva": len(pares_faltando) == 0,
        'pares_faltando': pares_faltando
    }
    

def checar_pares_necessarios(R, pares_necessarios):
    # Verifica se os todos os pares (x, x) existem em R
    pares_faltando = []
    for par in pares_necessarios:
        # Se o par não existir em R, ele é adicionado à lista de pares que faltam
        if not par in R:
            pares_faltando.append(par)
    return pares_faltando
