from bs4 import BeautifulSoup
import requests


def get_html(url):
    """
    получаем HTML
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.ok:  # 200 - True, another 403, 404 - False
        return r.text
    else:
        print(r.status_code)


def get_category(html):
    """
    Получаем ссылки на категории
    :param html:
    :return: list:
    """
    soup = BeautifulSoup(html, 'html.parser')
    catalog = soup.find('div', class_='catalog-menu__parent')
    items = catalog.find_all('a')
    urls = []
    for item in items:
        href = item.get('href')
        url = f'https://www.chitai-gorod.ru{href}'
        urls.append(url)
    return urls


def get_book_from_page(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    books = soup.find_all('div', class_='product-card__text product-card__row')
    products = []
    for item in books:
        products.append('https://www.chitai-gorod.ru' + item.find('a').get('href'))
    return products


def get_book_from_category(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find('div', class_='pagination').find_all('a')[-2].text
    get_book_from_page(url)
    books = []
    i = 1
    while i <= int(pagination):
        if i == 1:
            for book in get_book_from_page(url):
                print(book)
                books.append(book)
        else:
            page = url + '?page=' + str(i)
            for book in get_book_from_page(page):
                print(book)
                books.append(book)
        i += 1

    print(books)


def main():
    url = 'https://www.chitai-gorod.ru/catalog/books-18030'
    html = get_html(url)
    category_list = get_category(html)
    # for url in category_list:
    get_book_from_category('https://www.chitai-gorod.ru/catalog/books/hudozhestvennaya-literatura-110001')
    # get_book_from_page('https://www.chitai-gorod.ru/catalog/books/hudozhestvennaya-literatura-110001')


if __name__ == '__main__':
    main()
