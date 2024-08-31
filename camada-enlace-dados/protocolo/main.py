import time
import random
import threading

class LinkLayerProtocol:
    def __init__(self, packet_loss_prob=0.1):
        self.packet_loss_prob = packet_loss_prob

    def send(self, data, receiver):
        """ Transmite o dado para o receptor com uma possível perda simulada """
        if random.random() > self.packet_loss_prob:
            print(f"Enviando pacote: {data}")
            receiver.receive(data)
            return True
        else:
            print(f"Pacote perdido: {data}")
            return False

    def receive(self, data):
        """ Recebe o pacote e envia uma confirmação (ACK) """
        print(f"Pacote recebido: {data}")
        self.send_ack(data)

    def send_ack(self, data):
        """ Envia uma confirmação (ACK) para o transmissor """
        print(f"Enviando ACK para: {data}")

class Sender:
    def __init__(self, protocol, max_retries=3, initial_window_size=2, timeout=1.0):
        self.protocol = protocol
        self.max_retries = max_retries
        self.window_size = initial_window_size
        self.timeout = timeout
        self.congestion_threshold = 4
        self.current_ack = -1
        self.lock = threading.Lock()

    def send_data(self, data):
        """ Envia pacotes com controle de janela deslizante e retransmissão """
        window_start = 0
        while window_start < len(data):
            window_end = min(window_start + self.window_size, len(data))
            threads = []
            for i in range(window_start, window_end):
                packet = data[i]
                t = threading.Thread(target=self.send_packet_with_retries, args=(packet, i))
                threads.append(t)
                t.start()

            for t in threads:
                t.join()

            with self.lock:
                window_start = self.current_ack + 1

            self.adjust_window_size()

    def send_packet_with_retries(self, packet, seq_number):
        """ Envia o pacote com várias tentativas em caso de perda e aguarda o ACK """
        attempt = 0
        while attempt < self.max_retries:
            success = self.protocol.send((seq_number, packet), receiver)
            if success:
                if self.wait_for_ack(seq_number):
                    return
            attempt += 1
            print(f"Tentativa {attempt} de {self.max_retries} falhou para {packet}. Retentando...")
        print(f"Falha ao enviar {packet} após {self.max_retries} tentativas.")

    def wait_for_ack(self, seq_number):
        """ Aguarda o ACK do receptor com um timeout """
        start_time = time.time()
        while time.time() - start_time < self.timeout:
            with self.lock:
                if self.current_ack >= seq_number:
                    return True
            time.sleep(0.1)
        print(f"Timeout ao esperar ACK para pacote {seq_number}")
        return False

    def adjust_window_size(self):
        """ Ajusta o tamanho da janela com base em uma simulação de controle de congestionamento """
        with self.lock:
            if self.window_size < self.congestion_threshold:
                self.window_size += 1
            else:
                self.window_size = max(2, self.window_size // 2)

class Receiver:
    def __init__(self, protocol):
        self.protocol = protocol
        self.expected_seq = 0
        self.buffer = {}

    def receive(self, data):
        seq_number, packet = data
        if seq_number == self.expected_seq:
            self.protocol.receive(packet)
            self.expected_seq += 1

            while self.expected_seq in self.buffer:
                buffered_packet = self.buffer.pop(self.expected_seq)
                self.protocol.receive(buffered_packet)
                self.expected_seq += 1

        elif seq_number > self.expected_seq:
            print(f"Pacote fora de ordem {packet}, armazenando no buffer.")
            self.buffer[seq_number] = packet

protocol = LinkLayerProtocol(packet_loss_prob=0.2)  # 20% de chance de perder pacotes

sender = Sender(protocol, max_retries=3, initial_window_size=2, timeout=1.0)
receiver = Receiver(protocol)

data_packets = ['Pacote1', 'Pacote2', 'Pacote3', 'Pacote4', 'Pacote5', 'Pacote6', 'Pacote7', 'Pacote8']

sender.send_data(data_packets)