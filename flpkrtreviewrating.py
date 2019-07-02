import bs4
import urllib.request as url
path='https://www.flipkart.com/apple-iphone-8-plus-space-grey-64-gb/p/itmexrgvehtzhh9v?pid=MOBEXRGVQKBREZP8&srno=b_1_1&otracker=clp_banner_1_7.bannerX3.BANNER_apple-products-store_W8OZI07LNL&lid=LSTMOBEXRGVQKBREZP8VWK6HB&fm=neo%2Fmerchandising&iid=9b48c29c-94de-44e7-8b15-3522a70fecb2.MOBEXRGVQKBREZP8.SEARCH&ppt=browse&ppn=browse&ssid=22eq6bvicw0000001560924171847'
httpresponse=url.urlopen(path)
page=bs4.BeautifulSoup(httpresponse)

title=page.find('span',class_='_35KyD6')
print(title.text)

priceInfo=page.find('div',class_='_1vC4OE _3qQ9m1')
Discount=page.find('div',class_='VGWI6T _1iCvwn')
productdescp=page.find('div',class_='_3u-uqB')

print(priceInfo.text)
print(Discount.text)
print(productdescp.text)
#rating = page.find_all('div', class_='hGSR34')
#review = page.find_all('p', class_='_2xg6Ul')
#for i,j in zip(rating, review):
     #print("Rating : {}, Review : {}".format(i.text, j.text))
divc = page.find('div', class_='_39LH-M')
a_tag = divc.find_all('a')
reviewsHref=a_tag[-1]['href']
newUrl = 'https://www.flipkart.com' + reviewsHref
#for p in newUrl:
 #print(newUrl+p)

httpResponse = url.urlopen(newUrl)
pagef= bs4.BeautifulSoup(httpResponse)

rating = pagef.find_all('div', class_='hGSR34')
review = pagef.find_all('p', class_='_2xg6Ul')

for i,j in zip(rating, review):
   print("Rating : {}, Review : {}".format(i.text, j.text))