from datetime import datetime

class Horariomarcado:
    def __init__(self, data, hora, servico):
        self.data = data
        self.hora = hora
        self.servico = servico

    def marcarhorario(self):
        try:
            data_hora_str = f'{self.data} {self.hora}'
            marcandohorario = datetime.strptime(data_hora_str, '%d-%m-%Y %H:%M')
            nome_servico = self.bananadepijama()
            return f'O serviço "{nome_servico}" foi marcado para: {marcandohorario.strftime("%d-%m-%Y %H:%M")}'

        except ValueError:
            print('Formato inválido, por favor entre com dia, mês, ano. Seguido com as horas e minutos')
            return None
        
    def bananadepijama(self):
        if self.servico == '1':
            return 'agendar limpeza'
        elif self.servico == '2':
            return 'aplicação de inseticida'
        else:
            return 'Opção inválida'
        
        
