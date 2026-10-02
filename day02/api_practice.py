"""
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print("Status code:", response.status_code)
print("Response:")
print(response.json())
"""
"""
import requests

url = "https://jsonplaceholder.typicode.com/users"

new_user = {
    "name": "Varun",
    "email": "varun@example.com",
    "city": "Hyderabad"
}

response = requests.post(url, json=new_user)

print("Status code:", response.status_code)
print("Response:")
print(response.json())
"""
"""
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

updated_user = {
    "name": "Varun Kumar",
    "username": "varun",
    "email": "varun@example.com",
    "address": {
        "city": "Hyderabad"
    },
    "phone": "9999999999",
    "website": "example.com"
}

response = requests.put(url, json=updated_user)

print("Status code:", response.status_code)
print("Response:")
print(response.json())
"""
'''
import requests

url = "https://jsonplaceholder.typicode.com/users/1"

update = {
    "email": "newemail@example.com"
}

response = requests.patch(url, json=update)

print("Status code:", response.status_code)
print("Response:")
print(response.json())
'''

import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.delete(url)

print("Status code:", response.status_code)
print("Response:")
print(response.text)