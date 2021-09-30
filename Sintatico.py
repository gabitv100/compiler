import Lexico



class Sintatico:

    def __init__(self):
        self.termo = ''





    def simbolo(lex):
        for i in lex.Tokens:
            simbolo = i
            print(simbolo)
            # print("SINTATICO ::: " + str(simbolo))

    arquivo = open('teste.txt', 'r')
    unica_string = arquivo.read()
    arquivo.close()
    # print(unica_string)
    posicao = 0
    estado = 0

    lex = Lexico.Lex()

    for i in unica_string:
        estado = lex.nextToken(estado=estado, c=i,self='')
        print('Estado atual -> ' + str(estado))
    print(lex.Tokens)

    simbolo(lex)


