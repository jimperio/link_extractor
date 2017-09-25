# link_extractor

McSweeney's doesn't have previous/next links for tagged articles, boo!

## spider.py

This collects article links, going page by page.

### Usage

```
$ scrapy runspider spider.py -o links.json
```

To do the same for other article lists, just replace the URL in `start_urls`.

## link_opener.py

This just goes through the links in `links.json`, opening the next one in a browser upon a keypress.
