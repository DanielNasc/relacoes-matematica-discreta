from re import sub
from simple_term_menu import TerminalMenu
from checar_transitividade import checar_transitividade
from checar_reflexividade import reflexiva_S_em_S, reflexiva_S_em_T
from prints import *

def main():
    print_ascii_art()

    opcao = TerminalMenu(["S em S", "S em T"], title="Qual modelo de relação você deseja?").show()
    S = get_conjunto('S')
    T = get_conjunto('T') if opcao == 1 else None
    R = tratar_relacao()

    if opcao == 0:
        print_result(R, 'reflexiva', reflexiva_S_em_S(S, R), 'reflexivo')
    else:
        print_result(R, 'reflexiva', reflexiva_S_em_T(S, T, R), 'reflexivo')
        
    print_result(R, 'transitiva', checar_transitividade(R), 'transitivo')
    

def tratar_relacao():
    # Remove os caracters especiais
    print("\nFormato do input: (a,b),(b,c),(a,c)")
    entrada = sub('[^),0-9a-zA-Z]', '', input('Digite a relação R: '))

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

def get_conjunto(c):
    conjuntos = input("Digite o conjunto {}: ".format(c))
    conjuntos = sub('[^0-9a-zA-Z,]', '', conjuntos)
    conjuntos = conjuntos.split(',')
    return conjuntos

if __name__ == '__main__':
    main()
