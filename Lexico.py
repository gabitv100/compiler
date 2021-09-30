
#le arquivo



class Lex:
    Tokens = []
    termo = ''
    reservadas = ['program', 'real','integer','begin','read', 'if', 'then','write','else', 'end']

    def __init__(self):
        self.termo = ''



    def disparaErro(c):
        print("TOKEN DESCONHECIDO:" + c)
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
                print(estado)
                print(c)
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
                Lex.Tokens.append({"OPERADOR MATEMATICO": c})
                estado=0
                return estado
            elif Lex.logico(c):
                estado = 7

                Lex.termo = Lex.termo + c
                return estado
            elif Lex.fluxo(c):
                estado = 10
                Lex.Tokens.append({"OPERADOR FLUXO": c})
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
                Lex.Tokens.append({"INTEIRO": Lex.termo})
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
            else:
                print('LEX: ' +  Lex.termo)
                if Lex.termo in Lex.reservadas:
                    Lex.Tokens.append({"RESERVADA": Lex.termo})
                else:
                    Lex.Tokens.append({"VARIAVEL": Lex.termo})
                # ["VARIAVEL"] = Lex.termo
                Lex.termo = ''
                return 0
        if estado == 3:
            if Lex.numero(c):
                estado = 3
                Lex.termo = Lex.termo + c
                return estado
            elif Lex.ponto(c):
                Lex.disparaErro(c)
                return 0
            else:
                Lex.Tokens.append({"FLOAT": Lex.termo})
                Lex.termo = ''
                return 0
        if estado == 4:
            if Lex.letra(c):
                estado = 2
                print(estado)
                print(c)
                Lex.termo = Lex.termo + c
                return estado
            elif Lex.numero(c):
                estado = 1
                Lex.termo = Lex.termo + c
                return estado
            elif Lex.espaco(c):
                estado = 4
                return estado
            else:
                Lex.disparaErro(c)
                return 0
        if estado == 7:
            if Lex.logico(c):
                Lex.termo = Lex.termo + c
                Lex.Tokens.append({"LOGICO": Lex.termo})
                Lex.termo = ''
            elif Lex.espaco(c):
                if Lex.termo == '=':
                    estado = 8
                    Lex.Tokens.append({"ATRIBUICAO": Lex.termo})
                    Lex.termo = ''
                    return 0
                else:
                    Lex.Tokens.append({"LOGICO": Lex.termo})
                    Lex.termo = ''
                    return 0






