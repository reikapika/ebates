import requests
import json
import pprint # for testing purposes

# page number starts at 1 (I have to admit I'm not sure how to handle negative numbers like page=-1, and I tried it on browser it seems to has some sort of result instead of throwing errors)
url = 'http://api.viki.io/v4/videos.json?'
pages = 1

headers = {'User-Agent': 'Mozilla/5.0'}  # I had to hardcode this header to fix 403 request issues.
hd = {'true':0, 'false':0}
count_of_flags = 0


def get_json(url, pages, headers):
    params = {'app': '100250a',
              'page': str(pages),
              'per_page': '10',
              }
    r = requests.get(url=url, headers=headers, params=params)
    resp = r.json()
    lst_of_resps = resp['response']
    for response in lst_of_resps:
        flag = response.get('flags')
        if flag:
            global count_of_flags
            count_of_flags += 1
            if flag['hd'] == True:
                hd['true'] += 1
            elif flag['hd'] == False:
                hd['false'] += 1
        else:
            pass
    # print '#############', params
    return resp

    # pprint.pprint(resp)
    # print (resp['response'][0]['flags']['hd'])



if __name__ == '__main__':

    print '========'
    while get_json(url, pages, headers)['more'] != False:
        # print '+++++++', get_json(url, pages, headers)['more']
        pages += 1
        # print 'pages is now ', pages
        get_json(url, pages, headers)
    # get_json(url, pages, params, headers)

    print count_of_flags
    print hd
