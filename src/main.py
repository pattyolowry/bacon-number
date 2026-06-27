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

    return 0

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)