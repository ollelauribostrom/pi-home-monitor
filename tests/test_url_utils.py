from src.utils import url_utils as url

def test_url_format_https_protocol():
  raw = 'https://test.com' 
  assert url.format(raw) == raw

def test_url_format_http_protocol():
  raw = 'http://test.com' 
  assert url.format(raw) == raw

def test_url_format_no_protocol():
  raw = 'test.com' 
  assert url.format(raw) == 'http://test.com'

def test_url_format_no_protocol_https():
  raw = 'test.com' 
  assert url.format(raw, https = True) == 'https://test.com'