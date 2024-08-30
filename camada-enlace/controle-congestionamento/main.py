import random
import time

class CongestionControl:
    def __init__(self, max_window_size):
        self.window_size = 1 
        self.max_window_size = max_window_size 
        self.ssthresh = max_window_size / 2 
        self.state = 'slow_start' 
        self.data_sent = 0
        self.data_acked = 0 
    
    def send_data(self):

        print(f"Enviando {self.window_size} pacotes")
        self.data_sent += self.window_size
    
    def receive_ack(self):
        acks = random.randint(1, self.window_size)
        self.data_acked += acks
        print(f"Recebido {acks} confirmações")
    
    def adjust_window(self):
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
            time.sleep(1)  

max_window_size = 16
congestion_control = CongestionControl(max_window_size)

congestion_control.simulate(rounds=10)
