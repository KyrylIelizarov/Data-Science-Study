import login_to_lms
import get_cust_id
import get_cust_data
import requests
import re
import sys
from lxml import html

def main_func(username, password):
    # Log In to Shoreside LMS
    session_requests = login_to_lms.login_lms(username, password)

    custid_url, cust_getall_url = get_cust_id.get_custid_url(session_requests, 'Luis Salcedo')
    result = session_requests.get(custid_url)
    tree = html.fromstring(result.text)
    javascript_content = tree.xpath('//script[@type = "text/javascript"]/text()')

    # POST Pin All information
    payload = {"pageids": ["LoanHistoryView", "ContactInfoView", "EmploymentInfoView", "BankInfoView",
                           "PrepaidCardView", "DebitCardView", "ReferencesView", "LandlordView",
                           "CustomerSiteView", "CustomerFilesView", "CustomerDetailsHistoryView"]
               }
    result = session_requests.post(cust_getall_url, json=payload)
    javascript_full_content = html.fromstring(result.text).text_content()
    print javascript_full_content

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    main_func(username, password)