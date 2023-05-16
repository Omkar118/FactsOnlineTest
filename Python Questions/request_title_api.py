"""
Make a GET request to this endpoint ”https://jsonplaceholder.typicode.com/posts”.
And print all values for the key “title”.
"""

# importing the requests library
import requests

# api-endpoint
URL = "https://jsonplaceholder.typicode.com/posts"

# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.json()

for i in range(0,100):
#     print(i)
    print("Title for ID:",i,":",data[i]['title'])
