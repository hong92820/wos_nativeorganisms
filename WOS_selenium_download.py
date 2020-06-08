from selenium import webdriver

import re
import time

link = 'https://ets.webofknowledge.com/ETS/ets.do?mark_from=1&product=UA&colName=WOS&displayUsageInfo=true&parentQid=2&rurl=https%253A%252F%252Fapps.webofknowledge.com%252Fsummary.do%253Fproduct%253DWOS%2526search_mode%253DAdvancedSearch%2526doc%253D1%2526qid%253D2%2526SID%253DF16AhP7FdxFqmjGKXLI&mark_to=500&filters=HIGHLY_CITED%20HOT_PAPER%20OPEN_ACCESS%20PMID%20USAGEIND%20AUTHORSIDENTIFIERS%20ACCESSION_NUM%20FUNDING%20SUBJECT_CATEGORY%20JCR_CATEGORY%20LANG%20IDS%20PAGEC%20SABBR%20CITREFC%20ISSN%20PUBINFO%20KEYWORDS%20CITTIMES%20ADDRS%20CONFERENCE_SPONSORS%20DOCTYPE%20ABSTRACT%20CONFERENCE_INFO%20SOURCE%20TITLE%20AUTHORS%20%20&qid=3&SID=F16AhP7FdxFqmjGKXLI&totalMarked=500&action=saveToFile&sortBy=PY.D;LD.D;SO.A;VL.D;PG.A;AU.A&logEventQid=2&displayTimesCited=true&displayCitedRefs=true&fileOpt=fieldtagged&UserIDForSaveToRID=2011324173'
result = 127286

browser = webdriver.Chrome()

for i in range (1, result+1, 500):
    link = re.sub('mark_from=[0-9]+', 'mark_from=' + str(i), link, 1)
    link = re.sub('mark_to=[0-9]+', 'mark_to=' + str(i+499), link, 1)
    browser.get(link)
    time.sleep(2)

link = re.sub('mark_from=[0-9]+', 'mark_from=' + str(i), link, 1)
link = re.sub('mark_to=[0-9]+', 'mark_to=' + str(result), link, 1)



browser.close()
