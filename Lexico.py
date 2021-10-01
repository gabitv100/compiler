
class Lex:
    Tokens = []
    termo = ''
    reservadas = ['program', 'real','integer','begin','read', 'if', 'then','write','else', 'end']
    pos= 0

    def __init__(self):
        self.termo = ''



    def disparaErro(c):
        print("TOKEN DESCONHECIDO:" + c)
        Lex.Tokens.append({'tipo': "Desconhecido", 'termo': c})
        termo=''


    def letra(c):
        return 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122

    def numero(c):
        return 48 <= ord(c) <= 57

    def ponto(c):
        return c == '.'

    def espaco(c):
        return c in [' ', '\n', '\t']

    def matematico(c):
        return c in['+','-','*','/']

    def logico(c):
        return c in['=','>','<','!']

    def fluxo(c):
        return c in ['(',')']





    @staticmethod
    def nextToken(self,estado, c):
        if estado == 0:
            if Lex.letra(c):
                estado = 2
                Lex.termo = Lex.termo + c
                return estado
            elif Lex.numero(c):
                estado = 1
                Lex.termo = Lex.termo + c
                return estado
            elif Lex.espaco(c):
                estado = 4

                return estado
            elif Lex.matematico(c):
                estado = 6
                Lex.Tokens.append({'tipo':"OPERADOR MATEMATICO", 'termo' : c})
                estado=0
                return estado
            elif Lex.logico(c):
                estado = 7

                Lex.termo = Lex.termo + c
                return estado
            elif Lex.fluxo(c):
                estado = 10
                Lex.Tokens.append({'tipo':"OPERADOR FLUXO",'termo': c})
                return 0
            else:
                Lex.disparaErro(c)
                return 0
        if (estado == 1):
            if (Lex.numero(c)):
                Lex.termo = Lex.termo + c
                estado = 1
                return estado
            elif (Lex.ponto(c)):
                estado = 3
                Lex.termo = Lex.termo + c
                return estado
            elif (Lex.letra(c)):
                Lex.disparaErro(c)
                return 0
            else:
                # estado 5
                Lex.Tokens.append({'tipo':"INTEIRO",'termo': Lex.termo})
                Lex.termo = ''
                return 0
        if estado == 2:
            if Lex.letra(c):
                estado == 2
                Lex.termo = Lex.termo + c
                return estado
            elif Lex.numero(c):
                estado == 2
                Lex.termo = Lex.termo + c
                return estado
            elif Lex.espaco(c):
                print('LEX: ' +  Lex.termo)
                if Lex.termo in Lex.reservadas:
                    Lex.Tokens.append({'tipo':"RESERVADA",'termo': Lex.termo})
                else:
                    Lex.Tokens.append({'tipo':"VARIAVEL",'termo': Lex.termo})
                # ["VARIAVEL"] = Lex.termo
                Lex.termo = ''
                return 0
            else:
                print('LEX: ' + Lex.termo)
                if Lex.termo in Lex.reservadas:
                    Lex.Tokens.append({'tipo': "RESERVADA", 'termo': Lex.termo})
                else:
                    Lex.Tokens.append({'tipo': "VARIAVEL", 'termo': Lex.termo})
                # ["VARIAVEL"] = Lex.termo
                Lex.termo = ''

                Lex.disparaErro(c) # SITUAÇÃO DE TOKEN DESCONHECIDO, COMO NAO CONTO POSICAO, ISTO EVITA USO DE UMA FUNÇÃO BACK()
                estado = 0
                return estado


        if estado == 3:
            if Lex.numero(c):
                estado = 3
                Lex.termo = Lex.termo + c
                return estado
            elif Lex.ponto(c):
                Lex.disparaErro(c)
                return 0
            else:
                Lex.Tokens.append({'tipo':"FLOAT",'termo':Lex.termo})
                Lex.termo = ''
                return 0
        if estado == 4:
            if Lex.letra(c):
                estado = 2
                Lex.termo = Lex.termo + c
                return estado
            elif Lex.numero(c):
                estado = 1
                Lex.termo = Lex.termo + c
                return estado
            elif Lex.espaco(c):
                estado = 4

                return estado
            elif Lex.matematico(c):
                estado = 6
                Lex.Tokens.append({'tipo': "OPERADOR MATEMATICO", 'termo': c})
                estado = 0
                return estado
            elif Lex.logico(c):
                estado = 7

                Lex.termo = Lex.termo + c
                return estado
            elif Lex.fluxo(c):
                estado = 10
                Lex.Tokens.append({'tipo': "OPERADOR FLUXO", 'termo': c})
                return 0
            else:
                Lex.disparaErro(c)
                return 0
        if estado == 7:
            if Lex.logico(c):
                Lex.termo = Lex.termo + c
                Lex.Tokens.append({'tipo':"LOGICO",'termo':Lex.termo})
                Lex.termo = ''
            elif Lex.espaco(c):
                if Lex.termo == '=':
                    estado = 8
                    Lex.Tokens.append({'tipo':"ATRIBUICAO", 'termo':Lex.termo})
                    Lex.termo = ''
                    return 0
                else:
                    Lex.Tokens.append({'tipo':"LOGICO",'termo':Lex.termo})
                    Lex.termo = ''
                    return 0






