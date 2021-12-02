def print_ascii_art():
    print('''
         _                                          
   ___  | |__     ___    ___    __ _   _ __ 
  / __| | '_ \   / _ \  / __|  / _` | | '__|
 | (__  | | | | |  __/ | (__  | (_| | | |   
  \___| |_| |_|  \___|  \___|  \__,_| |_|   

                _                                     
  _ __    ___  | |   __ _    ___    ___     ___   ___ 
 | '__|  / _ \ | |  / _` |  / __|  / _ \   / _ \ / __|
 | |    |  __/ | | | (_| | | (__  | (_) | |  __/ \__ \ 
 |_|     \___| |_|  \__,_|  \___|  \___/   \___| |___/
                                                      
                                                                                            
    ''')

def print_result(R, prop, result, fecho):
  if result[prop]:
    print("\nA relação R é {}".format(prop))
  else:
    print("\nA relação R não é {}".format(prop))
    print("Fecho {}".format(fecho), f"{R + result['pares_faltando']}".replace("'", ''))

def print_antissimetria(R, antissimetrica):
  if antissimetrica['antissimetrica']:
    print("\nA relação R é antissimétrica")
  else:
    print("\nA relação R não é antissimétrica")
    print("Redução antissimétrica: {}"
          .format([x for x in R if x not in antissimetrica['pares_para_remover']])
          .replace("'", ''))
    