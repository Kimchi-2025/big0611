from bs4 import BeautifulSoup

html_doc = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>기초 웹 크롤링 따라하기</title>
    </head>
    <body>
        <div> 첫 번째 부분</div>
        <div> 두 번째 부분</div>
    </body>
    </html>
    '''

soup = BeautifulSoup(html_doc, 'html.parser')
body = soup.find('body')
div1 = soup.find('div')
div_all = soup.find_all('div')
print(div_all[1].text)


