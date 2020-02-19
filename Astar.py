from heapq import heappush, heappop


class Astar:
    def __init__(self):
        self.explored = {}
        self.path = []

    def traverser(self, graph, start_node, goal_node):
        if start_node not in graph or goal_node not in graph:
            print('Either source', start_node,
                'or target', goal_node, 'is not in G')

        # Queue items a tuple (costf(priority), (node, costg, parent})
        # Init queue with start node
        queue = []
        heappush(queue, (0, {'node': start_node, 'cost': 0, 'parent': None}))

        while queue:
            current_node, cost, parent = list(heappop(queue)[1].values())

            if current_node == goal_node:
                self.explored[current_node] = parent
                self.path = [current_node]
                node = parent
                while node is not None:
                    self.path.append(node)
                    node = self.explored[node]
                self.path.reverse()
                break

            if current_node not in self.explored:
                self.explored[current_node] = parent

            for neighbor, data in graph[current_node].items():
                costg = cost + float(data.get('weight'))
                costh = float(graph.node[neighbor]['heuristic'])
                costf = round((costg + costh), 1)

                queuenodes = [tuple[1]['node'] for tuple in queue]
                if neighbor not in self.explored and neighbor not in queuenodes:
                    heappush(queue, (costf, {
                        'node': neighbor, 'cost': costg, 'parent': current_node
                    }))
                elif neighbor in queuenodes:
                    queue_index = queuenodes.index(neighbor)
                    saved_costf = queue[queue_index][0]

                    # Replace if current cost is lower than saved
                    if costf < saved_costf:
                        queue.pop(queue_index)
                        heappush(queue, (costf, {
                            'node': neighbor, 'cost': costg, 'parent': current_node
                        }))