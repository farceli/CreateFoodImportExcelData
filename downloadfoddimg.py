import requests


def down(downloadname):
    cookies = {
        'BDqhfp': '%E5%93%88%E5%93%88%26%26-10-1undefined%26%260%26%261',
        'BIDUPSID': '9D638727D081658FF0A109065AB4AC33',
        'PSTM': '1688824781',
        'BAIDUID': '9D638727D081658F884EB60FD8845364:FG=1',
        'BAIDUID_BFESS': '9D638727D081658F884EB60FD8845364:FG=1',
        'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
        'BA_HECTOR': 'a025058gal0h25a524ah0g261ialn791p',
        'ZFY': 'o2:B4CQ0IszbXKf1pfBs3sM3TPqoODRgNza9fQYGCEKA:C',
        'delPer': '0',
        'PSINO': '6',
        'BDRCVFR[dG2JNJb_ajR]': 'mk3SLVN4HKm',
        'userFrom': 'www.baidu.com',
        'BDRCVFR[-pGxjrCMryR]': 'mk3SLVN4HKm',
        'cleanHistoryStatus': '0',
        'H_PS_PSSID': '36560_38643_38831_39027_39024_38877_38958_38955_39009_39012_38918_38973_38807_38986_38635_26350',
        'indexPageSugList': '%5B%22%E5%93%88%E5%93%88%22%2C%22%E5%9C%9F%E8%B1%86%E6%B3%A5%22%2C%22%E5%9C%9F%E8%B1%86%22%5D',
        'ab_sr': '1.0.1_MTRkMzQxYjYzNjg2OWYzMTQ3MzBlYzY4Mzg4MWM4ODczNGQzYzI5ZTFhNGVjYTMzOTdiMTNjNjU0YTY0NDQ5NzlhOWZiM2NmYzY2YTVjZDgzNjg0YmM5YWI2Y2M5ZTIxMzM1Yjc3MWNlNzE2YTNmNWZhNzAyYzI0NGY2YWI3Y2RlNTYxMWQ5YTAwOTc4ZGEwNzQwYWE2NjIxZTM0YjQ4Mw==',
    }

    headers = {
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        # 'Cookie': 'BDqhfp=%E5%93%88%E5%93%88%26%26-10-1undefined%26%260%26%261; BIDUPSID=9D638727D081658FF0A109065AB4AC33; PSTM=1688824781; BAIDUID=9D638727D081658F884EB60FD8845364:FG=1; BAIDUID_BFESS=9D638727D081658F884EB60FD8845364:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=a025058gal0h25a524ah0g261ialn791p; ZFY=o2:B4CQ0IszbXKf1pfBs3sM3TPqoODRgNza9fQYGCEKA:C; delPer=0; PSINO=6; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; cleanHistoryStatus=0; H_PS_PSSID=36560_38643_38831_39027_39024_38877_38958_38955_39009_39012_38918_38973_38807_38986_38635_26350; indexPageSugList=%5B%22%E5%93%88%E5%93%88%22%2C%22%E5%9C%9F%E8%B1%86%E6%B3%A5%22%2C%22%E5%9C%9F%E8%B1%86%22%5D; ab_sr=1.0.1_MTRkMzQxYjYzNjg2OWYzMTQ3MzBlYzY4Mzg4MWM4ODczNGQzYzI5ZTFhNGVjYTMzOTdiMTNjNjU0YTY0NDQ5NzlhOWZiM2NmYzY2YTVjZDgzNjg0YmM5YWI2Y2M5ZTIxMzM1Yjc3MWNlNzE2YTNmNWZhNzAyYzI0NGY2YWI3Y2RlNTYxMWQ5YTAwOTc4ZGEwNzQwYWE2NjIxZTM0YjQ4Mw==',
        'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1688919893311_R&pv=&ic=&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=MCw0LDEsMyw2LDUsMiw3LDgsOQ%3D%3D&ie=utf-8&sid=&word=%E5%93%88%E5%93%88',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'tn': 'resultjson_com',
        'logid': '12663946228419878430',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'fr': '',
        'word': downloadname,
        'queryWord': '哈哈',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '',
        'hd': '',
        'latest': '',
        'copyright': '',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'expermode': '',
        'nojc': '',
        'isAsync': '',
        'pn': '60',
        'rn': '30',
        'gsm': '3c',
        '1688919916500': '',
    }

    response = requests.get('https://image.baidu.com/search/acjson', params=params, cookies=cookies, headers=headers)
    for i in range(10):
        try:
            r = requests.get(url=response.json()['data'][i]['thumbURL'])
            with open('img/' + params['word'] + ".png", mode="wb") as f:
                f.write(r.content)  # 图片内容写入文件
            break
        except:
            if i == 9:
                print(params['word'] + '下载图片失败超过10次,不重试!')
