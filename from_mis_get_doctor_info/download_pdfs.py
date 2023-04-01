import requests

pdf_url = 'https://www.ishares.com/de/professionelle-anleger/de/literature/fact-sheet/susm-ishares-msci-em-sri-ucits-etf-fund-fact-sheet-de-de.pdf'
# res_size = requests.head(pdf_url)
# content_length = res_size.headers['Content-Length']

# 再用 pdf的大小去构建请求头
# headers = {
#     'Connection': 'keep-alive',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Range': f'bytes=0-{content_length}',
# }

resp = requests.get(pdf_url, stream=True, timeout=20)
print(resp.content)