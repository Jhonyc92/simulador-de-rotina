print()

# Define uma classe chamada "Pessoa"
class Pessoa:
    
    # O construtor da classe, inicializa um novo objeto Pessoa com o nome fornecido
    def __init__(self, nome):
        
        # Define o nome da pessoa como o nome fornecido
        self.nome = nome
        
        # Inicialmente define o estado "acordado" como Falso
        self.acordado = False
        
        # Inicialmente define o estado "comendo" como Falso
        self.comendo = False
        
        # Inicialmente define o estado "dirigindo" como Falso
    self.dirigindo = False
        
    # Método para fazer a pessoa acordar
    def acordar(self):
        
        # Verifica se a pessoa já está acordada
        if self.acordado:
            
            # Se sim, imprime que a pessoa já está acordada
            print(f"{self.nome} já estava acordado")
            
        else: 
            
            # Se não, muda o estado "acordado" para Verdadeiro
            self.acordado = True           
            
            # E imprime que a pessoa acordou
            print(f"{self.nome} acordou")
            
    # Método para fazer a pessoa comer
    def comer(self):
        
        # Verifica se a pessoa está acordada
        if self.acordado:
            
            # Verifica se a pessoa já está comendo
            if self.comendo:
                
                # Se sim, imprime que a pessoa já está comendo
                print(f"{self.nome} já estava comendo")
                
            # Verifica se a pessoa está dirigindo
            elif self.dirigindo:
                
                # Se sim, imprime que não pode comer enquanto dirige
                print(f"{self.nome} não pode comer enquanto está dirigindo")
                
            else: 
                
                # Se todas as condições acima não forem verdadeiras, então a pessoa pode comer
                self.comendo = True
                
                # Imprime que a pessoa começou a comer
                print(f"{self.nome} começou a comer")
                
        # Verifica se a pessoa está dormindo
        else:
            
            # Se sim, imprime que não pode comer enquanto dorme
            print(f"{self.nome} não pode comer enquanto está dormindo")
            
    # Método para fazer a pessoa parar de comer
    def parar_de_comer(self):
        
        if self.acordado:
            
            # Verifica se a pessoa não está comendo
            if not self.comendo:
                
                # Se sim, imprime que a pessoa não estava comendo
                print(f"{self.nome} não estava comendo")
                
            else:
                
                # Se a pessoa estiver comendo, então ela pode parar de comer
                self.comendo = False
                
                # Imprime que a pessoa parou de comer
                print(f"{self.nome} parou de comer")
                
        else:
            
            print(f"{self.nome} está dormindo")
            
    # Método para fazer a pessoa dirigir
    def dirigir(self):
        
        # Verifica se a pessoa está acordada
        if self.acordado:
            
            # Verifica se a pessoa já está dirigindo
            if self.dirigindo:
                
                # Se sim, imprime que a pessoa já estava dirigindo
                print(f"{self.nome} já estava dirigindo")
                
            # Verifica se a pessoa está comendo
            elif self.comendo:
                
                # Se sim, imprime que não deve dirigir enquanto come
                print(f"{self.nome} não pode dirigir enquanto está comendo")
                
            else:
                
                # Se nenhuma das condições acima for verdadeira, a pessoa pode dirigir
                self.dirigindo = True
                
                # Imprime que a pessoa começou a dirigir
                print(f"{self.nome} começou a dirigir")
                
        # Verifica se a pessoa está dormindo
        else:
            
            # Se sim, imprime que não pode dirigir
            print(f"{self.nome} não pode dirigir enquanto está dormindo")
            
    # Método para fazer a pessoa parar de dirigir
    def parar_de_dirigir(self):
        
        if self.acordado:
            
            # Verifica se a pessoa não está dirigindo
            if not self.dirigindo:
                
                # Se sim, imprime que a pessoa não está dirigindo
                print(f"{self.nome} não estava dirigindo")
                
            else:
                
                # Se a pessoa estiver dirigindo, então ela pode parar
                self.dirigindo = False
                
                # Imprime que a pessoa parou de dirigir
                print(f"{self.nome} parou de dirigir")
                
        else:
            
            print(f"{self.nome} está dormindo")
            
    # Método para fazer a pessoa dormir
    def dormir(self):
        
        if self.acordado:
            
            # Verifica se a pessoa está comendo
            if self.comendo:
                
                # Se sim, imprime que não pode dormir enquanto come
                print(f"{self.nome} não pode dormir enquanto está comendo")
                
            # Verifica se a pessoa está dirigindo
            elif self.dirigindo:
                
                # Se sim, imprime que não pode dormir enquanto dirige
                print(f"{self.nome} não pode dormir enquanto está dirigindo")
                
            # Se nenhuma das condições acima for verdadeira, a pessoa pode dormir
            else:
                
                # Define o estado "acordado" como Falso
                self.acordado = False
                
                # Imprime que a pessoa dormiu
                print(f"{self.nome} dormiu")
                
        # Verifica se a pessoa já estava dormindo
        else: 
            
            # Se sim, imprime que a pessoa já está dormindo
            print(f"{self.nome} já estava dormindo")

print("Simulando a Rotina de uma Pessoa")

# Pede ao Usuário para escolher um Nome
nome = input("Insira o nome: ")

# Criando um objeto "nome" da classe "Pessoa" e passando "nome" como nome para o construtor
nome = Pessoa(nome)

# Enquanto o Usuário não escolher Sair, o loop irá rodar de forma infinita
while True:
    
    print()
    
    # Menu interativo do Programa
    print("Menu")
    
    print()
    
    print("1 - Acordar")
    
    print("2 - Comer")
    
    print("3 - Dirigir")
    
    print("4 - Parar de comer")
    
    print("5 - Parar de dirigir")
    
    print("6 - Dormir")
    
    print("7 - Sair")
    
    print()
    
    # Pede ao Usuário para escolher a ação desejada
    op = input("Escolha a opção (1~7): ")
    
    print()
    
    # Opção para fazer a Pessoa Acordar
    if op == "1":
        
        # Ação de Acordar é executada
        nome.acordar()
        
    # Opção para fazer a Pessoa Comer
    elif op == "2":
                
        # Ação de Comer é executada
        nome.comer()
        
    # Opção para fazer a Pessoa Dirigir
    elif op == "3":
        
        # Ação de Dirigir é executada
        nome.dirigir()
        
    # Opção para fazer a Pessoa Parar de Comer
    elif op == "4":
        
        # Ação de Parar de Comer é executada
        nome.parar_de_comer()
        
    # Opção para fazer a Pessoa Parar de Dirigir
    elif op == "5":
        
        # Ação de Parar de Dirigir é executada
        nome.parar_de_dirigir()
        
    # Opção para fazer a Pessoa Dormir
    elif op == "6":
        
        # Ação de Dormir é executada
        nome.dormir()
        
    # Opção para Encerrar o Programa
    elif op== "7":
        
        # Informa que o Programa está encerrando
        print("Encerrando...")
        
        # Encerra o looping infinito do while True
        break
        
    # Caso seja digitada um valor diferente de 1 a 7
    else:

        # Imprime uma Mensagem informando que o Usuário digitou uma Opção Inválida
        print(f"Opção Inválida! Insira um número de 1 a 7")
