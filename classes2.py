class Quarto:
    def _init_(self, numero, tipo, preco_por_noite):
        self.numero = numero
        self.tipo = tipo
        self.preco_por_noite = preco_por_noite

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

class EventoHotel:
    def _init_(self, nome, data, localizacao, detalhes):
        self.nome = nome
        self.data = data
        self.localizacao = localizacao
        self.detalhes = detalhes