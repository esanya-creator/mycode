import requests, json
import csv

url= "https://api.exchangerate-api.com/v4/latest/"
class CurrencyConvert(object):
    
    def get_countryfrom_list(self):
        list1=[]
        with open("/home/ereddy/country.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for lines in csv_reader:
                list1.append(lines[0])
            return(list1)


    def get_currency_convert(self, from_country,url=url):
        url=url+from_country
        resp= requests.get(url).text
       	response= json.loads(resp)
        return response

    def get_currency(self,response):
        dict=response["rates"]
        for key in dict:
            if key == "INR":
                return (dict.get(key))
           
                

        
