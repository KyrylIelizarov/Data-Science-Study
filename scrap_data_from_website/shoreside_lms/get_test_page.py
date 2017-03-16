import login_to_lms
import get_cust_id
import get_cust_data
import requests
from lxml import html

# Log In to Shoreside LMS
session_requests = login_to_lms.login_lms("jack", "paf52")

custid_url, cust_getall_url = get_cust_id.get_custid_url(session_requests, 'Shonta Jones')
result = session_requests.get(custid_url)
tree = html.fromstring(result.text)
javascript_content = tree.xpath('//script[@type = "text/javascript"]/text()')

# POST Pin All information
payload = {"pageids": ["LoanHistoryView", "ContactInfoView", "EmploymentInfoView", "BankInfoView",
                       "PrepaidCardView", "DebitCardView", "ReferencesView", "LandlordView",
                       "CustomerSiteView", "CustomerFilesView", "CustomerDetailsHistoryView"]
           }
result = session_requests.post(cust_getall_url, json=payload)

print result.text
