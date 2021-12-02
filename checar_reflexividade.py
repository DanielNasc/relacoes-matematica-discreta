# S_test = [1, 2, 3 , 4, 10]
# T_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# R_test = [(3, 3), (2, 2), (5, 5), (1, 3)]

def reflexiva_S_em_S(S, R):
    # Cria uma lista com os elementos de S, tal que para todo x em S, é criado um par (x, x)
    pares_necessarios = []
    for e in S:
        pares_necessarios.append((e, e))

    # Verifica se os todos os pares (x, x) existem em R
    reflexiva, pares_faltando = checar_pares_necessarios(R, pares_necessarios)

    # Se R é uma relação reflexiva, então retorna um dict com 'reflexiva' como True e 'pares_faltando' como uma lista vazia
    # Caso contrário, retorna um dict com 'reflexiva' como False e 'pares_faltando' como a lista de pares que faltam

    return {
        "reflexiva": reflexiva,
        'pares_faltando': pares_faltando
    }

def reflexiva_S_em_T(S, T, R):

    # Cria uma lista com os elementos iguais de S e T, tal que para todo x em S e T, é criado um par (x, x)
    pares_necessarios = []
    for e in S:
        if e in T:
            pares_necessarios.append((e, e))
    
    # Verifica se os todos os pares (x, x) existem em R
    reflexiva, pares_faltando = checar_pares_necessarios(R, pares_necessarios)

    # Se R é uma relação reflexiva, então retorna um dict com 'reflexiva' como True e 'pares_faltando' como uma lista vazia
    # Caso contrário, retorna um dict com 'reflexiva' como False e 'pares_faltando' como a lista de pares que faltam
    return {
        "reflexiva": reflexiva,
        'pares_faltando': pares_faltando
    }

    

def checar_pares_necessarios(R, pares_necessarios):
    # Verifica se os todos os pares (x, x) existem em R
    reflexiva = True
    pares_faltando = []
    for par in pares_necessarios:
        # Se o par não existir em R, ele é adicionado à lista de pares que faltam
        if not par in R:
            reflexiva = False
            pares_faltando.append(par)
    return [reflexiva, pares_faltando]

# Testes        
# result = reflexiva_S_em_S(S_test, R_test)

# if result['reflexiva']:
#     print('E reflexiva')
# else:
#     print('Nao e reflexiva')
#     print('Fecho reflexivo: ', R_test + result['pares_faltando'])

# result = reflexiva_S_em_T(S_test, T_test, R_test)

# if result['reflexiva']:
#     print('E reflexiva')
# else:
#     print('Nao e reflexiva')
#     print('Fecho reflexivo: ', R_test + result['pares_faltando'])
