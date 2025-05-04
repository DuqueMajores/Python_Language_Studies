tabuleiro = [["-", "-", "-"], 
             ["-", "-", "-"], 
             ["-", "-", "-"]]

def dot():
    print("--------------------------------------")

while(True):
    dot()
    opc = input("A1, B1, C1\n" \
    "A2, B2, C2\n" \
    "A3, B3, C3\n" \
    "Escolha: ")

    if(opc == "A1"):
        tabuleiro[0][0] = "x"
    elif(opc == "B1"):
        tabuleiro[0][1] = "x"
    elif(opc == "C1"):
        tabuleiro[0][2] = "x"
    elif(opc == "A2"):
        tabuleiro[1][0] = "x"
    elif(opc == "B2"):
        tabuleiro[1][1] = "x"
    elif(opc == "C2"):
        tabuleiro[1][2] = "x"
    elif(opc == "A3"):
        tabuleiro[2][0] = "x"
    elif(opc == "B3"):
        tabuleiro[2][1] = "x"
    elif(opc == "C3"):
        tabuleiro[2][2] = "x"

    dot()
    for c in tabuleiro:
        print(c)

    dot()
    opc2 = input("A1, B1, C1\n" \
    "A2, B2, C2\n" \
    "A3, B3, C3\n" \
    "Escolha: ")

    if(opc2 == "A1"):
        tabuleiro[0][0] = "0"
    elif(opc2 == "B1"):
        tabuleiro[0][1] = "0"
    elif(opc2 == "C1"):
        tabuleiro[0][2] = "0"
    elif(opc2 == "A2"):
        tabuleiro[1][0] = "0"
    elif(opc2 == "B2"):
        tabuleiro[1][1] = "0"
    elif(opc2 == "C2"):
        tabuleiro[1][2] = "0"
    elif(opc2 == "A3"):
        tabuleiro[2][0] = "0"
    elif(opc2 == "B3"):
        tabuleiro[2][1] = "0"
    elif(opc2 == "C3"):
        tabuleiro[2][2] = "0"

    dot()
    for c in tabuleiro:
        print(c)
