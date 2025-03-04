import random;from curl_cffi import requests,CurlHttpVersion;from loguru import logger
def extract_content(text, markers):
    """
    从给定的字符串中提取指定标记之间的内容。

    参数:
    text (str): 要处理的字符串。
    markers (tuple): 一个包含两个元素的元组，第一个元素是起始标记，第二个元素是结束标记。

    返回:
    str: 起始和结束标记之间的内容。如果没有找到标记，则返回空字符串。
    """
    start_marker, end_marker = markers
    start_index = text.find(start_marker)
    if start_index == -1:
        return ''

    start_index += len(start_marker)
    end_index = text.find(end_marker, start_index)
    if end_index == -1:
        return ''

    return text[start_index:end_index]
class ins():
    def __init__(self,url,proxy):
        self.s = requests.Session()
        self.s.http_version = CurlHttpVersion.V1_1
        impersonate_v = ['chrome99', 'chrome100', 'chrome101', 'chrome104', 'chrome107', 'chrome110', 'chrome116',
                         'chrome119', 'chrome120', 'chrome123', 'chrome124']
        self.s.impersonate = random.choice(impersonate_v)
       # self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
        self.ua = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(100, 133)}.0.0.0 Safari/537.36'
        self.url=url
        self.proxies = {'https': proxy, 'http': proxy}
        self.s.proxies = self.proxies
        self.csrf_token=self.app_id=self.owner_id=self.media_id=self.shortcode=self.__spin_t=self.__spin_b=self.__spin_r=self.lsd=self.__hsi=self.__rev=None
        self.video_url=None
    def _ins_get(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'dpr': '1',
            'priority': 'u=0, i',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-full-version-list': '"Not(A:Brand";v="99.0.0.0", "Google Chrome";v="133.0.6943.142", "Chromium";v="133.0.6943.142"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': self.ua,
            'viewport-width': '912',
        }

        r=self.s.get(self.url,headers=headers)
       # logger.debug(r.text)
        self.__rev=extract_content(r.text,('data-btmanifest="','_main"'))
        self.__hsi=extract_content(r.text,('"cavalry_get_lid":"','",'))
        self.lsd=extract_content(r.text,('"token":"','"'))
        self.__spin_r=extract_content(r.text,('"__spin_r":',','))
        self.__spin_b = extract_content(r.text, ('"__spin_b":"', '",'))
        self.__spin_t = extract_content(r.text, ('"__spin_t":', ','))
        self.shortcode=extract_content(r.text,('"shortcode":"','",'))
        self.__hs=extract_content(r.text,('"haste_session":"','",'))
        #=======================================================
        self.media_id=extract_content(r.text,('"media_id":"','",'))
        self.owner_id=extract_content(r.text,('"media_owner_id":"','",'))
        self.app_id=extract_content(r.text,('"appId":"','",'))
        self.csrf_token=extract_content(r.text,('"csrf_token":"','"'))
        self.version_id=extract_content(r.text,('"versioningID":"','"'))
        logger.debug(self.media_id)
        if not self.media_id:
            raise Exception("输入的网址有误")
    def _get_ruling(self):
        headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'priority': 'u=1, i',
            'referer': self.url,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-full-version-list': '"Not(A:Brand";v="99.0.0.0", "Google Chrome";v="133.0.6943.142", "Chromium";v="133.0.6943.142"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': self.ua,
            'x-asbd-id': '359341',
            'x-csrftoken': self.csrf_token,
            'x-ig-app-id':  self.app_id,
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
            'x-web-session-id': '5izh7l:0qymj0:jgafh3',
           }

        params = {
            'media_id': self.media_id,
            'owner_id': self.owner_id,
        }
        r = self.s.get(
            'https://www.instagram.com/api/v1/web/get_ruling_for_media_content_logged_out/',params=params,headers=headers,)
        logger.debug(r.text)
    def _ins_post(self):
        headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'priority': 'u=1, i',
            'referer': self.url,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-full-version-list': '"Not(A:Brand";v="99.0.0.0", "Google Chrome";v="133.0.6943.142", "Chromium";v="133.0.6943.142"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': self.ua,
            'x-asbd-id': '359341',
            'x-bloks-version-id': self.version_id,
            'x-csrftoken':  self.csrf_token,
            'x-fb-friendly-name': 'PolarisPostActionLoadPostQueryQuery',
            'x-fb-lsd': self.lsd,
            'x-ig-app-id': self.app_id,
       }

        data = {
            'av': '0',
            '__d': 'www',
            '__user': '0',
            '__a': '1',
            '__req': 'c',
            '__hs': self.__hs,
            'dpr': '1',
            '__ccg': 'UNKNOWN',
            '__rev': self.__rev,
            '__s': '5izh7l:0qymj0:jgafh3',
            '__hsi': self.__hsi,
           # '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJw5ux609vCwjE1EE2Cw8G11wBz81s8hwGxu786a3a1YwBgao6C0Mo2swtUd8-U2zxe2GewGw9a361qw8Xxm16wa-0raazo7u3C2u2J0bS1LwTwKG1pg2fwxyo6O1FwlEcUed6goK2O4UrAwHxW1oxe17wGw9CubBKu9w',
            #'__csr': 'gjhcf8JkztYhKJFq_qjylijQG_FbF4oCVGJAKiVEyvjyXAJ2FEGX8uq4WG26uA499iqayaKV69g-KitojzdRHKXyeuK6VAV9V5AhoKESmaDgyQ4ULLy4eCyFbJ6J9ohiVozgOmHG5pUkCBDU8krz8gXhA7pojVEqQ9wLDxW00jooE2wwmVFBhhazE31w9C5F7wIx2aK1FBg1yEK0aOw59w3BU0D91xwaBk2i1ECwyw6ig623qy1PEq5EcUK3y31j0nUS0xjw8B0qEap4aw8219fCk800tcGw6Mw1vS',
            '__comet_req': '7',
            'lsd': self.lsd,
            'jazoest': '2852',
            '__spin_r': self.__spin_r,
            '__spin_b':self.__spin_b,
            '__spin_t': self.__spin_t,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'PolarisPostActionLoadPostQueryQuery',
            'variables': '{"shortcode":"目标","fetch_tagged_user_count":null,"hoisted_comment_id":null,"hoisted_reply_id":null}'.replace('目标',self.shortcode),
            'server_timestamps': 'true',
            'doc_id': '8845758582119845',
        }
        r = self.s.post('https://www.instagram.com/graphql/query',headers=headers, data=data,)
        video_url=r.text.replace(r'\u0026', '&')
       # logger.debug(video_url)
        self.video_url=extract_content(video_url,('"video_url":"','",'))
     #   if self.video_url:
        #    logger.success(self.video_url)
    def _video_get(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': self.ua,
        }
        r = self.s.post(self.video_url, headers=headers)
        logger.success(r.url)
    def _start(self):
        self._ins_get()
       # self._get_ruling()
        self._ins_post()

        return self.video_url
if __name__ == '__main__':
    url='https://www.instagram.com/reels/DGldfT_NtOf/'
    proxy='127.0.0.1:2080'
    v=ins(url,proxy)._start()
    logger.success(v)