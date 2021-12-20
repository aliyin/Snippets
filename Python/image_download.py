import requests

def GetImage(link):
    try:    
        response = requests.get(link, stream=True)
        response.raise_for_status()
        #this will split the url by '/', and get the last index of it, for the file name.
        with open(link.split("/")[-1], 'wb') as handle:
            handle.write(response.content)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

GetImage("https://via.placeholder.com/350x150.jpg")

