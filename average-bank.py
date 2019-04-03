import requests
import string

def GetJSON(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        print(url + " returned error code " + str(response.status_code))
        raise
    else:
        response_data = response.json()
        return response_data

words = {}
FDICFile = "https://banks.data.fdic.gov/api/institutions?filters=ACTIVE%3A1&fields=NAME&sort_by=OFFICES&sort_order=DESC&limit=10000&offset=0&format=json&download=false&filename=data_file"
dataBlob = GetJSON(FDICFile)["data"]

for bank in dataBlob:
    for s in bank["data"]["NAME"].split():
        for c in string.punctuation:
            s = s.replace(c,"")
            if s in words.keys():
                words[s] += 1
            else:
                words[s] = 1
                
for w in sorted(words, key=words.get, reverse=True):
    print(w, words[w])

