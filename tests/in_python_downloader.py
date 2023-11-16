import requests

url = "https://territorial.io/clans"
response = requests.get(url)

if response.status_code == 200:
    with open("clans", "wb") as file:
        file.write(response.content)
        print("File downloaded successfully!")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
