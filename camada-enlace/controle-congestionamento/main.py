import random
import time

class CongestionControl:
    def __init__(self, max_window_size):
        self.window_size = 1  # Tamanho inicial da janela
        self.max_window_size = max_window_size  # Tamanho máximo da janela
        self.ssthresh = max_window_size / 2  # Limiar de transição para a fase de congestionamento
        self.state = 'slow_start'  # Estado inicial
        self.data_sent = 0  # Dados enviados
        self.data_acked = 0  # Dados confirmados
    
    def send_data(self):
        # Simula o envio de dados com base na janela de congestionamento
        print(f"Enviando {self.window_size} pacotes")
        self.data_sent += self.window_size
    
    def receive_ack(self):
        # Simula o recebimento de uma confirmação de pacotes
        acks = random.randint(1, self.window_size)
        self.data_acked += acks
        print(f"Recebido {acks} confirmações")
    
    def adjust_window(self):
        # Ajusta o tamanho da janela com base no estado e confirmações recebidas
        if self.state == 'slow_start':
            if self.data_acked >= self.window_size:
                self.window_size = min(self.window_size * 2, self.max_window_size)
                self.data_acked = 0
                if self.window_size >= self.ssthresh:
                    self.state = 'congestion_avoidance'
                print(f"Janela aumentada para {self.window_size} (slow start)")
            else:
                print("Aguardando confirmações suficientes")
        elif self.state == 'congestion_avoidance':
            if self.data_acked >= self.window_size:
                self.window_size += 1
                self.data_acked = 0
                print(f"Janela aumentada para {self.window_size} (congestion avoidance)")
    
    def simulate(self, rounds):
        for _ in range(rounds):
            self.send_data()
            self.receive_ack()
            self.adjust_window()
            time.sleep(1)  # Simula o tempo de rede

# Parâmetros do controle de congestionamento
max_window_size = 16
congestion_control = CongestionControl(max_window_size)

# Simular o controle de congestionamento
congestion_control.simulate(rounds=10)
