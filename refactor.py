import requests
import lxml.html


def get_collections_list(url):

    collections_html = requests.get(f'{url}')

    collections = lxml.html.fromstring(collections_html.content)

    lst_collections = []

    for i in collections.xpath('.//a/@href'):
        if "collections" in i:
            lst_collections.append(i.split('/')[2])
        else:
            pass
    return lst_collections


def get_products_list(cid):

    products_html = requests.get(f'https://copy-brand.x.yupoo.com/collections/{cid}')

    products = lxml.html.fromstring(products_html.content)

    lst_products = []

    # print('Album contido na coleção: ' + locals()['cid'])

    for i in products.xpath('.//a/@href'):
        if "albums/" in i:
            lst_products.append(i.split('/')[2].split('?')[0])
        else:
            pass
    return lst_products


def get_photos_list(aid):

    photos_html = requests.get(f'https://copy-brand.x.yupoo.com/albums/{aid}?uid=1')

    photos = lxml.html.fromstring(photos_html.content)

    lst_photos = []

    # print('Fotos contidas no album: ' + locals()['aid'])

    for i in photos.xpath('.//div[@class="showalbum__children image__main"]//div//img/@src'):
        if len(i.split('/')[4]) == 8:
            lst_photos.append(i.split('/')[4])
        else:
            pass
    return lst_photos


def get_photos(aid, cid, pid):

    url = f'https://copy-brand.x.yupoo.com/albums/{aid}?uid=1&isSubCate=false&referrercate={cid}'
    count = 0

    with requests.Session() as c:
        c.get(url)
        c.headers.update({'referer': url})
        res = c.get(f'https://photo.yupoo.com/copy-brand_v/{pid}/big.png')
        if res.status_code == 200:
            return res.content






    with open(f'photo_teste.jpg', 'wb') as f:
        f.write(get_photos())
        f.close()