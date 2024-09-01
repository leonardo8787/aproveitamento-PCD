class LeastConnectionsBalancer:
    def __init__(self, servers):
        self.servers = {server: 0 for server in servers}

    def get_next_server(self):
        server = min(self.servers, key=self.servers.get)
        self.servers[server] += 1
        return server

    def release_connection(self, server):
        if server in self.servers:
            self.servers[server] -= 1

# Teste
servers = ["Server1", "Server2", "Server3"]
lc_balancer = LeastConnectionsBalancer(servers)

for _ in range(10):
    server = lc_balancer.get_next_server()
    print(f"Server selected: {server}")
    lc_balancer.release_connection(server)
