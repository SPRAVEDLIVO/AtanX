import json
def settings(file="config.json"):
    with open(file) as f:
        config = json.load(f)
        return config