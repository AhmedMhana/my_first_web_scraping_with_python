from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
 
my_url = 'https://deals.souq.com/eg-en/laptops/t/211' 


#opening up connection, grapping the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"block-grid-large"})

filename = "products.csv"
f = open(filename,"w")
headers = "product_name,price,shipping\n"
f.write(headers)

for container in containers:
	#discount = container.findAll("span",{"class":"discount"})[0].text.strip()
	price_html = container.findAll("h5",{"class":"price"})[0]
	price_before = price_html.span.text.replace("\n","").replace("\t","").strip()
	currency =  price_html.span.small.text.strip()

	product_name_container = container.findAll("h6",{"class":"title"})
	product_name = product_name_container[0].a["title"]
	
	shipping_container = container.findAll("div",{"class":"free-shipping"})
	shipping = shipping_container[0].text.strip()
	
	print("product name: "+ product_name)
	print("price: "+ price_before)
	#print("discount: "+ discount)
	print("shipping: "+ shipping)
	
	f.write(product_name.replace(",","|") + "," + price_before + "," + shipping + "\n")
	
f.close()