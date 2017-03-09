import requests
import sys
from lxml import html

def login_lms(username, password):
    session_requests = requests.session()

    login_url = "https://apply.shoresideloans.com/plm.net/LoginPage.aspx"
    login_type_url = "https://apply.shoresideloans.com/plm.net/LoginSetType.aspx"

    result = session_requests.get(login_url)
    tree = html.fromstring(result.text)
    viewstategenerator = list(set(tree.xpath("//input[@name='__VIEWSTATEGENERATOR']/@value")))[0]
    viewstate = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
    eventvalidation = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]

    payload = {
        "__EVENTVALIDATION": eventvalidation,
        "__VIEWSTATE": viewstate,
        "__VIEWSTATEGENERATOR": viewstategenerator,
        "ctl00$maincontent$LoginButton": "Login",
        "ctl00$maincontent$Password": password,
        "ctl00$maincontent$Username": username
    }
    result = session_requests.post(
        login_url,
        data = payload
    )

    result = session_requests.get(login_type_url)
    tree = html.fromstring(result.text)
    viewstategenerator = list(set(tree.xpath("//input[@name='__VIEWSTATEGENERATOR']/@value")))[0]
    viewstate = list(set(tree.xpath("//input[@name='__VIEWSTATE']/@value")))[0]
    eventvalidation = list(set(tree.xpath("//input[@name='__EVENTVALIDATION']/@value")))[0]
    #eventargument = list(set(tree.xpath("//input[@name='__EVENTARGUMENT']/@value")))[0]
    #eventtarget = list(set(tree.xpath("//input[@name='__EVENTTARGET']/@value")))[0]

    payload = {
        "__EVENTARGUMENT": "",
        "__EVENTTARGET": "",
        "__EVENTVALIDATION": eventvalidation,
        "__VIEWSTATE": viewstate,
        "__VIEWSTATEGENERATOR": viewstategenerator,
        "ctl00$maincontent$LoginButton": "Login",
        "ctl00$maincontent$LoginType": "LoginTypeCorporate",
        "ctl00$maincontent$RegionsList": "",
        "ctl00$maincontent$StoresList": ""
    }
    result = session_requests.post(
        login_type_url,
        data=payload
    )


    print(result.text)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    login_lms(username, password)
