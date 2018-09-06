import appex
from sys import argv
from webbrowser import open
from urllib.parse import quote

if __name__ == '__main__':
  if not appex.is_running_extension():
    # With argument
    word = argv[1]

  else:
    # No argument
    word = appex.get_text()
    if not word:
      print('No input.')
      sys.exit()

  url = 'eureca://paste?go=true&str='
  url = url + quote(word)
  open(url)

