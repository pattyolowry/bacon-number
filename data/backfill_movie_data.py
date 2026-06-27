from bridges.bridges import *
from bridges.data_src_dependent import data_source
from dotenv import load_dotenv
import csv

load_dotenv()
bridges_api_key = os.getenv("BRIDGES_API_KEY")
bridges_user = os.getenv("BRIDGES_API_USER")

# Fetch data from BRIDGES API
bridges = Bridges(2, bridges_user, bridges_api_key)
bridges.set_title ("Accessing Wikidata Movie/Actor Data")

# Write to movie_data.csv
# Ref: https://www.geeksforgeeks.org/python/working-csv-files-python/
with open ("./data/movie_data.csv", "a") as file:
    csvwriter = csv.writer(file)
    for year in range(1950, 2027):
        print(f"Fetching data for {year}...")
        data = data_source.get_wiki_data_actor_movie(year, year)
        print(f"{len(data)} connections found!")
        for entry in data:
            csvwriter.writerow([year, entry.movie_name, entry.actor_name]) 
        # Wikidata only allows one request per min, so sleep in between requests
        time.sleep(60)