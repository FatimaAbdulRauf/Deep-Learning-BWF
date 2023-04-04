import pandas as pd
import json

df = pd.read_csv('data.csv', names=["a","b","c","d","message"])
print(df)

obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
 {"name": "Katie", "age": 38,
 "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""
result = json.loads(obj)
print(result)

data_j = pd.read_json("sample4.json")
print(data_j)

read_excel = pd.read_excel("states.xlsx")
print(read_excel)
