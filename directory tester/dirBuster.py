import requests
url = input("Enter the url: ")
wordlist_location = input("Enter the worldlist location:")
with open(wordlist_location, 'r') as file:
    words = file.read()
    line = words.splitlines()

    for i in line:
        url = f"{url}/{i}"
        r = requests.get(url)
        if r.status_code==200:
            with open("ValidUrl.txt","a") as file:
                file.write(f"{url}\n")
        else:
            print(f"Not valid => {url}")
            
    