import requests
from lxml import html
import spacy


def get_custid_url(session_requests, cust_name):

    # Load English tokenizer, tagger, parser, NER and word vectors
    # nlp = spacy.load('en')

    search_url = "https://apply.shoresideloans.com/plm.net/customers/SearchCustomers.ashx?term="
    cust_url = "https://apply.shoresideloans.com/plm.net/customers/CustomerDetails.aspx?customerid="
    cust_getall_url = "https://apply.shoresideloans.com/plm.net/customers/CustomerDetails.aspx/GetPageAjaxContent?customerid="

    cust_search_url = search_url + cust_name.replace(' ', '+')

    result = session_requests.get(cust_search_url)
    custid_url = ''
    custid_getall_url = ''

    # Check if result is not empty
    if len(result.json()) > 0:
        result_json = result.json()[0]
        custid_url = "{0}{1}".format(cust_url, result_json[u'value'])
        custid_getall_url = "{0}{1}".format(cust_getall_url, result_json[u'value'])
    else:
        cust_name_parts = cust_name.split(' ')
        for name_part in cust_name_parts:
            cust_search_url = search_url + name_part
            result = session_requests.get(cust_search_url)
            if len(result.json()) > 0:
                result_json = result.json()
                #TODO Find the most similar name from the list and return its u'value'

                '''doc1 = nlp(cust_name)
                for element in result_json:
                    doc2 = nlp(element[u'label'])
                    print '{0} vs {1}. similarity: {2}'.format(doc1,doc2,doc1.similarity(doc2))
                    '''

    return custid_url, custid_getall_url
