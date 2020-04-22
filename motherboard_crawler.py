import re

import requests
from bs4 import BeautifulSoup


def crawler():
    resp = requests.get('https://www.coolpc.com.tw/eachview.php?IGrp=5')
    if resp.status_code != 200:
        print('coolpc website status code return %d' % resp.status_code)
        return

    # print('resp:', resp.text)
    soup = BeautifulSoup(resp.text)
    motherboard_list = soup.select('span')
    for motherboard in motherboard_list:
        print(motherboard.text)
        # match = re.match(r'(?P<brand>技嘉|微星|華擎)\s(?P<model>[a-zA-Z|\s|0-9|-]+)', motherboard.text)
        # if match:
        #     print('brand: %s , model: %s' % (match.group('brand'), match.group('model')))
    #         brand = match.group('brand')
    #         model = match.group('model')
    #     else:
    #         print('Bundle product => ', cpu.text)
    #
    #     match = re.search(r'NT(?P<price>[\d]+)', cpu.text)
    #
    #     if match:
    #         price = match.group('price')
    #     else:
    #         print('price is missing => ', cpu.text)


if __name__ == '__main__':
    crawler()
