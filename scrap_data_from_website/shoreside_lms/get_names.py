import login_to_lms
import get_cust_id
import get_cust_data

from lxml import html

import sys
import requests
# Import pandas
import pandas as pd


def main_func(username, password):
    # Log In to Shoreside LMS
    session_requests = login_to_lms.login_lms(username, password)

    # Load .xslx with names
    xlsx_file = 'Shoreside_LMS_loans.xlsx'
    xl = pd.ExcelFile(xlsx_file)
    input_names = xl.parse('input')
    output_names = input_names

    for lab, row in input_names.iterrows():
        if lab < 5:
            # if Shonta Jones2897
            # Get and prepare Name
            cust_name = row['Judgment Creditor']
            cust_name = cust_name.rstrip(' ')

            custid_url, cust_getall_url = get_cust_id.get_custid_url(session_requests, cust_name)

            if len(custid_url) > 0:
                # GET main loan information
                result = session_requests.get(custid_url)
                tree = html.fromstring(result.text)
                javascript_content = tree.xpath('//script[@type = "text/javascript"]/text()')
                for str in javascript_content:
                    print type(str)
                    output_names.loc[lab, 'SSN'] = get_cust_data.get_cust_ssn(str)
                    output_names.loc[lab, 'Loan #'] = get_cust_data.get_cust_loannum(str)
                    output_names.loc[lab, 'Loan Status'] = get_cust_data.get_cust_loanstatus(str)

                # POST Pin All information
                payload = {"pageids": ["LoanHistoryView", "ContactInfoView", "EmploymentInfoView", "BankInfoView",
                                       "PrepaidCardView", "DebitCardView", "ReferencesView", "LandlordView",
                                       "CustomerSiteView", "CustomerFilesView", "CustomerDetailsHistoryView"]
                           }
                result = session_requests.post(cust_getall_url, json=payload)
                javascript_full_content = result.text
                print type(javascript_full_content)
                output_names.loc[lab, 'Address'] = get_cust_data.get_cust_address(javascript_full_content)
                output_names.loc[lab, 'City'] = get_cust_data.get_cust_city(javascript_full_content)
                state, zip = get_cust_data.get_cust_statezip(javascript_full_content)
                output_names.loc[lab, 'State'] = state
                output_names.loc[lab, 'Zip'] = zip

            print ("{0} SSN:{1} Loan#: {2} Loan Status: {3} Address: {4} City: {5} State: {6} Zip: {7}".format(
                output_names.loc[lab, 'Judgment Creditor'], output_names.loc[lab, 'SSN'],
                output_names.loc[lab, 'Loan #'], output_names.loc[lab, 'Loan Status'],
                output_names.loc[lab, 'Address'], output_names.loc[lab, 'City'],
                output_names.loc[lab, 'State'], output_names.loc[lab, 'Zip']
            ))


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    main_func(username, password)
