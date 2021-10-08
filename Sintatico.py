import Lexico





lex = Lexico.Lex()
pos = 0
simbolo=''

arquivo = open('teste.txt', 'r')
unica_string = arquivo.read()
arquivo.close()
# print(unica_string)
posicao = 0
estado = 0

for i in unica_string:
    estado = lex.nextToken(estado=estado, c=i, self='')
    print('Estado atual -> ' + str(estado))
print(lex.Tokens)
listaTokens = (lex.Tokens)

def disparaErro(esperado):
    print('Erro sintatico, era esperado: ' + esperado)
    return 0


# FUNCOES <------------------------------------------------ <-


def MVAR(lex):
    if lex.simbolo == ',':
        getSimbolo(lex)
        VAR(lex)
    else:
        return lex


def VAR(lex):
    if lex.tipo == 'VARIAVEL':
        print('DEBUG: ' + lex.simbolo)
        getSimbolo(lex)
        MVAR(lex)
    else:
        disparaErro(' alguma variavel')




def TPV(lex):
    if lex.simbolo in ['real','integer']:
        print('DEBUG: ' + lex.simbolo)
        getSimbolo(lex)
    else:
        disparaErro('real ou integer')

def DCV(lex):
    TPV(lex)
    if lex.simbolo == ':':
        print('DEBUG: ' + lex.simbolo)
        getSimbolo(lex)
        VAR(lex)
    else:
        disparaErro(' : ')

def MDV(lex):
    if lex.simbolo == ';':
        DC(lex)
    else:
        disparaErro(';')
def DC(lex):
    DCV(lex)
    if lex.simbolo == ';':
        getSimbolo(lex)
        DCV(lex)
        return lex
    elif lex.tipo == 'RESERVADA':
        DC(lex)
    else:
        disparaErro('DC')

def MCM(lex):
    if lex.simbolo == ';':
        print('DEBUG: ' + lex.simbolo)
        getSimbolo(lex)
        CMS(lex) # PODE TER RECURSAO INFINITA AQUI

# def MFATOR(lex):


def FATOR(lex):
    if lex.tipo in ['INTEIRO','FLOAT','VARIAVEL']:
        print('DEBUG: ' + lex.simbolo)
        getSimbolo(lex)
    elif lex.simbolo=='(':
        print('DEBUG: ' + lex.simbolo)
        EXP(lex)
        if lex.simbolo == ')':
            getSimbolo(lex)
        else:
            disparaErro(') ')



def OPUN(lex):
    if lex.simbolo == '-':
        getSimbolo(lex)

# def OTERM(lex):


def TERM(lex):
    OPUN(lex)
    FATOR(lex)
    # MFATOR(lex)

def EXP(lex):
    TERM(lex)
    # OTERM(lex)



def CM(lex):
    if lex.simbolo in ['read','write']:
        print('DEBUG: ' + lex.simbolo)
        getSimbolo(lex)
        if lex.simbolo == '(':
            print('DEBUG: ' + lex.simbolo)
            getSimbolo(lex)
            if lex.tipo == 'VARIAVEL':
                print('DEBUG: ' + lex.simbolo)
                getSimbolo(lex)
                if lex.simbolo == ')':
                    print('DEBUG: ' + lex.simbolo)
                    getSimbolo(lex)
                    MCM(lex)
                else:
                    disparaErro(')')
            else:
                disparaErro('nome de variavel')
        else:
            disparaErro('(')
    elif lex.tipo == 'VARIAVEL':
        print('DEBUG: ' + lex.simbolo)
        getSimbolo(lex)
        if lex.tipo == 'ATRIBUICAO':
            getSimbolo(lex)
            EXP(lex)






def CMS(lex):
    CM(lex)


def C(lex):
    if lex.tipo == 'RESERVADA':
        lex = DC(lex)
        getSimbolo(lex)
        if lex.simbolo == 'begin':
            print('DEBUG: '+ lex.simbolo)
            getSimbolo(lex)
            CMS(lex)
            getSimbolo(lex)
            if lex.simbolo == 'end':
                print('>>>>>> Sucesso de compilação! <<<<<<<<')
            else:
                disparaErro('end')
        else:
            disparaErro('begin')
    elif lex.simbolo == 'begin': #NAO HOUVE VARIAVEIS
        getSimbolo(lex)
        CMS(lex)
        getSimbolo(lex)
        if lex.simbolo == 'end':
            print('>>>>>> Sucesso de compilação! <<<<<<<<')
        else:
            disparaErro('end')
    else:
        disparaErro('declaração de variavel ou começo de programa')



def sP(lex):
    getSimbolo(lex)
    print('SIMBOLO : ' + lex.simbolo)
    if(lex.simbolo == 'program'):
        getSimbolo(lex)
        if lex.tipo == 'VARIAVEL':
            getSimbolo(lex)
            C(lex)
        else:
            disparaErro('Nome de programa')
    else:
        disparaErro('program')


def getSimbolo(lex):
    simbolo = lex.Tokens[lex.pos]['termo']
    tipo = lex.Tokens[lex.pos]['tipo']
    lex.simbolo=simbolo
    lex.tipo=tipo
    lex.pos = lex.pos + 1



sP(lex)



print('DEBUG: ' + lex.simbolo)

#
# def REL()

#

#
# def FATOR():
#
# def OTERM():
#
# def OPAD():
#
# def MFATOR():
#
# def OPMUL():
#
# def PFALSA():
#
#
