import random
import time
import requests
from lxml import etree
import csv

datas = []
# 随机获得ua
def get_ua():
    first_num = random.randint(55, 62)
    third_num = random.randint(0, 3200)
    fourth_num = random.randint(0, 140)
    os_type = [
        '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
        '(Macintosh; Intel Mac OS X 10_12_6)'
    ]
    chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

    ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                   '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                  )
    return ua


headers = {
    'user-agent': get_ua(),
    "cookie": 'BMAP_SECKEY=9in0cwzAdnKG_ESstdqBQKA3n3irmTPvmjQvd6g6wvdaWoYGzHN1MDcTeehyHF6qwQvXYPXu9qdUU9HYsjFOmsk-rttMsc4v_mUxbyvaCa-JX0XOY4Qv0Ox0e_pYAxvLXTH-wGGo0Xe2xMn7oAMHfN_jhiZR_U2BVGAV-ThkVx9O0xEpmnubac0xFsP_hnoM; SECKEY_ABVK=dCmKxCAlA6+aXldfqqiaXKkUsdCKAOVmiTXKhu86Ilw%3D; lianjia_uuid=cab8d085-c2a8-4ab3-bf4b-1dd9f3772b62; ftkrc_=1175bf5c-0105-4caf-87da-a9f1adb5f1f9; lfrc_=f7f2eb97-67d5-4e33-80ab-fb4a3b5d532a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221926a7f85a226f-0f7c674b42cca4-4c657b58-1296000-1926a7f85a32abb%22%2C%22%24device_id%22%3A%221926a7f85a226f-0f7c674b42cca4-4c657b58-1296000-1926a7f85a32abb%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fother.php%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wysuzhou%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; crosSdkDT2019DeviceId=ceqchs-97pmhw-8bbdhjsuew9yf30-n78p83p6o; lianjia_ssid=0bfef1f1-4ef3-4185-a227-b30d1f9386e2; Hm_lvt_b160d5571570fd63c347b9d4ab5ca610=1728438276,1728447786,1729143746,1729472399; HMACCOUNT=E6A8E198D8008FF7; login_ucid=2000000144757586; lianjia_token=2.00158c909574b72e2b0421b9a48fd70dc1; lianjia_token_secure=2.00158c909574b72e2b0421b9a48fd70dc1; security_ticket=Lne27EmUsO7C2h3HpEmc5Z+ZwSeD7RPCw0FxfRa6aGSB9ScszaBOwmWUetlE0yl/y5ZOv80QW2+2MNZ0uRRLtbph1zbo1o0G9Fft/6ZoV3XqZ/WeNeNNM6JiCOZxz0p9b1x40iHcFIuZGwV7SWCifdGtPIs5NKfQKScqomU31TM=; digv_extends=%7B%22utmTrackId%22%3A%22%22%7D; select_city=320500; Hm_lpvt_b160d5571570fd63c347b9d4ab5ca610=1729473772; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiY2QxYjA0MTQ5OWU0MWJmYmM2NjczNDEyYjFjYTNkZGJhNzM5ZDc3MGM3ZTEzZmZjNjg4MzA0ZmEwYTgwM2Y2NDc2ZTcxOGI0YTkwYTZjYTMwYTA3NDMxZjBiMzk0NDc5NjNmMDQwMTVlYTdiYzAzNmNlZDEyOGRhNDZhZjQxZDA4OTBkODYwM2U4MzllZDkwMDYyZDY3MWViYmE4NGE4ZWMxNTRjZDA5OTdjNWNhNDM5NGQ5OGNlMGMyNWRiMjUwZWM5M2NmMzRjZDgzNGYxMDE0MThmY2JkYzM1MzAxNmQ3ZDU2MzllM2U4ZjU4M2RkNDIwZjAzOTZmYTRmYjQ3MFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIzOTkzZDQ4MlwifSIsInIiOiJodHRwczovL3N1LmtlLmNvbS9lcnNob3VmYW5nL2MyMzk4MjE4ODc5MjMwMTUvP3N1Zz0lRTklODclOTElRTUlQkUlQTElRTUlOEQlOEUlRTUlQkElOUMiLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='
}
for u in range(1, 11):
    urls = 'https://su.ke.com/ershoufang/pg{}c239821887922921/?sug=魅力花园'.format(u)
    res = requests.get(urls, headers=headers)
    res.encoding = res.apparent_encoding
    html = etree.HTML(res.text)
    # print(res.text)
    items = html.xpath('//li[@class="clear"]')

    for i in items:
        jiage = i.xpath('./div/div[2]/div[5]/div[1]/span/text()')[0]
        jiage2 = float(jiage.replace(' ', '').replace('\n', ''))
        url = i.xpath("./div/div[1]/a/@href")[0]
        t = i.xpath('./div/div[2]/div[2]/text()')[1]
        t2 = t.replace(' ', '').replace('\n', '')
        if '共9层' in t2:
            datas1 = (int(jiage2), t2, url)
            datas.append(datas1)

    time.sleep(2)

sorted_pairs = sorted(datas, key=lambda pair: pair[0])

file = open('data.csv', 'w', newline='', encoding='utf-8')
for datas in sorted_pairs:
    print(datas)
    writer = csv.writer(file)
    writer.writerows([datas])
print("CSV文件保存成功！")
