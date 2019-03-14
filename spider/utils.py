# coding=utf8
import logging
import random
import re
import sys
import threading

import requests
from requests.auth import HTTPDigestAuth
import hashlib, json

reload(sys)
sys.setdefaultencoding('utf-8')

h5_ua = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36'
pc_ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'

class ThreadLocalSession(threading.local, requests.Session):
    pass

session = ThreadLocalSession()


def parse_auth_url(url):
    matched = re.match('^(https?://)(.+?):(.+?)@(.+)$', url)
    if matched:
        prefix, username, password, suffix = matched.groups()
        auth = HTTPDigestAuth(username, password)
        url = prefix + suffix
        return auth, url
    return None, url


def crawl(url, ua_used=True, h5=False, data=None, headers=None, cookies=None, auth=None, proxy=None, method='get',
          allow_redirects=True,
          timeout=15, need_return_headers=False, need_return_cookies=False, raise_exception=False, clear_cookies=False):
    headers = headers if headers is not None else {}
    cookies = cookies if cookies else {}
    if ua_used:
        headers['User-Agent'] = h5_ua if h5 else pc_ua
    if auth is None:
        auth, url = parse_auth_url(url)
    proxy_start = random.randrange(1000)
    for retry in range(3):
        if clear_cookies:
            session.cookies.clear()
        if isinstance(proxy, (list, tuple)):
            current_proxy = proxy[(proxy_start + retry) % len(proxy)]
        else:
            current_proxy = proxy
        try:
            logging.info('retry=%d h5=%s proxy=%s url=%s ' % (retry, h5, current_proxy, url))
            proxies = None
            if current_proxy:
                proxies = {"http": current_proxy, 'https': current_proxy}
            if method == 'post':
                rsp = session.post(url, proxies=proxies, headers=headers, cookies=cookies, data=data, auth=auth,
                                   allow_redirects=allow_redirects,
                                   timeout=timeout)
            elif method == 'put':
                rsp = session.put(url, proxies=proxies, headers=headers, cookies=cookies, data=data, auth=auth,
                                  allow_redirects=allow_redirects,
                                  timeout=timeout)
            else:
                rsp = session.get(url, proxies=proxies, headers=headers, cookies=cookies, data=data, auth=auth,
                                  allow_redirects=allow_redirects,
                                  timeout=timeout)
            if 400 <= rsp.status_code <= 499:
                raise Exception('get status_code %d %s' % (rsp.status_code, url))
            content = rsp.content
            headers = rsp.headers
            cookies = rsp.cookies
            if need_return_headers and need_return_cookies:
                return content, headers, cookies
            if need_return_headers:
                return content, headers
            if need_return_cookies:
                return content, cookies
            return content
        except Exception as e:
            if raise_exception:
                raise
            logging.warning("Crawl while Server Error reason is %s", e)

    if raise_exception:
        raise Exception()
    if need_return_headers and need_return_cookies:
        return None, None, None
    if need_return_headers or need_return_cookies:
        return None, None
    return None

def get_md5(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    return hl.hexdigest()


# 将dict数据保存到json
def store_json(file_name, data):
    with open(file_name, 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))


# 将json文件中的数据读取到dict
def load_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data


# 尽量等长分割一维数组(最后一组可能会更短)
def list_cut(x, batch_num):
    batch_size = (len(x) / batch_num) + 1
    result = []
    for i in range(batch_num):
        if i + 1 == batch_num:
            result.append(x[i * batch_size:])
        else:
            result.append(x[i * batch_size:(i + 1) * batch_size])
    return result

def read_redit(_redit, key,):
    try:
        value = _redit.get(key) or None
    except:
        logging.error("redis failed, get(x) error.")
        value = None
    return value


def put_data2redit(_redit,key,value):
    try:
        _redit.setex(key, value, 10 * 365 * 86400)
    except:
        logging.error("redis failed, setex(x) error.")

