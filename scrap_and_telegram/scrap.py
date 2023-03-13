from bs4 import BeautifulSoup
import requests

def crawling(website_link, link_class):
    '''
    Args: website_link = stringl link of website to be crawled
          link_class = string; class name for job link on website
    Returns: job_link = list; list of jobs
    '''

    # get content of website and parse it
    website_request = requests.get(website_link, timeout=5)
    website_content = BeautifulSoup

   # extract job description
   jobs_link = website_content.find_all(class_ = link_class)
   return jobs_link
