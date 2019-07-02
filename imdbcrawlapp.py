import bs4
import urllib.request as url
path='https://www.imdb.com/find?ref_=nv_sr_fn&q=batman'
httpresponse=url.urlopen(path)
page=bs4.BeautifulSoup(httpresponse)

title=page.find('td',class_='result_text')
print(title.text)
divc = page.find('td', class_='result_text')
a_tag = divc.find('a')
Href=a_tag['href']
newUrl = 'https://www.iMDb.com' + Href
print(newUrl)
httpRes = url.urlopen(newUrl)
pagef=bs4.BeautifulSoup(httpRes)
duration=pagef.find('time',datetime='PT126M')
print("MOVIE DURATION: {}".format(duration.text.strip()))
releasedate=pagef.find('a',title='See more release dates')
print("RELEASE DATE: {}".format(releasedate.text.strip()))
plot=pagef.find('div',class_='summary_text')
print("PLOT SUMMARY:  {}".format(plot.text.strip()))
director=pagef.find_all('div',class_='credit_summary_item')
for i in director:
  print(i.text.strip())


a_tag = pagef.find_all('a', class_='quicklink')
reviewsHref=a_tag[2]['href']

newUrl = 'https://www.imdb.com' + reviewsHref
print(newUrl)
httpResponse = url.urlopen(newUrl)
pagef= bs4.BeautifulSoup(httpResponse)

rating = pagef.find_all('span', class_='rating-other-user-rating')
review = pagef.find_all('a', class_='title')

for i,j in zip(rating, review):
   print("Rating : {}, Review : {}".format(i.text.strip(), j.text.strip()))