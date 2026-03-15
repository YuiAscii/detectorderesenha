def temResenha():
    print(f"""
    BEM-VINDO AO DETECTOR DE RESENHAS!
    O Averiguador de resenhas profissional!
    """)

    while True:
        userInput = input(f"Insira sua mensagem: ")

        if "resenha" in userInput.lower():
            resposta = input(f"Resenha presente! Deseja testar mais uma resenha? (Y ou N)  ").lower()

            if resposta == "y":
                continue
            elif resposta == "n":
                break

        else:
            resposta2 = input("Resenha nÃ£o encontrada, quer tentar de novo? (Y ou N)  ").lower()
            if resposta2 == "y":
                continue
            if resposta2 == "n":
                break
temResenha() 

"""---------------------------------------------------------------------
CODIGO REGISTRADO POR

 X     X                        XX                             
X     X                X        X  X     XXX              X    X
 X   X     X    X     X        XXXXX    X   X   XXXXXX   X    X 
  XX      X     X    X       X     X    XXX    XX       X    X  
  X        XXXX     X       X      X       X   XXXXXX  X    X   
                                       XXXX          
---------------------------------------------------------------------"""