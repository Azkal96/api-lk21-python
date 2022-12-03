from lk21.extractors.layarkaca21 import Layarkaca21
from lk21 import Bypass
import json
import app

def resjson(data):
    return json.dumps(data, indent=4, sort_keys=True)

scraper = Layarkaca21()
#search
def search(name):
    result = scraper.search(name)
    id = []
    image = []
    hasil = {}
    data = resjson(result)
    
    """
    for x, data in enumerate(result):
        #print(i['id'])
        #id.append(i['id'])
        image = meta(data['id'])
        result[x]['image'] = image
    """ 
        
        
    ''' test
    for i in id:
        image.append(meta(i))
    for x, data in enumerate(result):
        result[x]['image'] = image[x]
    '''
    
    #print(hasil)
    #print(data)
    print(len(result))
    return result
    #print(resjson(result))


#show
def show(id):
    return scraper.extract(id)
#show = scraper.extract(result[0])

#print(resjson(show))
def meta(id):
    data =scraper.extract(id)
    return data['metadata']['image']



def download(url):
    bypasser = Bypass()
    return bypasser.bypass_url(url)

def tess():
    return "tes"
