from time import  sleep
from FLPK_navigator import burl, conn, pages, purl
from FLPK_extract import fprod_title, fprod_stock, frtng_avg, fprod_price, fdelvry_price, ffinal_price, fprod_img, fprod_warnty, fprod_url
url_list = []
final_prod_list = []

search_query = 'mac book'

max_items = 10
item_no = 0

burl , burl_list =  burl(search_query)
resp_status, response = conn(burl)
c_page, t_page, basejson = pages(response)
print len(basejson)
print c_page, ':',t_page
t_page = 1 # to limit the total pages to 1

if c_page == t_page:
    url_list = burl_list
else:
    for cp in range(c_page, t_page+1):
        url_list = purl(cp, t_page, search_query, burl)

#for item in url_list:
#    print item


    
for urlx in url_list:
    c_page, t_page, basejson = pages(response)
    for j in range(len(basejson)):
        #print 'jfor',j
        if j>0 and j<len(basejson):
                #print 'jif',j
                #print'len_basejson[j]',len(basejson[j]['widget']['data']['products'])
                try:
                    for items in basejson[j]['widget']['data']['products']:
                            prod_Title = fprod_title(items)
                            prod_Stock = fprod_stock(items)
                            rtng_Avg = frtng_avg(items)
                            prod_Price = fprod_price(items)
                            #print prod_Price
                            delvry_Price = fdelvry_price(items)
                            final_Price = ffinal_price(items)
                            img_url = fprod_img(items)
                            prod_Warnty = fprod_warnty(items)
                            prod_Url = fprod_url(items)
                            #print prod_Url
                            final_prod = {'Title':prod_Title,'Price':final_Price,'Image_url': img_url,'Prod_Url':prod_Url}
                            print final_prod
                            final_list = [prod_Title, final_Price, img_url, prod_Url]
                            final_prod_list.append(final_list)
                except:
                    print 'Handling key error'
    #sleep(5)

                    
print len(final_prod_list)
print final_prod_list
#for prod in final_prod_list:
#    print prod
