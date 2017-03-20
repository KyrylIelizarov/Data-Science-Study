import re

def get_cust_ssn(text_to_parse):

    #SSN search reg exp
    reg_expression_ssn = '\\\\u003eSSN :\\\\u003c/b\\\\u003e\\\\u003c/td\\\\u003e\\\\r\\\\n    \\\\u003ctd\\\\u003e\\\\u003cb\\\\u003e\d{3}-\d{2}-\d{4}\\\\u003c'

    # Search SSN
    ssn = ''
    m = re.search(reg_expression_ssn, text_to_parse)
    if m != None:
        ssn = re.search('\d{3}-\d{2}-\d{4}', m.group()).group()

    return ssn

def get_cust_loannum(text_to_parse):

    #Loan # search reg exp
    reg_expression_loannum = 'Loan# \d*'

    # Search Loan #
    loan_num = ''
    m = re.search(reg_expression_loannum, text_to_parse)
    if m != None:
        #print '---{0}---'.format(m.group())
        loan_num = re.search('\d*$', m.group()).group()

    return loan_num

def get_cust_loanstatus(text_to_parse):

    #Loan Status search reg exp
    reg_expression = 'ctl00_LoansRepeater_Span_Loan_Status2_0\\\\"( style=\\\\"color:red;\\\\"\\\\u003e[\w, ]*\\\\u003c/|\\\\u003e[\w, ]*\\\\u003c/)span\\\\u003e[\w, ]*\\\\r\\\\n'

    Loan_status=''
    step1 = re.search(reg_expression, text_to_parse)
    if step1 != None:
        step2_1 = re.search('\\\\u003e[\w, ]*\\\\u003c/', step1.group())
        step2_2 = re.search('\\\\u003e[\w, ]*\\\\r\\\\n', step1.group())
        step3_1 = step2_1.group()[6:-7]
        step3_2 = step2_2.group()[6:-4]
        Loan_status = step3_1 + step3_2

    return Loan_status

def get_cust_address(text_to_parse):

    #Address search reg exp

    reg_expression = '\\\\u003eAddress :\\\\u003c/td\\\\u003e\\\\r\\\\n      \\\\u003ctd\\\\u003e[\w\p\d.,-:;/ ]*\\\\u003c/td\\\\u003e\\\\r\\\\n'

    address = ''
    index_start = text_to_parse.find("\\\\u003eAddress :")
    index_end = text_to_parse.find("\\u003eRent or Own :")
    step1 = text_to_parse[index_start + 61: index_end]
    address = step1[0:step1.find("\\")]

    return address

def get_cust_city(text_to_parse):

    #City search reg exp
    reg_expression = '\\\\u003eCity :\\\\u003c/td\\\\u003e\\\\r\\\\n[\s ]*\\\\u003ctd\\\\u003e[\w\p\d.,-:;/ ]*\\\\u003c/td\\\\u003e\\\\r\\\\n'

    city = ''
    index_start = text_to_parse.find("\\\\u003eCity :")
    index_end = text_to_parse.find("\\\\u003eState, Zip :")
    step1 = text_to_parse[index_start + 58: index_end]
    city = step1[0:step1.find("\\")]
    return city

def get_cust_statezip(text_to_parse):

    #State, Zip search reg exp
    reg_expression = '\\\\u003ctd\\\\u003eState, Zip :\\\\u003c / td\\\\u003e\\\\r\\\\n[ ]*\\\\u003ctd\\\\u003e\\\\r\\\\n[\w ]*\\\\r\\\\n[\d -]*\\\\r\\\\n'

    state = ''
    zip = ''
    index_start = text_to_parse.find("\\\\u003eState, Zip :")
    index_end = text_to_parse.find("\\\\u003eMail Address :")
    step1 = text_to_parse[index_start + 70: index_end]
    state = re.search('[A-Z]{2}',step1[0:step1.find("\\\\r\\\\n")]).group()
    step2 = step1[step1.find("\\\\r\\\\n")+6:step1.find("\\\\u003c")]
    zip = re.search('[0-9]{5}|[0-9]{5}-[0-9]{4}',step2[0:step2.find("\\\\r\\\\n")]).group()

    return  state, zip

def get_cust_bankname(text_to_parse):
    # Bank Name search reg exp

    index_start = text_to_parse.find("\\\\u003eBank Name :")
    index_end = text_to_parse.find("\\\\u003eBank Phone :")
    step1 = text_to_parse[index_start + 90: index_end]
    bank_name = step1[0:step1.find("\\")]

    return bank_name


def get_cust_aba(text_to_parse):
    # Bank Name search reg exp

    index_start = text_to_parse.find("\\\\u003eABA Number :")
    index_end = text_to_parse.find("\\\\u003eAccount Length :")
    step1 = text_to_parse[index_start + 91: index_end]
    bank_aba = step1[0:step1.find("\\")]

    return bank_aba

def get_cust_accountnumber(text_to_parse):
    # Bank Name search reg exp
    account_number=''
    index_start = text_to_parse.find("\\\\u003eAccount Number :")
    index_end = text_to_parse.find('\\\\"ctl00_BankInfoRepeater_ctl00_0_Bank_AccountNumberManualAchLink_0')
    step1 = text_to_parse[index_start + 100: index_end]
    step2 = step1[0:step1.find("\\")]
    m = re.search('[0-9]+',step2)
    if m != None:
        account_number = m.group()
    else:
        account_number = step2

    return account_number