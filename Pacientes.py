from Main import (Pacientes, Pacientes_nome, Pacientes_idade, Pacientes_peso,
                       Pacientes_altura, Pacientes_cpf, Pacientes_contato)

import csv

class Pacientes:
    while True:
        nome = input("Informe o seu nome: ")
        if not Pacientes_nome.validar_nome(nome):
            print("Nome invalido. Tente novamente.")
            continue
        while True:
            try:
                idade = int(input("Informe a sua idade: "))
                if not Pacientes_idade.validar_idade(idade):
                    print("Idade invalida. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Incluir apenas números")
                continue

        while True:
            try:
                altura = float(input("Informe a sua altura: "))
                if not Pacientes_altura.validar_altura(altura):
                    print("Altura invalida. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Incluir apenas números")
                continue

        while True:
            try:
                peso = float(input("Informe o seu peso: "))
                if not Pacientes_peso.validar_peso(peso):
                    print("Peso invalido. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Incluir apenas números")
                continue

        cpf = ""
        while True:
            cpf = input("Informe o seu CPF: ")
            valido = Pacientes_cpf.validar_cpf(cpf)
            if valido:
                break
            else:
                print("CPF invalido. Tente novamente")

        while True:
            try:
                contato = int(input("Informe o seu número para contato: "))
                if not Pacientes_contato.validar_contato(contato):
                    print("Contato invalido. Tente novamente")
                    continue
                break
            except ValueError:
                print("Incluir apenas números")
                continue


            estado_civil = input("Informe o seu Estado Civil: ")
            motivo = input("Qual o motivo que o levou a vir ao hospital? ")


        while True:
            alergia = input("Possui alguma alergia (sim) ou (não): ")
            if alergia.lower() == "sim":
                alergia = input("Informe a que tem alergia: ")
            else:
                alergia = "Nenhuma"
                continue


        paciente = Pacientes(nome, idade, altura, peso, cpf, contato, estado_civil, motivo, alergia)

        if not paciente.validador_dados():
            print("Dados invalidos. Tente novamente")
            continue

        with open('dadosPacientes.csv', 'a', newline='') as dados_paciente:
            writer = csv.writer(dados_paciente)
            writer.writerow([paciente.nome, paciente.idade, paciente.altura, paciente.cpf, paciente.contato,
                             paciente.estado_civil, paciente.alergia, paciente.motivo])

        print("\n")

        escolha = input("Deseja adicionar mais um paciente (sim) ou (não)? ")

        if escolha.lower() != 'sim':
            print("Obrigado pelas informações, garanto que os seu dados estaram protegidos, BY!!!")
            break
