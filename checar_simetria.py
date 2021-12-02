def checar_simetria(R):
    """
    Função que checa se uma lista é simétrica.
    """
    if R == []:
        return True
    
    pares_faltando = []
    for par in R:
        par_invertido = (par[1], par[0])
        if not par_invertido in R:
            pares_faltando.append(par_invertido)
    
    return {
        'simetrica': len(pares_faltando) == 0,
        'pares_faltando': pares_faltando
    }

def checar_antissimetria(R):

    pares_para_remover = []
    for par in R:
        par_invertido = (par[1], par[0])
        if par_invertido in R and par != par_invertido:
            pares_para_remover.append(par_invertido)
    
    return len(pares_para_remover) == 0
