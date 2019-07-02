import bs4
import urllib.request as url
path=('https://www.flipkart.com/mobiles/~iphone-8-plus-64gb-and-256gb/pr?sid=tyy%2C4io&otracker=clp_banner_1_7.bannerX3.BANNER_apple-products-store_W8OZI07LNL&fm=neo%2Fmerchandising&iid=M_5826fc3d-bc31-4902-b063-9ccef8c5780b_3.W8OZI07LNL&ppt=clp&ppn=apple-products-store&ssid=nf5abwjrc00000001560877563648')
http=url.urlopen(path)
pageSource=bs4.BeautifulSoup(http)
divlist=pageSource.find_all('div',class_='_3wU53n')
priceList = pageSource.find_all('div', class_='_1vC4OE')
for item,price in zip(divlist,priceList):
 print(item.text)
 print(price.text)
 print('********************')
