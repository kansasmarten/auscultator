import requests, bs4, datetime, csv, yagmail
import pandas as pd
# Create a private.py file with the following string variables:
from private import gusername, gpassword, grecipient

yag = yagmail.SMTP(gusername, gpassword)
date = datetime.date.today()
patients = 0
url="https://www.tmh.org/covid-19/hospitalization-rates-and-your-safety"

### Primary function ###
def checkin():

    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text,'lxml')
    name = soup.find_all('p')

    ##########################################################
    ### To throw html into a file                          ###
    ### To make pretty on Mac vscode: shift + option + f   ###
    ##########################################################
    # file = open("htmlstuff.html", "w")
    # file.write(repr(soup))
    # file.close()

    for x in name:
        x = x.get_text()
        if "Total number of patients" in x:
            x = x.split(" ")
            patients = x[-1]
        elif "Updated" in x:
            x = x.split(" ")
            month, day, year = x[-1].split("/")
            year = "20"+year
            thisdate = datetime.date(int(year),int(month),int(day))
    
    if thisdate >= date:
        data = [[thisdate, patients]]
        df = pd.DataFrame(data=data, columns = ['Date', 'Patients'])
        return df
    else:
        # print("error")
        return False

    ##############
    ### Checks ###
    ##############
    # print(patients)
    # print(thisdate)

################################
### CSV Read, Combine, Write ###
################################
df1 = checkin()
if df1:
    # Add info to csv file
    df2 = pd.read_csv('data.csv')
    data = pd.concat([df1, df2], ignore_index=True)
    data.to_csv('data.csv', header=True, index=True)
    # email user the data
    contents = [
        "TMH has updated their information", url, 'data.csv'
    ]
    yag.send(grecipient, 'TMH Update', contents)