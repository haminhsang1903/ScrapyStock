import requests

cookies = {
    '_ga': 'GA1.3.1850311231.1604374787',
    '_gid': 'GA1.3.126066724.1604835253',
    'finance_viewedstock': 'TCB,',
    'language': 'vi-VN',
    'isShowLogin': 'true',
    '__gads': 'ID=b9a6aa2ec92c012a-22d43ad087c400d2:T=1604374787:RT=1604421617:S=ALNI_MYhVd6D4yrPRDjQjaMs7ulx3uBc_A',
    'cto_bundle': 'DewZc19BNXk4cTlhOEF2T2gwQnc0dmx2U1RQdjFqWUdVdnpBV2NtWUNEelQ0TndoT3F1ZU5pVmVpU2pzQ0hCJTJCZVYlMkIxRVp5a1cyeHZWSVh6QmhLSmVQJTJCZFVnUlJqRmlLJTJCNkdnVCUyQk9VSVdwMlZWd0swUFVSTmNGV3pRdnJUR1ZmRFRoYmU',
    'MarketGidStorage': '%7B%220%22%3A%7B%22svspr%22%3A%22https%3A%2F%2Ffinance.vietstock.vn%2FVNM%2Ftai-chinh.htm%3Ftab%3DCTKH%22%2C%22svsds%22%3A1%2C%22TejndEEDj%22%3A%22QMJVVaim5%22%7D%2C%22C756865%22%3A%7B%22page%22%3A11%2C%22time%22%3A1604407451284%7D%7D',
    '__RequestVerificationToken': 'hedG-j2MulLsj-tUkbOZwLjd4gt1u4o6MAUxyIhJowghsLsMhBgyKIMVYf4SxSHgnVcMsVFff_d76N8WHIghn474w9jQhOTP0SfzajcAU6Y1',
    '__oaue': 'false',
    'ASP.NET_SessionId': 'upunkqc05wtmn1nzzcx40xga',
    'adAsiaUserIp': '115.77.123.31',
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'finance.vietstock.vn',
    'Origin': 'https://finance.vietstock.vn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
    'Connection': 'keep-alive',
    'Referer': 'https://finance.vietstock.vn/TCB/thong-ke-giao-dich.htm?grid=market',
    'Content-Length': '207',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
  'Code': 'TCB',
  'OrderBy': '',
  'OrderDirection': 'desc',
  'PageIndex': '1',
  'PageSize': '10',
  'FromDate': '2020-11-01',
  'ToDate': '2020-11-08',
  'ExportType': 'default',
  'Cols': 'TKLGD,TGTGD,VHTT,GD3,TGG,TGPTG,BQM,BQB,KLGDKL,GTGDKL',
  'ExchangeID': '1'
}
response = requests.post('https://finance.vietstock.vn/data/gettradingresult', headers=headers, cookies=cookies, data=data)

print(response.json())