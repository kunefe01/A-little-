
import requests
import json

api_key = "9f3084e4e59b10febf761574"
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz = input("Bozulacak olan döviz türü : ")
alinan_döviz = input("Alınan döviz türü : ")
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsunuz : "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc_json = json.loads(sonuc.text)

# print(sonuc_json["conversion_rates"][alinan_döviz])

print("1 {0} = {1} {2}".format(bozulan_doviz,sonuc_json["conversion_rates"][alinan_döviz],alinan_döviz))

print("{0} {1} = {2} {3}".format(miktar , bozulan_doviz , miktar * sonuc_json["conversion_rates"][alinan_döviz] , alinan_döviz))