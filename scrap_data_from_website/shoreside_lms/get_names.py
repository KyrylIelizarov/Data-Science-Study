import login_to_lms
from lxml import html
import sys
import requests
# Import pandas
import pandas as pd

# Log In to Shoreside LMS
session_requests = login_to_lms.login_lms("jack", "paf52")

# Load .xslx with names
file = 'Shoreside_LMS_loans.xlsx'
xl = pd.ExcelFile(file)
input_names = xl.parse('input')

search_url = "https://apply.shoresideloans.com/plm.net/customers/SearchCustomers.ashx?term="
cust_url = "https://apply.shoresideloans.com/plm.net/customers/CustomerDetails.aspx?customerid="

#Luis Salcedo
#Billie Evans

for lab, row in input_names.iterrows():
    if lab < 1:
        # Get and prepare Name
        cust_name = row['Judgment Creditor']
        cust_name = cust_name.rstrip(' ')
        cust_search_url = search_url + cust_name.replace(' ', '+')


        result = session_requests.get(cust_search_url)
        custid_url = ''
        # Check if result is not empty
        if len(result.json()) > 0:
            result_json = result.json()[0]
            custid_url = cust_url + str(result_json[u'value'])
            #print custid_url
        else:
            print "Nothing found"

        if len(custid_url) > 0:
            result = session_requests.get(custid_url)
            print result.text.encode('ascii', 'ignore')
            '''tree = html.fromstring(result.text)
            smth = tree.xpath('//table[@class = "ProfileProperties"]'/)[0]
            print smth'''
