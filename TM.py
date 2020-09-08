import requests
import re
import time


goods = input("请输入商品名: ")  # 搜索关键字
depth = 2  # 搜索深度为2，即爬取第1页，第2页
start_url = 'https://list.tmall.com/search_product.htm?q='+goods+'&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton'
infoList = []
hd = {  'authority': 's.taobao.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'referer': 'https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': 'cna=v1iCFj5e5HUCAWp5DX0quDsv; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; tracknick=shaon1992; tg=0; miid=1632897152788742981; UM_distinctid=16f88fb7505647-021c8a4768c455-c383f64-1fa400-16f88fb7506a97; lgc=shaon1992; enc=bTD3YQaxUUPgMwDFOzNQb7gq%2FH5pgW5AsroLZZNZWAol%2F%2Bq%2FnesRJw6MtTZsB9Nr694mCB7jvjlmb3PQSo3OVA%3D%3D; mt=ci=23_1; t=f85195559e028f48ad19815224752b39; _m_h5_tk=f61d8dd502cb28f5d6db372130b5d45e_1584960506160; _m_h5_tk_enc=a36c7546e631f9f340b6dc44c895175f; tfstk=cC6GBWq-X1R_yzhqNf91DL3u9YeRZEM2rtWCLORQY8cl6tBFilcEa5iTxFbGHj1..; uc3=id2=UUGq1RsrN4lVRg%3D%3D&vt3=F8dBxd9gD5LRH%2BhN35Q%3D&nk2=EFY19v%2BIN9jj&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; uc4=id4=0%40U2OdIeIjT8V0ugGcC5lw5EpiSlBQ&nk4=0%40Eo9LPCpw%2BKOBalOW5iTVFcrXPNw%3D; _cc_=UtASsssmfA%3D%3D; sgcookie=EHwF2Jp4HScWqZwBHzOfu; cookie2=157515f6c454549c82338d09b1970007; _tb_token_=76fe5a3ffb3e8; v=0; alitrackid=item.taobao.com; lastalitrackid=www.taobao.com; uc1=cookie14=UoTUP2D5qVEqyw%3D%3D; JSESSIONID=C3FB11DB6A138C4FEBEEB6CF68BA9B04; l=dBMg_kwlqqvYK87zKOCwdykmBh_OLIRfguyeoWKwi_5Q4_L1lU7OoyHxmEp6cjWAMIxH4cjscS2tZeJgJso4ne2e4AadZxDDB; isg=BBQUyTYnNrtGL6HwNFoBuS4w5VKGbThXLBPCq671_x8imbXjxXzw5_dbmZEBYXCv',
  }
for j in range(depth):  # 对每一个页面进行处理，使用for循环
    try:
        url = start_url+ '&S=' + str(60 * j)
        try:
            r = requests.get(url, headers=hd, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding  # 把获取到的页面信息 替换成utf-8信息，这样就不会乱码
            print(r.status_code)
            html = r.text
            print(r.url)
            #print(r.text)
        except:
            print("抓取异常")
        try:
            plt = re.findall(r'<b>&yen;</b>.*?\.\d\d', html)  # 获取商品价格
            tlt = re.findall(r'target=\"_blank\" title=\".*?\"', html)   #商品名
            jlt =  re.findall(r'data-ks-lazyload=  "//.+?.jpg', html)   #商品图片地址
            wlt = re.findall(r'<a href="//.+?" target="_blank" title="', html)   #商品链接
            for i in range(len(plt)):
                price = plt[i].split('/b>')[1]
                title = tlt[i].split('e="')[1].split('"')[0]
                img = jlt[i].split('"')[1]
                spid = wlt[i].split('f="')[1].split('" ta')[0]
                infoList.append([price, title, img, spid])
        except:
            print(" ")
            #print("分析异常")
    except:
        continue  # 如果某一个页面解析出了entity，那么继续解析下一个页面。
    time.sleep(2)

tplt = "{:^10}\t{:^10}\t{:^40}\t{:^60}\t{:^60}"
print(start_url)
print(tplt.format("序号", "价格","商品名称","商品图片","商品链接"))
count = 0
for g in infoList:
    count = count + 1
    print(tplt.format(count, g[0], g[1],'https:'+g[2],'https:'+ g[3]))  # 打印商品信息
with open("tianmao.txt","w",encoding='utf-8') as f:                                                   #设置文件对象
    for i in infoList:                                                                 #对于双层列表中的数据
        i = str(i).strip('[').strip(']').replace(',','').replace('\'','')+'\n'  #将其中每一个列表规范化成字符串
        f.write(i)
