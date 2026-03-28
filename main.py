class Formulario:
    def __init__(self, matricula_user, ponto_de_controle, numero_da_linha, numero_do_carro, matricula_do_motorista, hora_de_saida, hora_de_chegada, roleta_inicial, roleta_local, pessoas_em_pe):

        self.lista_pontos_de_controle = ("ESTAÇÃO N.S. MERCÊS (RIO)", "ESTAÇÃO JOÃO BRASIL (NIT)", "ESTAÇÃO N.S. MERCÊS (VOLTA)", "ESTAÇÃO JOÃO BRASIL (VOLTA)")

        self.linhas = {
            "castelo": ("2146D","4146D","6146D","2590R"),
            "niteroi": ("2144R","4144R")
        }


        self.matricula_user = matricula_user
        self.ponto_de_controle = ponto_de_controle
        self.numero_da_linha = numero_da_linha
        self.numero_do_carro = numero_do_carro
        self.matricula_do_motorista = matricula_do_motorista
        self.hora_de_saida = hora_de_saida
        self.hora_de_chegada = hora_de_chegada
        self.tempo_viagem_total = 0
        self.roleta_inicial = roleta_inicial
        self.roleta_local = roleta_local
        self.pessoas_em_pe = pessoas_em_pe
        self.carregamento_de_pessoas_no_onibus = 0
        self.data_anotacao = 0
        self.hora_anotacao = 0



    @property
    def matricula_user(self):
        return self.__matricula_user
    
    @matricula_user.setter
    def matricula_user(self, matricula_digitada):
        if isinstance(matricula_digitada, int) and matricula_digitada > 0:
            self.__matricula_user = matricula_digitada
            print("Matricula Validada")
            
        else:
            self.__matricula_user = 0
            print("Matrícula Inválida")
    
    @property
    def ponto_de_controle(self):
        return self._ponto_de_controle
    
    @ponto_de_controle.setter
    def ponto_de_controle(self, posicao_lista_ponto_de_controle):

        if isinstance(posicao_lista_ponto_de_controle, int) and 0 <= posicao_lista_ponto_de_controle < len(self.lista_pontos_de_controle):

            if posicao_lista_ponto_de_controle == 0:
                self._ponto_de_controle = self.lista_pontos_de_controle[0]

            elif posicao_lista_ponto_de_controle == 1:
                self._ponto_de_controle = self.lista_pontos_de_controle[1]

            elif posicao_lista_ponto_de_controle == 2:
                self._ponto_de_controle = self.lista_pontos_de_controle[2]

            elif posicao_lista_ponto_de_controle == 3:
                self._ponto_de_controle = self.lista_pontos_de_controle[3]

            else:
                pass
        else:
            print("Insira um valor válido")
            self._ponto_de_controle = "NÃO INFORMADO"

            raise ValueError()
        
    @property
    def numero_da_linha(self):
        return self._numero_da_linha
    
    @numero_da_linha
    def numero_da_linha(self, posicao_lista_numero_da_linha):
        
        
    
            


matricula_user = 123
ponto_de_controle = 4 #passa a posicao da lista
numero_da_linha = 1 #2146D
numero_do_carro = 294
matricula_do_motorista = 5436
hora_de_saida = "9:00"
hora_de_chegada = "10:20"
roleta_inicial = 59000
roleta_local = 59030
pessoas_em_pe = 0


user1 = Formulario(matricula_user, ponto_de_controle, numero_da_linha, numero_do_carro, matricula_do_motorista, hora_de_saida, hora_de_chegada, roleta_inicial, roleta_local, pessoas_em_pe)


print(user1.ponto_de_controle)
