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
        print '---{0}---'.format(m.group())
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
