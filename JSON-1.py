import json

data = {
    "url": "https://www.youtube.com/watch?v=UmljXZIypDc",
    "title": "django tutorial part 1",
    "date": "1397",
    "comments": True,
    "list_of_comments": [
        {
            "username": "awesome!",
        },
        {
            "username": "keep it up",
        }
    ],
    "suggestions": ["flask tutorial", "fastapi tutrial"],
    "likes": None,
}

# Serialize

# json_data = json.dumps(data, indent=4)
# print(json_data)

file = open("data.json", "w")
json.dump(data, file, indent=4)
