import requests
import xlsxwriter
from bs4 import BeautifulSoup as b


workbook = xlsxwriter.Workbook('prueba1.xlsx')
worksheet = workbook.add_worksheet('Amazon_products')#name sheet
worksheet.write('A1','Product')
worksheet.write('B1', 'Price')


#url = 'https://www.amazon.com/s?k=teclado+gamer'
url = 'https://www.amazon.com/s?k=teclado+gamer&language=es_COP'

headers = {
'user_agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 OPR/80.0.4170.61",
"Accept-Encoding":"gzip, deflate, br",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
'permissions-policy': 'interest-cohort=()',
"DNT":"1",
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


html = requests.get(url,headers=headers)
content = html.content
soup = b(content,'lxml')
print(soup)

row = 1

for post in soup.findAll('div',{'class':'a-section a-spacing-medium'}):
	title = post.find('a',{'class':'a-link-normal a-text-normal'})
	price = post.find('span',{'class':'a-offscreen'})
	if price is not None:
		print(title.text)
		print(price.text)
		worksheet.write(row,0,title.text)
		worksheet.write(row,1,price.text)
		row += 1
workbook.close()
