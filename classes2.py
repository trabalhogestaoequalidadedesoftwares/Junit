class Quarto:
    def _init_(self, numero, tipo, preco_por_noite):
        self.numero = numero
        self.tipo = tipo
        self.preco_por_noite = preco_por_noite
    def calcular_custo_estadia(self, numero_de_noites):
        return numero_de_noites * self.preco_por_noite

    def __str__(self):
        return f"Número do Quarto: {self.numero}, Tipo: {self.tipo}, Preço por Noite: {self.preco_por_noite}"

class Reserva:
    def _init_(self, checkin, checkout, cliente, quarto):
        self.checkin = checkin
        self.checkout = checkout
        self.cliente = cliente
        self.quarto = quarto

class Funcionario:
    def _init_(self, nome, cargo, numero_identificacao, salario):
        self.nome = nome
        self.cargo = cargo
        self.numero_identificacao = numero_identificacao
        self.salario = salario

class CheckOut:
    def _init_(self, data_hora, cliente, quarto):
        self.data_hora = data_hora
        self.cliente = cliente
        self.quarto = quarto   
    def __str__(self):
        return f"Data e Hora: {self.data_hora}, Cliente: {self.cliente}, Quarto: {self.quarto}"
    checkout_instance = CheckOut(data_hora, cliente, quarto)
    print(checkout_instance)


class ComentarioHotel:
    def _init_(self, cliente, data, classificacao, comentario):
        self.cliente = cliente
        self.data = data
        self.classificacao = classificacao
        self.comentario = comentario

class ServicoHotel:
    def _init_(self, nome, horarios_funcionamento, custo_adicional):
        self.nome = nome
        self.horarios_funcionamento = horarios_funcionamento
        self.custo_adicional = custo_adicional
    def calcular_custo_total(self, custo_base):
        return custo_base + self.custo_adicional

    def __str__(self):
        return f"Nome do Serviço: {self.nome}, Horários de Funcionamento: {self.horarios_funcionamento}, Custo Adicional: {self.custo_adicional}"

class EventoHotel:
    def _init_(self, nome, data, localizacao, detalhes):
        self.nome = nome
        self.data = data
        self.localizacao = localizacao
        self.detalhes = detalhes
