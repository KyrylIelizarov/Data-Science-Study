import get_cust_data
import re


text = '''---\\u003eAddress :\\u003c/td\\u003e\\r\\n      \\u003ctd\\u003e807 28th Street\\u003c/td\\u003e\\r\\n      \\u003ctd\\u003eRent or Own :\\u003c/td\\u003e\\r\\n      \\u003ctd\\u003e\\u003c/td\\u003e\\r\-'''
step2 = re.search('\\\\u003ctd\\\\u003e[\w\d., ]*\\\\u003c', text)


print step2.group()