from typing import List, Optional

# Ref: https://opendsa-server.cs.vt.edu/OpenDSA/Books/Everything/html/GraphImpl.html#graph-implementations
class Edge:
    vertex: int
    prev: Optional["Edge"]
    next: Optional["Edge"]

    def __init__(self, v: int, p: Optional["Edge"], n: Optional["Edge"]) -> None:
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
    vertices: List[Vertex]
    edges: List[Edge]
    actor_indexes: dict[str, int]
    movie_indexes: dict[str, int]

    def __init__(self) -> None:
        self.edge_count = 0
        self.vertices = []
        self.edges = []
        self.actor_indexes = {}
        self.movie_indexes = {}
    
    def add_connection(self, actor: str, movie: str) -> None:
        actor_idx = self._add_actor(actor)
        movie_idx = self._add_movie(movie)
        self._add_edge(actor_idx, movie_idx)
    
    def _add_actor(self, actor: str) -> int:
        # Adds vertex for actor and returns index of the actor
        idx = self.actor_indexes.get(actor.lower(), None)
        if not idx:
            idx = len(self.vertices)
            new_vertex = Vertex(actor, "actor")
            self.vertices.append(new_vertex)
            self.edges.append(Edge(-1, None, None))
            self.actor_indexes[actor.lower()] = idx
        return idx

    def _add_movie(self, movie: str) -> int:
        # Adds vertex for movie and returns index of the movie
        idx = self.movie_indexes.get(movie.lower(), None)
        if not idx:
            idx = len(self.vertices)
            new_vertex = Vertex(movie, "movie")
            self.vertices.append(new_vertex)
            self.edges.append(Edge(-1, None, None))
            self.movie_indexes[movie.lower()] = idx
        return idx

    def get_value(self, v: int) -> Vertex:
        return self.vertices[v]
    
    def set_value(self, v: int, val: Vertex) -> None:
        self.vertices[v] = val
    
    def neighbors(self, v: int) -> List[int]:
        temp: List[int] = []
        curr: Edge = self.edges[v]
        while curr.next:
            curr = curr.next
            temp.append(curr.vertex)
        return temp
    
    def vertex_count(self) -> int:
        return len(self.vertices)
    
    def get_movie_index(self, name: str) -> Optional[int]:
        return self.movie_indexes.get(name.lower(), None)
        
    
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
        