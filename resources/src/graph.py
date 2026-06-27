from typing import List, Any

# Ref: https://opendsa-server.cs.vt.edu/OpenDSA/Books/Everything/html/GraphImpl.html#graph-implementations
# TODO: fix typing of prev and next
class Edge:
    vertex: int
    prev: Any
    next: Any

    def __init__(self, v: int, p: Any, n: Any) -> None:
        self.vertex = v
        self.prev = p
        self.next = n

class Vertex:
    name: str
    type: str

    def __init__(self, n: str, t: str) -> None:
        self.name = n
        self.type = t

class Graph:
    edge_count: int
    verticies: List[Vertex]
    edges: List[Edge]
    actor_indexes: dict[str, int]
    movie_indexes: dict[str, int]

    def __init__(self) -> None:
        self.edge_count = 0
        self.verticies = []
        self.edges = []
        self.actor_indexes = {}
        self.movie_indexes = {}
        return
    
    def add_connection(self, actor: str, movie: str) -> None:
        actor_idx = self._add_actor(actor)
        movie_idx = self._add_movie(movie)
        self._add_edge(actor_idx, movie_idx)
    
    def _add_actor(self, actor: str) -> int:
        # Adds vertex for actor and returns index of the actor
        idx = self.actor_indexes.get(actor, None)
        if not idx:
            idx = len(self.verticies)
            new_vertex = Vertex(actor, "actor")
            self.verticies.append(new_vertex)
            self.edges.append(Edge(-1, None, None))
            self.actor_indexes[actor] = idx
        return idx

    def _add_movie(self, movie: str) -> int:
        # Adds vertex for movie and returns index of the movie
        idx = self.movie_indexes.get(movie, None)
        if not idx:
            idx = len(self.verticies)
            new_vertex = Vertex(movie, "movie")
            self.verticies.append(new_vertex)
            self.edges.append(Edge(-1, None, None))
            self.movie_indexes[movie] = idx
        return idx

    def get_value(self, v: int) -> Vertex:
        return self.verticies[v]
    
    def set_value(self, v: int, val: Vertex) -> None:
        self.verticies[v] = val
    
    def neighbors(self, v: int) -> List[int]:
        temp: List[int] = []
        curr: Edge = self.edges[v]
        while curr.next:
            curr = curr.next
            temp.append(curr.vertex)
        return temp
        
    
    def _find(self, v: int, w: int) -> Edge | None:
        curr: Edge = self.edges[v]
        while (curr.next and curr.next.vertex < w):
            curr = curr.next
        return curr
    
    def _add_edge(self, v: int, w: int) -> None:
        curr: Edge = self._find(v, w)
        if curr.next and curr.next.vertex == w:
            return
        else:
            # Add edge to v
            curr.next = Edge(w, curr, curr.next)
            if curr.next.next:
                curr.next.next.prev = curr.next
            # Add edge to w
            curr = self._find(w, v)
            curr.next = Edge(v, curr, curr.next)
            if curr.next.next:
                curr.next.next.prev = curr.next
            self.edge_count += 1
        

# TODO: Remove this when done testing
# connections = [
#     { "movie": "The Odyssey", "actor": "Matt Damon" },
#     { "movie": "The Odyssey", "actor": "Tom Holland" },
#     { "movie": "The Odyssey", "actor": "Zendaya" },
#     { "movie": "The Odyssey", "actor": "Robert Pattinson" },
#     { "movie": "The Odyssey", "actor": "Anne Hathaway" },
# ]

# graph = Graph()

# for connection in connections:
#     graph.add_connection(connection["actor"], connection["movie"])

# neighbors = graph.neighbors(1)
# print("Connections to The Odyssey:")
# for neighbor in neighbors:
#     vertex = graph.get_value(neighbor)
#     print(f"Name: {vertex.name}, Type: {vertex.type}")

# neighbors = graph.neighbors(5)
# print("Connections to Anne Hathaway:")
# for neighbor in neighbors:
#     vertex = graph.get_value(neighbor)
#     print(f"Name: {vertex.name}, Type: {vertex.type}")