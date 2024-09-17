import requests

img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVJCpCdWiUEXEM_XdSnqHcvfZkz3U5NOZLMQ&s"

response = requests.get(img)

with open("test.jpg", "wb") as file:
    file.write(response.content)
