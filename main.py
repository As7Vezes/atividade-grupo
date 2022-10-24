grauUrgencia = input("Qual o seu grau de urgência? ")

if grauUrgencia.lower() == "urgência" or grauUrgencia.lower() == "urgencia":
        print("Iremos te acompanhar para a sala de urgência, por favor quando possível nos fornecer seus dados pessoais.")
        print("Por favor insira seus dados pessoais.")
        nome = input("Por favor insira seu nome: ")
        idade = input("Por favor insira sua idade: ")
        genero = input("Por favor insira seu genero: ")
        
if grauUrgencia.lower() == "leve" or grauUrgencia.lower() == "moderado":
    agendamento = input("Possui agendamento? ")
    
    if agendamento.lower() == "sim":
        print("Por favor se dirija as salas 1,2,4 ou 5")
    if agendamento.lower() == "não":
        
        print("Por favor reliza o processo de triagem")
        atendimento = input("Será atendido no mesmo dia? ")
        if atendimento.lower() == "sim": 
            print("Se dirija a sala de espera")
            prioridade = input("O paciente é gestante ou PCD? ")
            if prioridade.lower() == "sim":
                print("Por favor se digija a sala de atendimento prioritário 4 ou 5")
            if prioridade.lower() == "não":
                faixaEtaria = input("Insira o código da sua faixa Etária 1: Criaças ou recem nascidos; 2: Adultos; 3: Idosos; ")
                if int(faixaEtaria) == 1:
                    print("Por favor se dirija para a sala 1 de pediatria.")
                if int(faixaEtaria) == 2:
                    print("Por favor se dirija para a sala 2")
                if int(faixaEtaria) == 3:
                        print("Por favor se dirija para a sala de prioridade 3")
                    
        if atendimento.lower() == "não":    
            print("Realizar agendamento na recpeção.")
            
        
        