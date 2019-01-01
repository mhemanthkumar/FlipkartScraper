import json
import requests
import re
burl_list = []
purl_list = []



headers={'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10_10_1)AppleWebKit/537.36(KHTML,likeGecko)Chrome/39.0.2171.95Safari/537.36'}



def burl(sq):
    b00 = 'https://www.flipkart.com/search?q='
    b01=  re.sub(' ','%20',sq)
    b11 = '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    burl = b00+b01+b11
    #print burl
    burl_list.append(burl)
    return burl, burl_list

def conn(url):
    try:
        response = requests.get(url, headers=headers)
        resp_status = re.match(r'(.*?)\[(.*?)\]>', str(response)).group(2)
        if int(resp_status) == 200:
            return 'Connection OK code:200', response
        else:
            return resp_status
    except:
        print "Check Internet Connection"
def pages(response):
    reg_var = re.compile('window.__INITIAL_STATE__ = ({.*?});', re.DOTALL)
    matches = reg_var.search(response.content)
    jdata = matches.group(1)
    jsonData = json.loads(jdata)
    basejson = jsonData['pageDataV4']['page']['data']['10003']
    # print len(basejson) # no. of items = len(basejson -1)
    try:
        current_page = jsonData['pageDataV4']['page']['data']['10003'][len(basejson) - 1]['widget']['data']['currentPage']
    except:
        current_page = 1
        #print 'Single Page'
    try:
        total_page = jsonData['pageDataV4']['page']['data']['10003'][len(basejson) - 1]['widget']['data']['totalPages']
    except:
        total_page = 1
        #print "Single Page"
    return current_page, total_page, basejson



def purl(cp, tp, sq, burl):
    if cp == 1:
        purl_list.append(burl)
    cp = cp + 1
    np = str(cp)
    #print np
    if cp <= tp:
        p00 = 'https://www.flipkart.com/search?q='
        p01 = re.sub(' ', '+', sq)
        p11 = '&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
        p22 = '&page='
        pno = np
        purl = p00 + p01 + p11 + p22 + pno
        purl_list.append(purl)
        #print purl
    return purl_list

