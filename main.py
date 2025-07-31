import sqlite3
import json


try:
    with open('regData.json', 'r') as file:
        data = json.load(file)
    print("Data loaded successfully.")
    print(data)
except:
    print("you suck at coding")
    quit()

