import urllib.request
import urllib

def getHtml(url):
    #create the object, assign it to a variable
    # proxy = urllib.request.ProxyHandler({'http': '127.0.0.1'})
    # construct a new opener using your proxy settings
    # opener = urllib.request.build_opener(proxy)
    # install the openen on the module-level
    # urllib.request.install_opener(opener)
    # page = urllib.request.urlopen(url)
    # html = page.read()
    # return html

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20161103 Firefox/23.0'}
    req = urllib.request.Request(url, headers)
    con = urllib.request.urlopen(req)
    html = con.read()
    return html
