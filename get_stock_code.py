import urllib
import urllib.request
import re

def getpage(path):
    data = urllib.request.urlopen(path).read().decode("gbk")
    return data

def getcode(data):
    sh_regex_str = "<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/[a-z][a-z]([6]\S\S.*?).html\">(.*?)\("
    sz_regex_str = "<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/[a-z][a-z]([0][0]\S\S.*?).html\">(.*?)\("
    cyb_regex_str = "<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/[a-z][a-z]([3][0][0]\S\S.*?).html\">(.*?)\("

    sh_pat = re.compile(sh_regex_str)
    sh_codelist = sh_pat.findall(data)

    sz_pat  = re.compile(sz_regex_str)
    sz_codelist = sz_pat.findall(data)

    cyb_pat = re.compile(cyb_regex_str)
    cyb_code_list = cyb_pat.findall(data)

    return sh_codelist, sz_codelist, cyb_code_list

path="http://quote.eastmoney.com/stocklist.html"
data = getpage(path)
sh_codelist, sz_codelist, cyb_code_list = getcode(data)

filepath = 'D:\\study\\py_finance\\'

i=0
j=0 
k=0
sh_list = filepath + "沪市股票.txt"
sh_file = open(sh_list, 'w+')
for code in sh_codelist:
    i += 1
    #print(code[0], code[1])
    sh_file.write(code[0])
    sh_file.write(' ')
    sh_file.write(code[1])
    sh_file.write('\n')
sh_file.close()
print("沪市共有股票{}支".format(i))


sz_list = filepath + "深市股票.txt"
sz_file = open(sz_list,'w+')
for code in sz_codelist:
    j += 1
    sz_file.write(code[0])
    sz_file.write(' ')
    sz_file.write(code[1])
    sz_file.write('\n')
sz_file.close()
print("深市共有股票{}支".format(j))

cyb_list = filepath + "创业板.txt"
cyb_file = open(cyb_list, 'w+')
for code in cyb_code_list:
    k += 1
    cyb_file.write(code[0])
    cyb_file.write(' ')
    cyb_file.write(code[1])
    cyb_file.write('\n')
cyb_file.close()
print('创业板共有股票{}支'.format(k))
