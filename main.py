import requests
import selectorlib
import smtplib,ssl,os
from dotenv import load_dotenv

load_dotenv()


URL = "https://programmer100.pythonanywhere.com/tours/"

"INSERT INTO events VALUES ('Tigers','Tigers - City','2027-09-09')"

def scrape(URL):
    response = requests.get(URL)
    scraped = response.text
    return scraped

def extract(scraped):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    # Use .extract() directly without appending ['tours'] on this line
    data = extractor.extract(scraped)['tours']
    #print (data)
    return data
def write(data):
    with open('file.txt', 'a') as file:
        file.writelines(data+'\n')
def send_mail(data):
    sender_email = 'welcomekasthuri@gmail.com'
    receiver_email = 'welcomekasthuri@gmail.com'
    sender_password =os.getenv('PASSWORD')
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(sender_email,sender_password)
        server.sendmail(sender_email, receiver_email, data)

    print("Email Sent")
def read():
    with open('file.txt', 'r') as file:
        data = file.read()
    return data

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        content = read()
        if extracted != "No upcoming tours":

            if extracted not in content:
                value =extracted not in content
                write(extracted)
                #send_mail("subject:New event\n\n" +extracted)
                print(extracted)
                print(f"content - {content}")

