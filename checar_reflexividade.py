S_test = [1, 2, 3 , 4]
R_test = [(3, 3), (2, 2)]

def reflexiva(S, R: list):
    e_reflexiva = True

    pares_necessarios = []
    for e in S:
        pares_necessarios.append((e, e))

    pares_faltando = []
    for par in pares_necessarios:
        if not par in R:
            e_reflexiva = False
            pares_faltando.append(par)

    if e_reflexiva:
        return {
            "e_reflexiva": e_reflexiva,
            'pares_faltando': pares_faltando
        }
    else: 
        return {
            'e_reflexiva': e_reflexiva,
            'pares_faltando': pares_faltando + reflexiva(S, R + pares_faltando)['pares_faltando']
        }
            
result = reflexiva(S_test, R_test)

if result['e_reflexiva']:
    print('E reflexiva')
else:
    print('Nao e reflexiva')
    print('Fecho reflexivo: ', R_test + result['pares_faltando'])
