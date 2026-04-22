import urllib.request
import json

def get_top_10_richest():
    url = "https://forbes400.onrender.com/api/forbes400?limit=10"

    print("Fetching live data...\n")
    
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    print("=" * 65)
    print(f"{'TOP 10 RICHEST PEOPLE IN THE WORLD':^65}")
    print("=" * 65)
    print(f"{'Rank':<6} {'Name':<25} {'Net Worth':>12}  {'Source'}")
    print("-" * 65)

    for i, person in enumerate(data, start=1):
        name      = person.get("person", {}).get("name", "N/A")
        net_worth = f"${person.get('finalWorth', 0) / 1000:.1f}B"
        source    = person.get("source", "N/A")
        print(f"{i:<6} {name:<25} {net_worth:>12}  {source}")

    print("=" * 65)

get_top_10_richest()