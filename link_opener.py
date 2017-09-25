#!/usr/bin/env python

import json
import webbrowser


def main():
  with open('links.json') as f:
    link_data = f.read()

  links = json.loads(link_data)

  print 'Press Enter to open next article!'

  while links:
    raw_input()
    link = links.pop()
    full_url = 'https://www.mcsweeneys.net' + link['url']
    print 'Opening {}...'.format(full_url)
    webbrowser.open(full_url)

  print 'All done!'


if __name__ == "__main__":
  main()
