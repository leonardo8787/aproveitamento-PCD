class RoundRobinBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_next_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

# Teste
servers = ["Server1", "Server2", "Server3"]
rr_balancer = RoundRobinBalancer(servers)

for _ in range(10):
    print(f"Server selected: {rr_balancer.get_next_server()}")
