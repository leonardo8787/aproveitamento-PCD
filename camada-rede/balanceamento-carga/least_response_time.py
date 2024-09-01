import random

class LeastResponseTimeBalancer:
    def __init__(self, servers):
        self.servers = {server: random.uniform(0.5, 1.5) for server in servers}

    def get_next_server(self):
        server = min(self.servers, key=self.servers.get)
        self.servers[server] = self.get_response_time()
        return server

    def get_response_time(self):
        return random.uniform(0.5, 1.5)  # Simula o tempo de resposta

# Teste
servers = ["Server1", "Server2", "Server3"]
lrt_balancer = LeastResponseTimeBalancer(servers)

for _ in range(10):
    print(f"Server selected: {lrt_balancer.get_next_server()}")
