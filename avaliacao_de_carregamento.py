from datetime import datetime, timedelta



class Formulario:
    def __init__(self, matricula_user, ponto_de_controle, numero_do_carro, matricula_do_motorista, hora_de_saida, hora_de_chegada, roleta_inicial, roleta_local, pessoas_em_pe):

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
                    "ida": ["6146D Rua 128 X Castelo", "6146E Rua 128 X Castelo - Via Barroco"],
                    "volta": ["6146D Castelo X Rua 128", "6146E Castelo X Rua 128 - Via Barroco"] 
                },

                "2590": {
                    "ida": ["2590R Ponta Negra x Castelo"],
                    "volta": ["2590R Castelo X Ponta Negra"],
                },
            },

            "niteroi": {
                "2144": {
                    "ida": ["2144R Maricá X Niterói"],
                    "volta": ["2144R Niterói X Maricá"]
                }, 

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
        self.numero_da_linha = "NÃO INFORMADO"
        self.numero_do_carro = numero_do_carro
        self.matricula_do_motorista = matricula_do_motorista
        self.hora_de_saida = hora_de_saida
        self.hora_de_chegada = hora_de_chegada
        self.tempo_viagem_total = self.calcular_tempo(hora_de_saida, hora_de_chegada)
        self.roleta_inicial = roleta_inicial
        self.roleta_local = roleta_local
        self.pessoas_em_pe = pessoas_em_pe
        self.carregamento_de_pessoas_no_onibus = self.validar_roletas(roleta_inicial, roleta_local)
        self.data_anotacao = self.definir_data_da_anotacao()
        self.hora_anotacao = self.definir_hora_da_anotacao()



    @property
    def matricula_user(self):
        return self.__matricula_user
    
    @matricula_user.setter
    def matricula_user(self, matricula_digitada):
        if isinstance(matricula_digitada, int) and matricula_digitada > 0:
            self.__matricula_user = matricula_digitada
            
        else:
            self.__matricula_user = "NÃO INFORMADA"
            print("Matrícula Inválida \n")
            raise ValueError("Matrícula Não encontrada")
    
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

    
    def definir_numero_da_linha(self):
            
            #esse if verifica todas as condições de IDA da estacao merces
            if self.ponto_de_controle == self.lista_pontos_de_controle[0]:
                print(f"{self.lista_pontos_de_controle[0]} Linhas")

                for chave, valor in enumerate(self.linhas["castelo"].keys(), start=1):
                    print(f"[{chave}] - {valor}")

                pergunta = int(input("\nEscolha uma das opções: ")) - 1 #passando o indice

                if pergunta == 0:
                    print("\n\nLinha escolhida: 2146 IDA\n")
                    for contador, linha in enumerate(self.linhas["castelo"]["2146"]["ida"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["castelo"]["2146"]["ida"][indice_da_lista_de_linhas]

                elif pergunta == 1:
                    print("\n\nLinha escolhida: 4146 IDA\n")
                    for contador, linha in enumerate(self.linhas["castelo"]["4146"]["ida"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["castelo"]["4146"]["ida"][indice_da_lista_de_linhas]

                elif pergunta == 2:
                    print("\n\nLinha escolhida: 6146 IDA\n")
                    for contador, linha in enumerate(self.linhas["castelo"]["6146"]["ida"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["castelo"]["6146"]["ida"][indice_da_lista_de_linhas]

                elif pergunta == 3:
                    print("\n\nLinha escolhida: 2590 IDA\n")
                    for contador, linha in enumerate(self.linhas["castelo"]["2590"]["ida"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["castelo"]["2590"]["ida"][indice_da_lista_de_linhas]

                else:
                    print("Inválido. \nEscolha um dígito válido")
                    raise ValueError()



            #esse if verifica todas as condições de VOLTA da estacao merces
            elif self.ponto_de_controle == self.lista_pontos_de_controle[2]: 
                print(f"{self.lista_pontos_de_controle[2]} Linhas \n")

                for chave, valor in enumerate(self.linhas["castelo"].keys(), start=1):
                    print(f"[{chave}] - {valor}")

                pergunta = int(input("\nEscolha uma das opções: ")) - 1 #passando o indice

                if pergunta == 0:
                    print("\n\nLinha escolhida: 2146 VOLTA\n")
                    for contador, linha in enumerate(self.linhas["castelo"]["2146"]["volta"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["castelo"]["2146"]["volta"][indice_da_lista_de_linhas]

                elif pergunta == 1:
                    print("\n\nLinha escolhida: 4146 VOLTA\n")
                    for contador, linha in enumerate(self.linhas["castelo"]["4146"]["volta"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["castelo"]["4146"]["volta"][indice_da_lista_de_linhas]

                elif pergunta == 2:
                    print("\n\nLinha escolhida: 6146 VOLTA\n")
                    for contador, linha in enumerate(self.linhas["castelo"]["6146"]["volta"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["castelo"]["6146"]["volta"][indice_da_lista_de_linhas]

                elif pergunta == 3:
                    print("\n\nLinha escolhida: 2590 VOLTA\n")
                    for contador, linha in enumerate(self.linhas["castelo"]["2590"]["volta"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["castelo"]["2590"]["volta"][indice_da_lista_de_linhas]
                else:
                    print("Inválido. \nEscolha um dígito válido")
                    raise ValueError()

            #esse if verifica todas as condições de IDA da estacao joao brasil
            elif self.ponto_de_controle == self.lista_pontos_de_controle[1]: 
                print(f"{self.lista_pontos_de_controle[1]} Linhas\n")

                for chave, valor in enumerate(self.linhas["niteroi"].keys(), start=1):
                    print(f"[{chave}] - {valor}")

                pergunta = int(input("\nEscolha uma das opções: ")) - 1 #passando o indice

                if pergunta == 0:
                    print("\n\nLinha escolhida: 2144 IDA\n")
                    for contador, linha in enumerate(self.linhas["niteroi"]["2144"]["ida"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["niteroi"]["2144"]["ida"][indice_da_lista_de_linhas]

                elif pergunta == 1:
                    print("\n\nLinha escolhida: 4144 IDA IDA\n")
                    for contador, linha in enumerate(self.linhas["niteroi"]["4144"]["ida"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["niteroi"]["4144"]["ida"][indice_da_lista_de_linhas]

                elif pergunta == 2:
                    print("\n\nLinha escolhida: 6144 IDA\n")
                    for contador, linha in enumerate(self.linhas["niteroi"]["6144"]["ida"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["niteroi"]["6144"]["ida"][indice_da_lista_de_linhas]
                
                elif pergunta == 3:
                    print("\n\nLinha escolhida: 534 IDA\n")
                    for contador, linha in enumerate(self.linhas["niteroi"]["534"]["ida"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["niteroi"]["534"]["ida"][indice_da_lista_de_linhas]

                else:
                    print("Inválido. \nEscolha um dígito válido")
                    raise ValueError()
            
            #esse if verifica todas as condições de VOLTA da estacao joao brasil
            elif self.ponto_de_controle == self.lista_pontos_de_controle[3]: #estacao VOLTA
                print("Estação João Brasil VOLTA\n")

                for chave, valor in enumerate(self.linhas["niteroi"].keys(), start=1):
                    print(f"[{chave}] - {valor}")

                pergunta = int(input("\nEscolha uma das opções: ")) - 1 #passando o indice

                if pergunta == 0:
                    print("\n\nLinha escolhida: 2144 VOLTA\n")
                    for contador, linha in enumerate(self.linhas["niteroi"]["2144"]["volta"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["niteroi"]["2144"]["volta"][indice_da_lista_de_linhas]

                elif pergunta == 1:
                    print("\n\nLinha escolhida: 4144 VOLTA\n")
                    for contador, linha in enumerate(self.linhas["niteroi"]["4144"]["volta"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["niteroi"]["4144"]["volta"][indice_da_lista_de_linhas]

                elif pergunta == 2:
                    print("\n\nLinha escolhida: 6144 VOLTA\n")
                    for contador, linha in enumerate(self.linhas["niteroi"]["6144"]["volta"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["niteroi"]["6144"]["volta"][indice_da_lista_de_linhas]

                elif pergunta == 3:
                    print("\n\nLinha escolhida: 534 VOLTA\n")
                    for contador, linha in enumerate(self.linhas["niteroi"]["534"]["volta"], start=1):
                        print(f"[{contador}] - {linha}")
                    
                    indice_da_lista_de_linhas = int(input("\nEscolha a linha: ")) - 1
                    self.numero_da_linha = self.linhas["niteroi"]["534"]["volta"][indice_da_lista_de_linhas]

                else:
                    print("Inválido. \nEscolha um dígito válido")
                    raise ValueError()

            else:
                print("Inválido.")
                raise ValueError()

    @property
    def numero_do_carro(self):
        return self._numero_do_carro

    @numero_do_carro.setter
    def numero_do_carro(self, numero_do_carro_digitado):
        if isinstance(numero_do_carro_digitado, int) and numero_do_carro_digitado > 0:
            self._numero_do_carro = numero_do_carro_digitado
        else:
            print("Numero do carro Inválido. \nDigite novamente")
            raise ValueError("Numero do carro Inválido.")
    

    @property
    def matricula_do_motorista(self):
        return self._matricula_do_motorista
    
    @matricula_do_motorista.setter
    def matricula_do_motorista(self, matricula_digitada):
        if isinstance(matricula_digitada, int) and matricula_digitada > 0:
            self._matricula_do_motorista = matricula_digitada
            
        else:
            self._matricula_do_motorista = "NÃO INFORMADA"
            print("Matrícula Inválida \n")
            raise ValueError("Matrícula Não encontrada")
        
    @property 
    def roleta_inicial(self):
        return self._roleta_inicial
    
    @roleta_inicial.setter
    def roleta_inicial(self, roleta_digitada):
        if isinstance(roleta_digitada, int) and roleta_digitada >= 0 and roleta_digitada < 99999:
            self._roleta_inicial = roleta_digitada
        else:
            self._roleta_inicial = "NÃO INFORMADO"
            raise ValueError("Roleta Errada")
        
    @property
    def roleta_local(self):
        return self._roleta_local
    
    @roleta_local.setter
    def roleta_local(self, roleta_digitada):
        if isinstance(roleta_digitada, int) and roleta_digitada >= 0 and roleta_digitada < 99999:
            self._roleta_local = roleta_digitada
            self._roleta_local = roleta_digitada
        else:
            self._roleta_inicial = "NÃO INFORMADO"
            raise ValueError("Roleta Errada")
    

    def definir_hora_da_anotacao(self):
        hora_atual = datetime.now()
        self.hora_anotacao = f"{hora_atual.strftime('%H:%M:%S')}"
        return self.hora_anotacao

    def definir_data_da_anotacao(self):
        hora_atual = datetime.now()
        self.data_anotacao = f"{hora_atual.strftime('%d/%m/%Y')}"
        return self.data_anotacao


    def tratar_horarios(self, horario_str):
        limpo = str(horario_str).replace(":", "").strip()
        formato_completo = limpo.zfill(4)
        return datetime.strptime(formato_completo, "%H%M")


    def calcular_tempo(self, horario_inicial, horario_final):
        try:
            inicio = self.tratar_horarios(horario_inicial)
            fim = self.tratar_horarios(horario_final)
            
            diferenca = fim - inicio
            if diferenca.days < 0:
                diferenca = timedelta(days=1) + diferenca
                
            self.tempo_viagem_total = str(diferenca)
            return self.tempo_viagem_total
        except ValueError:
            return "Erro: Formato de hora inválido"
        
    def validar_roletas(self, roleta_inicial, roleta_local):
        if self.roleta_inicial < self.roleta_local:
            total_de_pessoas_no_onibus = roleta_local - roleta_inicial
            return total_de_pessoas_no_onibus

        elif self.roleta_inicial == self.roleta_local:
            print(f"ROLETAS IDÊNTICAS\n\nInicial: {self.roleta_inicial}\nLocal: {self.roleta_local}\n")

            pergunta = str(input("Você deseja que as roletas sejam excluidas?[s/n]: ")).strip().lower()
            if pergunta == 's':
                self.roleta_inicial = 0
                self.roleta_local = 0

            elif pergunta == 'n':
                print("Refaça o formulário...")
                raise ValueError("Erro de digitação, Refaça o formulário")
            
            else:
                print("Digite s ou n [ex: s]: ")
                raise ValueError("Opção Inválida")
        else:
            print("A roleta inicial não pode ser maior que a local")
            raise ValueError("Roleta inicial menor que a roleta local")
        
    @property
    def pessoas_em_pe(self):
        return self._pessoas_em_pe
    
    @pessoas_em_pe.setter
    def pessoas_em_pe(self, pessoas_em_pe_digitada):
        if isinstance(pessoas_em_pe_digitada, int) and pessoas_em_pe_digitada >= 0:
            self._pessoas_em_pe = pessoas_em_pe_digitada
            
        else:
            self._pessoas_em_pe = "NÃO INFORMADO"
            print("Insira um valor válido")
            raise ValueError("Erro de valor")
    
    def exibir_relatorio(self):
        print("\n" + "="*75)
        print(f"{'VIAÇÃO NOSSA SENHORA DO AMPARO':^75}")
        print(f"{'RELATÓRIO DE CARREGAMENTO':^75}")
        print("="*75)
        
        print(f"| DATA: {self.data_anotacao:<15} | HORA REGISTRO: {self.hora_anotacao:<10} |")
        print(f"| MATRÍCULA USUÁRIO: {self.matricula_user:<10} | MATRÍCULA MOTORISTA: {self.matricula_do_motorista:<8} |")
        print(f"| NÚMERO DO CARRO: {self.numero_do_carro:<52} |")
        print("-" * 75)
        
        print(f"  PONTO DE CONTROLE: {self.ponto_de_controle}")
        print(f"  LINHA SELECIONADA: {self.numero_da_linha}")
        print(f"  HORÁRIO: Saída {self.hora_de_saida} -> Chegada {self.hora_de_chegada}")
        print(f"  TEMPO TOTAL DE VIAGEM: {self.tempo_viagem_total}")
        print("-" * 75)

        print(f"  ROLETA INICIAL: {self.roleta_inicial:<15} ROLETA LOCAL: {self.roleta_local}")
        print(f"  PASSAGEIROS (GIRO): {self.carregamento_de_pessoas_no_onibus:<11} PESSOAS EM PÉ: {self.pessoas_em_pe}")

        total_viagem = self.carregamento_de_pessoas_no_onibus + (self.pessoas_em_pe if isinstance(self.pessoas_em_pe, int) else 0)
        print(f"  CARREGAMENTO TOTAL NO PONTO: {total_viagem}")
        
        print("="*75 + "\n")




while True:
    try:
        print("\n" + 75 * "=")
        print(20 * " ", "Viação Nossa Senhora do Amparo", 20 * " ")
        print(75 * "=" + "\n")

        matricula_user = int(input("Sua matrícula: "))
        print("\n[1] - ESTAÇÃO N.S. MERCÊS (RIO)")
        print("[2] - ESTAÇÃO JOÃO BRASIL (NIT)")
        print("[3] - ESTAÇÃO N.S. MERCÊS (VOLTA)")
        print("[4] - ESTAÇÃO JOÃO BRASIL (VOLTA)")
        ponto_de_controle = int(input("\nDigite o número do seu ponto de controle: ")) - 1
        carro = int(input("Número do carro: "))
        matricula_do_motorista = int(input("Matrícula do motorista: "))
        horario_saida = input("Hora de saída (HH:MM): ")
        horario_chegada = input("Hora de chegada (HH:MM): ")
        roleta_inicial = int(input("Roleta Inicial: "))
        roleta_local = int(input("Roleta Local: "))
        pessoas_em_pe = int(input("Pessoas em pé: "))
        user1 = Formulario(matricula_user, ponto_de_controle, carro, matricula_do_motorista, horario_saida, horario_chegada, roleta_inicial, roleta_local, pessoas_em_pe)
        print("\n")

        user1.definir_numero_da_linha()

        user1.exibir_relatorio()
        break

    except ValueError as e:
        print(f"\n[ERRO]: {e}")
        print("Tente preencher o formulário novamente...\n")
    
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")
