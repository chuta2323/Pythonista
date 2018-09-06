import appex
from urllib.parse import quote
from webbrowser import open

TWITTER_ID = 'Input your ID'

if __name__ == '__main__':
  if appex.is_running_extension():
    # No argument
    info = appex.get_web_page_info()
    title = info['title']
    url = info['url']
    
    # Create scheme
    scheme = 'feather://' + TWITTER_ID + '/post?text='
    text = title + ' - ' + url
    scheme = scheme + quote(text)

    open(scheme)

