from bs4 import BeautifulSoup

html_doc = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>기초 웹 크롤링</title>
</head>
<body>
    크롤링을 해봅시다.
</body>
</html>
'''

soup = BeautifulSoup(html_doc, 'html.parser')
head = soup.find('head')
body = soup.find('body')
print(body)

