import heapq

def calculate_min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost
        
        heapq.heappush(cables, cost)

    return total_cost


print(calculate_min_cost_to_connect_cables([10, 22, 1, 5, 12, 2, 12]))
