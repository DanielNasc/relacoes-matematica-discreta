# from prints import *
# R_test = [(2,2),(3,3)]

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

def checar_assimetria(R):
    """
    Função que checa se uma lista é assimétrica.
    """
    
    pares_para_remover = []
    for par in R:
        par_invertido = (par[1], par[0])
        if par_invertido in R and par != par_invertido:
            pares_para_remover.append(par_invertido)
    
    return len(pares_para_remover) == 0

# print_result(R_test, 'simetrica', checar_simetria(R_test), 'simétrico')
# print_assimetria(checar_assimetria(R_test))