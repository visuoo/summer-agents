
import requests

data = "https://en.wikipedia.org/wiki/Lionel_Messi"
page = requests.get(data)
print(page.text)
