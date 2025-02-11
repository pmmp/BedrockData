from bs4 import BeautifulSoup
import json
import requests
import os
import shutil

save = ["ParticleType"]

def prepare():
    if os.path.exists("enums"):
        shutil.rmtree("enums")
    os.makedirs("enums")

def fetch_html(branch):
    url = f"https://raw.githubusercontent.com/Mojang/bedrock-protocol-docs/refs/heads/{branch}/html/enums.html"
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def dump_enums(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    rows = soup.table.contents[3:]
    for row in rows:
        enum_name = row.td.string
        enum_values = {}
        
        for line in row.find_all("tr"):
            cols = line.find_all("td")
            key = cols[0].string
            value = cols[1].string.split(" ")[0]
            try:
                enum_values[key] = int(value)
            except:
                enum_values[key] = value
        
        print(enum_name, enum_values)
        if enum_name in save:
            file_name = enum_name.replace("::", "_")
            with open(f"enums/{file_name}.json", "w", encoding="utf-8") as json_file:
                json.dump({"name": enum_name, "values": enum_values}, json_file, indent=4)

prepare()
branch = input("Enter branch name (main): ") or "main"
html = fetch_html(branch)
dump_enums(html)