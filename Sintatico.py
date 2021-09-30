import Lexico



class Sintatico:

    def __init__(self):
        self.termo = ''


    #FUNCOES <------------------------------------------------ <-
    def P():

    def C():

    def DC():

    def DCV():

    def TPV():

    def VAR():

    def MVAR():

    def CMS():

    def MCM():

    def CM():

    def COND():

    def REL():

    def EXP():

    def TERM():

    def OPU():

    def FATOR():

    def OTERM():

    def OPAD():

    def MFATOR():

    def OPMUL():

    def PFALSA():





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

