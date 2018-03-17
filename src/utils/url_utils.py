def format(url, https = False):
  if 'http://' in url or 'https://' in url:
    return url
  elif https:
    return 'https://{}'.format(url)
  else:
    return 'http://{}'.format(url)
