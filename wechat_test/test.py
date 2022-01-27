from bs4 import BeautifulSoup
soup = BeautifulSoup(open('test.html',encoding = "utf-8"),features = "lxml")

print(soup.text)

