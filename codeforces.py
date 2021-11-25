import requests
import os
from bs4 import BeautifulSoup
from pprint import pprint
import time

#open and read the file after the appending:
path="..\..\codeforces\\"
f = open(path+"lastUpdate.txt", "r")
lastup=f.read()
f.close()
lastprocess=''

URL = "https://codeforces.com/submissions/t17/page/"
lastupnext=''
for i in range(10000):
    newurl=URL+str(i+1)
    print(newurl)
    page = requests.get(newurl)
    time.sleep(10)
    soup = BeautifulSoup(page.content, "html.parser")
    x=soup.find("html")
    x=x.find("div", id="pageContent")
    x=x.find_all("tr")
    lastprocessnext=''
    for j in range(len(x)-1):
        y=x[j+1].find_all("td")
        vr=y[5].find("span")
        strng=(y[3].find('a'))['href'].split('/')
        contest_id=strng[2]
        submission_id=vr['submissionid']
        if submission_id==lastprocess:
            break
        if submission_id==lastup:
            break
        if lastupnext=='':
            lastupnext=submission_id
        if lastprocessnext=='':
            lastprocessnext=submission_id
        if(vr['submissionverdict']=='OK'):
            submission_id="https://codeforces.com/contest/"+contest_id+"/submission/"+submission_id
            print(submission_id)
            page2=requests.get(submission_id)
            time.sleep(10)
            if page2.url!=submission_id:
                # print("error : "+page2.url)
                # print("status : "+str(page2))
                # pprint(vars(page2))
                continue
            soup2 = BeautifulSoup(page2.content, "html.parser")
            x2=soup2.find("html")
            name=(x2.find("div", class_="datatable"))
            name=name.find('table')
            name=name.find_all("tr")
            name=name[1]
            name=name.find_all('td')
            lan=name[3].get_text().split()[0]
            name=name[2].find('a').get_text()
            x2=x2.find('pre').get_text()
            if not os.path.exists(path):
                os.makedirs(path)
            ext=''
            if lan=='GNU':
                ext='.cpp'
            if lan=='Kotlin':
                ext='.kts'
            if lan=='PyPy':
                ext='.py'
            f = open(path+name+ext, "w")
            f.write(x2)
            f.close()
            print(name)
            # break
        lastprocess=lastprocessnext
    # break
f = open(path+"lastUpdate.txt", "w")
f.write(lastupnext)
f.close()
print("succefully done")