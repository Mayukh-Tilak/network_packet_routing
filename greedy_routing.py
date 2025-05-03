import random

class NetworkRouter:
    def __init__(self, name):
        self.name = name
        self.neighbors = []  # List of (neighbor, latency) pairs
    
    def add_neighbor(self, neighbor, latency):
        self.neighbors.append((neighbor, latency))
    
    def get_best_neighbor(self):
        # Return the neighbor with the minimum latency
        if not self.neighbors:
            return None
        return min(self.neighbors, key=lambda x: x[1])

def simulate_packet_routing(start_router, destination_router, time_steps=100):
    current_router = start_router
    path = [current_router.name]
    total_latency = 0
    steps = 0
    
    while current_router != destination_router and steps < time_steps:
        # Select the best neighbor based on greedy choice (least latency)
        best_neighbor = current_router.get_best_neighbor()
        if best_neighbor:
            path.append(best_neighbor[0].name)
            total_latency += best_neighbor[1]
            current_router = best_neighbor[0]  # Move to the best neighbor
        else:
            print("No valid route found.")
            return path, total_latency
        
        steps += 1

    if current_router == destination_router:
        return path, total_latency
    else:
        print("Destination not reachable within time steps.")
        return path, total_latency

# Create routers
routers = {f"R{i}": NetworkRouter(f"R{i}") for i in range(5)}

# Add neighbors with latency
routers["R0"].add_neighbor(routers["R1"], 5)
routers["R0"].add_neighbor(routers["R2"], 2)
routers["R1"].add_neighbor(routers["R0"], 5)
routers["R1"].add_neighbor(routers["R3"], 1)
routers["R2"].add_neighbor(routers["R0"], 2)
routers["R2"].add_neighbor(routers["R3"], 4)
routers["R3"].add_neighbor(routers["R1"], 1)
routers["R3"].add_neighbor(routers["R2"], 4)
routers["R4"].add_neighbor(routers["R2"], 3)
routers["R4"].add_neighbor(routers["R3"], 2)

# Simulate routing
start_router = routers["R0"]
destination_router = routers["R4"]
path, total_latency = simulate_packet_routing(start_router, destination_router)

print(f"Path: {' -> '.join(path)}")
print(f"Total Latency: {total_latency} ms")
