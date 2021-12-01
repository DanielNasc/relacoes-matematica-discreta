from checar_transitividade import transitiva

def main():
    R = tratar_input(input())
    result = transitiva(R)
    if result[0]:
        print("É transitiva")
    else:
        print('Não é transitiva')
        print('Fecho de R: ', R + result[1])
    return

def tratar_input(texto: str):
    elementos = []
    texto_sanitizado = texto.strip().split('),')
    
    for ts in texto_sanitizado:
        nums = ts.replace('(','').split(',')
        e = []
        for n in nums:
            e.append(int(n.replace(')', '')))
        elementos.append(tuple(e))
    return elementos

if __name__ == '__main__':
    main()
