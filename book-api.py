import requests

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIxNjc3ODA4LCJpYXQiOjE3MzEyMjcxMjksImV4cCI6MTczMTIzMDcyOSwidHlwZSI6MjB9.bOe5YMcQ-hg_BUskiYZAID0AIGWZEXzlaDNma0OR1Dw'

url = 'https://web-gate.chitai-gorod.ru/api/v2/categories'


def get_json(url):
    """
    получаем JSON
    """
    headers = {'Authorization': f'Bearer {token}'}

    r = requests.get(url, headers=headers)
    if r.ok:  # 200 - True, another 403, 404 - False
        return r.json()
    else:
        print(r.status_code)


def get_books_id(json):
    books_id = json['data'][0]['id']
    return books_id


def get_books_category_id(books_id):
    books_category = [item for item in get_json(url)['data'] if item['attributes']['ancestorID'] == books_id]
    books_category_id = []
    for item in books_category:
        books_category_id.append(item['id'])
    return books_category_id


def main():
    books_id = get_books_id(get_json(url))
    for item in get_books_category_id(books_id):
        print(item)


if __name__ == '__main__':
    main()
