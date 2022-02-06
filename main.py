import requests
from bs4 import BeautifulSoup

 if __name__=='__main__':
     web = requests.get('https://www.bmkg.go.id/cuaca/prakiraan-cuaca-indonesia.bmkg')
     #print(web.text)
     soap = BeautifulSoup(web.content, 'html.parser')
     #print(soap)
     cuaca = soap.select('.table-prakicu-provinsi > tbody > tr')
     #print(cuaca[0])
     data_cuaca = []
     for item in cuaca:
         baris = item.select('td')
         data_cuaca.append({
             'kota': baris[0].text,
             'siang': baris[1].text,
             'malam': baris[2].text,
             'suhu': baris[3].text,
             'kelembaban': baris[4].text,
         }]
         


