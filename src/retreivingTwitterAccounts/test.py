import requests
from bs4 import BeautifulSoup


def code_spider(url,operation):
    source = requests.get(url)
    text = source.text
    soup = BeautifulSoup(text)
    list=[]
    if(operation==1):
        for link in soup.find_all('a', href=True):
            politiician_link=link['href']

            if politiician_link.startswith('/politiker/') and 'pg' not in politiician_link:
#                 print politiician_link
                if politiician_link not in list:
                    list.append(politiician_link)
        return list
    else:
        
        for link in soup.find_all('a', href=True,target="twitter"):
            twitter_link=link['href']
            if twitter_link not in list:
                list.append(twitter_link)
                print twitter_link
        return list
#     for code in soup.findAll('code'):
#         line = str(code).replace('<br>','\n')
#         soup2 = BeautifulSoup(line)
#         script = soup2.get_text()
#         script = script.replace('?', ' ')
#         print(script)


def crawlForPages():
    i=1
    url='https://www.wahl.de/politiker/?pg='
    person_url='https://www.wahl.de'
    full_list=[]
#     crawling of the pages that I need to access to retreive the social media info
    while i<131:
        print i
        list=code_spider(url+str(i),1)
        i=i+1
        full_list.extend(list)
#     print full_list
#     now crawling through the actual pages for a person
    twitter_map={}
    f= open("guru99.txt","w+")
    for person_page in full_list:
        person_data=code_spider(person_url+person_page, 2)
        if len(person_data)>0:
            twitter_map[person_url+person_page]=person_data[0]
            person_url_info=person_page.split('/')
            name=person_url_info[3]
            party=person_url_info[2]
            f.write(person_url+person_page+" "+name+" "+party+" "+person_data[0]+'\n')
    print twitter_map
    f.close()
crawlForPages()