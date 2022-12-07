from selenium import webdriver
from  bs4 import BeautifulSoup
browser = webdriver.Chrome()
browser.get("https://ful.io")
content = browser.page_source
soup = BeautifulSoup(content)
social_links = []
for i in soup.findAll('div', attrs={'class':"lg:w-1/4 md:w-1/2 w-full px-4"}):
    mail = i.find('a',href=True,attrs={'class': "hover:text-gray-500 text-base leading-4 mt-2 lg:mt-4 text-white cursor-pointer flex items-center justify-center md:justify-start mb-4"})
    contact = i.find('a',href=True,attrs={'class':""})

for i in soup.find_all('div',attrs={'class':"flex my-2 -mx-1 justify-center"}):
    social_link1 = i.find('a',href=True,attrs={'class':"px-1"})
    social_link2 = i.find('a',href=True,attrs={'class':""})
    
print("SOCIAL LINKS")
print(social_link1['href'])
print(social_link2['href'])  
print("Email/s")
print(mail.text)
print("Contact")
print(contact.text)



