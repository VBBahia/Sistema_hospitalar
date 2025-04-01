class Pacientes:
    def __init__(self, nome, idade, altura, peso, cpf, contato, estado_civil, alergia, motivo):
        self._nome = nome
        self._idade = idade
        self._altura = altura
        self._peso = peso
        self._cpf = cpf
        self._contato = contato
        self._estado_civil = estado_civil
        self._alergia = alergia
        self._motivo = motivo

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome
    
    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        self._idade = idade

    def get_altura(self):
        return self._altura

    def set_altura(self, altura):
        self._altura = altura
    
    def get_peso(self):
        return self._peso

    def set_peso(self, peso):
        self._peso = peso
    
    def get_cpf(self):
        return self._cpf

    def set_cpf(self, cpf):
        self._cpf = cpf
    
    def get_contato(self):
        return self._contato

    def set_contato(self, contato):
        self._contato = contato
    
    def get_estado_civil(self):
        return self._estado_civil

    def set_estado_civil(self, estado_civil):
        self._estado_civil = estado_civil

    def get_alergia(self):
        return self._alergia

    def set_alergia(self, alergia):
        self._alergia = alergia
    
    def get_motivo(self):
        return self._motivo

    def set_motivo(self, motivo):
        self._motivo = motivo


    def __str__(self):
        #Formatação de saida para o console
       return(f"NOME: {self._nome} \n"
            f"IDADE: {self._idade} \n"
            f"ALTURA: {self._altura} \n"
            f"CPF: {self._cpf} \n"
            f"CONTATO: {self._contato} \n"
            f"ESTADO CIVIL: {self._estado_civil} \n"
            f"ALERGIA: {self._alergia} \n"
            f"MOTIVO: {self._motivo} \n")

    def validador_dados(self):
        pass

class Pacientes_nome(Pacientes):
    @staticmethod
    def validar_nome(nome):
        return len(nome) <= 50 and not any(char.isdigit() for char in nome)

    def validador_dados(self):
        return Pacientes_nome.validar_nome(self.get_nome())

class Pacientes_idade(Pacientes):
    @staticmethod
    def validar_idade(idade):
        return idade > 0 or idade < 150

    def validador_dados(self):
        return Pacientes_idade.validar_idade(self.get_idade())

class Pacientes_altura(Pacientes):
    @staticmethod
    def validar_altura(altura):
        return altura > 0.0 and altura < 3.0

    def validador_dados(self):
        return Pacientes_altura.validar_altura(self.get_altura())

class Pacientes_peso(Pacientes):
    @staticmethod
    def validar_peso(peso):
        return peso > 0 and peso < 600

    def validador_dados(self):
        return Pacientes_peso.validar_peso(self.get_peso())

class Pacientes_cpf(Pacientes):
    @staticmethod
    def validar_cpf(cpf):
        cpf = '' .join(filter(str.isdigit, cpf)) #Ele vai remover todos os digitos númericos, e juntar o restante numa string só

        if len(cpf) != 11 or len(set(cpf)) == 1:
            return False

        def calcular_digito_verificador(cpf, peso):
            soma = sum(int(digito) * peso for digito, peso in zip(cpf,range(peso, 1, -1)))
            resto = soma % 11
            return 0 if resto < 2 else 11 - resto

        digito1 = calcular_digito_verificador(cpf[:9], 10)
        digito2 = calcular_digito_verificador(cpf[:10], 11)

        return int(cpf[9]) == digito1 and int(cpf[10]) == digito2

    def validador_dados(self):
        return Pacientes_cpf.validar_cpf(self.get_cpf())

class Pacientes_contato(Pacientes):
    @staticmethod
    def validar_contato(contato):
        return len(str(contato)) >= 8

    def validador_dados(self):
        return Pacientes_contato.validar_contato(self.get_contato())
