from typing import List, Optional
from collections import deque
import csv
from graph import Graph



def main() -> int:
    graph = Graph()

    # Pull data from movie_data.csv
    # Ref: https://www.geeksforgeeks.org/python/working-csv-files-python/
    with open ("./data/movie_data.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            year, movie, actor = row
            graph.add_connection(actor, f"{movie} ({year})")

    print(f"Edges: {graph.edge_count}")
    print(f"Vertices: {graph.vertex_count()}")

    # # TODO: Remove this when done testing
    # connections = [
    #     { "movie": "The Odyssey", "actor": "Matt Damon" },
    #     { "movie": "The Odyssey", "actor": "Tom Holland" },
    #     { "movie": "The Odyssey", "actor": "Zendaya" },
    #     { "movie": "The Odyssey", "actor": "Robert Pattinson" },
    #     { "movie": "The Odyssey", "actor": "Anne Hathaway" },
    #     { "movie": "The Devil Wears Prada", "actor": "Anne Hathaway" },
    #     { "movie": "The Devil Wears Prada", "actor": "Meryl Streep" },
    #     { "movie": "Mamma Mia", "actor": "Meryl Streep" },
    #     { "movie": "Mamma Mia", "actor": "Amanda Seyfried" },
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
    return 0

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)