import feapder


class AirSpiderDemo(feapder.AirSpider):
    def start_requests(self):
        url = "https://www.zoomeye.org/search"
        params = {
            "q": "%22Last-Modified%3A%20Tue%2C%2017%20May%202016%2010%3A22%3A58%20GMT%22%20%22Last-Modified%3A%20Thu%2C%2024%20Mar%202016%2005%3A58%3A21%20GMT%22%20%22Last-Modified%3A%20Thu%2C%2019%20Mar%202015%2009%3A24%3A20%20GMT%22%20%2Bcountry%3A%22US%22",
            "page": "11",
            "pageSize": "20",
            "t": "v4+v6+web"
        }
        yield feapder.Request(url, params=params, method="GET")

    def download_midware(self, request):
        request.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Cube-Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Im9tVkRTd3RwelRGNVpHWG80UjJfUmdTbmVxN1EiLCJlbWFpbCI6Ik5vbmUiLCJleHAiOjE2NTkwMTc2MDkuMH0.NOXUZP8EOKp26vlg7uofGJDb5RtPkClJcQMZB26ZL3M",
            "Connection": "keep-alive",
            "Referer": "https://www.zoomeye.org/searchResult?q=%22Last-Modified%3A%20Tue%2C%2017%20May%202016%2010%3A22%3A58%20GMT%22%20%22Last-Modified%3A%20Thu%2C%2024%20Mar%202016%2005%3A58%3A21%20GMT%22%20%22Last-Modified%3A%20Thu%2C%2019%20Mar%202015%2009%3A24%3A20%20GMT%22%20%2Bcountry%3A%22US%22&page=11&pageSize=20",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        }
        request.cookies = {
            "__jsluid_s": "32fbf34545995b6e620c371cf4e87867",
            "SECKEY_ABVK": "4fqi9mk9Uj9n2w7wWljPYnVvz6hemH7vRrf52H4KnLk%3D",
            "BMAP_SECKEY": "MIty7Q21CFqeH_AfLdIi4xrCIDR44S8gkkCbjDxS3YK97ZmtkT-Fz9w2WTVuyXIEFdiodYvLIyHz7n-vLmyuJW7lZsDns0WcmBDuioTUs_cP6tirD_ZNy_Pxx_JLDzgX6diwBIGRMeXPQTO5K5RzDY6wbsSwlByzZjX6_qub85AZ-PTrwzzWkyvSMhiPY9pR"
        }
        return request

    def parse(self, request, response):
        print(response.text)
        print(response)


if __name__ == "__main__":
    AirSpiderDemo(thread_count=1).start()
