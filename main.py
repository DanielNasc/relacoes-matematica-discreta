from re import sub
from checar_transitividade import transitiva
from print_ascii import print_ascii_art

def main():
    # Pedir uma relação R ao usuário
    # Ex: (1,3),(1,4),(2,1),(3,2)
    print_ascii_art()
    R = tratar_entrada(input('Digite a relação R: '))
    # print(R)

    # Checar se R é transitiva
    result = transitiva(R)

    # Imprimir o resultado
    if result['e_transitiva']:
        print('\nA relação R é transitiva')
    else:
        print('\nA relação R não é transitiva')
        print('Fecho transitivo de R:', f"{R + result['pares_necessarios']}".replace("'", ''))

def tratar_entrada(entrada: str):
    # Remove os caracters especiais
    entrada = sub('[^),0-9a-zA-Z]', '', entrada)

    # Relação R
    R = []

    # Separar os elementos da relação R
    for elemento in entrada.split('),'):
        # Separar os elementos do par
        par = tuple([x.replace(')', '') for x in elemento.split(',')])
        # Adicionar o par na relação R se ele não estiver repetido
        if not par in R:
            R.append(par)
    return R

if __name__ == '__main__':
    main()
