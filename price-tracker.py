import os
import requests
import re
import time
from bs4 import BeautifulSoup as bs

def generate_sound(inp):
    if inp == 1:
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 5000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
    elif inp == 2:
        beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
        beep(3)


def check_fk_price(url, amount):

    request = requests.get(url)
    soup = bs(request.content,'html.parser')

    product_name = soup.find("span",{"class":"B_NuCI"}).get_text()
    price = soup.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
    prince_int = int(''.join(re.findall(r'\d+', price)))
    print(product_name + " is at " + price)
    if prince_int < prince_int:
        print("Book Quickly")
        generate_sound(1)
    else:
        print("No Slots found")



def main():
    URL = "https://www.flipkart.com/apple-macbook-air-m1-8-gb-256-gb-ssd-mac-os-big-sur-mgn93hn-a/p/itmb53580bb51a7e?pid=COMFXEKMXWUMGPHW&lid=LSTCOMFXEKMXWUMGPHW40HAM7&marketplace=FLIPKART&q=macbook+air+m1&store=search.flipkart.com&srno=s_1_3&otracker=AS_Query_HistoryAutoSuggest_1_7_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_7_na_na_na&fm=SEARCH&iid=cf486f4b-8d24-4747-8fa5-4b17cb4b3a7b.COMFXEKMXWUMGPHW.SEARCH&ppt=hp&ppn=homepage&ssid=npbt1mddr40000001622911909542&qH=be9862f704979d6e"
    while True:
        check_fk_price(URL, 90000)
        time.sleep(3600)

if __name__ == "__main__":
    main()
