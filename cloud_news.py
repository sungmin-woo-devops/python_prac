import requests

# Top 10 Cloud Computing News Sites
media_dict = {
    'TechCrunch': 'https://techcrunch.com/',
    'ZDNet': 'https://www.zdnet.com/',
    'CIO': 'https://www.cio.com/',
    'InfoWorld': 'https://www.infoworld.com/',
    'CloudTech': 'https://www.cloudcomputing-news.net/',
    'Cloudwards': 'https://www.cloudwards.net/',
    'The New Stack': 'https://thenewstack.io/',
    'CloudTechReview': 'https://www.cloudtechreview.com/',
    #'CloudTweaks': 'https://cloudtweaks.com/',
    'CloudTech360': 'https://cloudtech360.com/'
}

# Check status code of each site
for url in media_dict.values():
    response = requests.get(url)
    #print(response.status_code)

    if response == 200:
        print('Success!')
    elif response == 301:
        print('Moved permanently.')
    elif response == 302:
        print('Moved temporarily.')
    elif response == 400:
        print('Bad request.')
    elif response == 403:
        print('Forbidden.')
    elif response == 404:
        print('Not found.')
    elif response == 500:
        print('Server error.')
    elif response == 503:
        print('Service unavailable.')
    elif response == 504:
        print('Gateway timeout.')
    else:    
        print('Unknown error.')

# Output: