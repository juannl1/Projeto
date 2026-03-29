class Formulario:
    def __init__(self, matricula_user, ponto_de_controle, numero_da_linha, numero_do_carro, matricula_do_motorista, hora_de_saida, hora_de_chegada, roleta_inicial, roleta_local, pessoas_em_pe):

        self.lista_pontos_de_controle = ("ESTAÇÃO N.S. MERCÊS (RIO)", "ESTAÇÃO JOÃO BRASIL (NIT)", "ESTAÇÃO N.S. MERCÊS (VOLTA)", "ESTAÇÃO JOÃO BRASIL (VOLTA)")

        self.linhas = {
            "castelo": {
                "2146": {
                    "ida": ["2146D Maricá X Castelo", "2146M Garagem Rio do Ouro X Castelo"],
                    "volta": ["2146D Castelo X Maricá", "2146M Castelo X Maricá"]
                },

                "4146": {
                    "ida": ["4146D Recanto x Castelo", "4146T Terminal Itaipuaçu X Castelo", "4146B Recanto X Castelo - via Vivendas", "4146G Terminal Itaipuaçu X Castelo"],
                    "volta": ["4146D Castelo X Recanto", "4146T Castelo X Terminal de Itaipuaçu", "4146B Castelo X Recanto - via Vivendas", "4146G Castelo X Terminal Itaipuaçu - via Vivendas"]
                },

                "6146": {
                    "ida": ["Rua 128 X Castelo", "6146E Rua 128 X Castelo - Via Barroco"],

                    "volta": ["6146D Castelo X Rua 128", "6146E Castelo X Rua 128 - Via Barroco"] 
                    
                },

                "2590": {
                    "ida": ["2590R Ponta Negra x Castelo"],
                    "volta": ["2590R Castelo X Ponta Negra"],
                },
            },

            "niteroi": {
                "4144": {
                    "ida": ["4144R Recanto x Niterói", "4144T Terminal Itaipuaçu X Niterói", "4144C Recanto X Niterói - via Vivendas", "4144S  Terminal Itaipuaçu X Niterói - via Vivendas"],
                    "volta": ["4144D Niterói X Recanto", "4144T Niterói X Terminal de Itaipuaçu", "4144B Niterói X Recanto - via Vivendas", "4144G Niterói X Recanto - via Vivendas"]
                },

                "6144": {
                    "ida": ["6144R Rua 128 X Niterói - via Barroco"],
                    "volta": ["6144U Rua 128 X Niterói - via Cajueiros"]
                },

                "534": {
                    "ida": ["534A Jaconé X Niterói"],
                    "volta": ["534A Niterói X Jaconé"]
                }
            }
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
            print("Matricula Validada \n")
            
        else:
            self.__matricula_user = 0
            print("Matrícula Inválida \n")
    
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
    
    @numero_da_linha.setter
    def numero_da_linha(self, posicao_lista_numero_da_linha):
        if isinstance(posicao_lista_numero_da_linha, int):
            if self.ponto_de_controle == self.lista_pontos_de_controle[0]:
                self._numero_da_linha = self.linhas["castelo"]["2146"]["ida"][posicao_lista_numero_da_linha]
                print(f"Linha de ônibus salva [{self.numero_da_linha}]")




            elif self.ponto_de_controle == self.lista_pontos_de_controle[2]:
                self._numero_da_linha = self.linhas["castelo"]["2146"]["volta"][posicao_lista_numero_da_linha]
                print(f"Linha de ônibus salva [{self.numero_da_linha}]")

        
            elif self.ponto_de_controle == self.lista_pontos_de_controle[1]:

                self._numero_da_linha = self.linhas["niteroi"]["2144"]["ida"][posicao_lista_numero_da_linha]

                print(f"Linha de ônibus salva [{self.numero_da_linha}]")
            
            elif self.ponto_de_controle == self.lista_pontos_de_controle[3]:
                self._numero_da_linha = self.linhas["niteroi"]["2144"]["volta"][posicao_lista_numero_da_linha]
                print(f"Linha de ônibus salva [{self.numero_da_linha}]")

        else:
            self._numero_da_linha = "NÃO INFORMADO"
            ValueError()


            
        
    
            


matricula_user = 123
ponto_de_controle = 0 #passa a posicao da lista
numero_da_linha = 0 #2146D passa a posicao na lista
numero_do_carro = 294
matricula_do_motorista = 5436
hora_de_saida = "9:00"
hora_de_chegada = "10:20"
roleta_inicial = 59000
roleta_local = 59030
pessoas_em_pe = 0


user1 = Formulario(matricula_user, ponto_de_controle, numero_da_linha, numero_do_carro, matricula_do_motorista, hora_de_saida, hora_de_chegada, roleta_inicial, roleta_local, pessoas_em_pe)


print(user1.ponto_de_controle)
print(user1.numero_da_linha)
