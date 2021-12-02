from checar_transitividade import checar_transitividade
from checar_reflexividade import reflexiva_S_em_S, reflexiva_S_em_T
from checar_simetria import *
from prints import *

class Result:
    def __init__(self, R: list, S, opt, T) -> None:    
        self.R = R
        self.transitiva = checar_transitividade(R)
        self.simetrica = checar_simetria(R)
        self.antissimetrica = checar_antissimetria(R.copy())
        
        self.opcao = opt
        if opt == 1:
            self.reflexiva = reflexiva_S_em_T(S, T, R)
        else:
            self.reflexiva = reflexiva_S_em_S(S, R)

    def prints(self) -> None:

        print_result(self.R, 'reflexiva', self.reflexiva, 'reflexivo')
        print_result(self.R, 'transitiva', self.transitiva, 'transitivo')
        print_result(self.R, 'simetrica', self.simetrica, 'simétrico')
        print_antissimetria(self.R, self.antissimetrica) 

        if self.reflexiva['reflexiva'] and self.transitiva['transitiva']:
            if self.simetrica['simetrica']:
                print("\nR é uma relação de equivalência")
            if self.antissimetrica['antissimetrica']:
                print("\nA relação é uma Ordem Parcial")
        