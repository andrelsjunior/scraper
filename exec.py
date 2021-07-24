from refactor import get_products_list, get_photos_list, get_collections_list, get_photos


def iter_photos(url):

    coll = get_collections_list(url)

    alb = []
    count = 0
    pics = []

    for collection in coll:
        if len(alb) == 5:
            count = 0
            pass
        else:
            alb.append(get_products_list(collection))
            print(f'{collection} {count}')
            count += 1

    print('Chegamos à: ' + str(len(alb)) + ' resultados')

    for album in alb:
        for produto in album:
            if len(pics) == 5:
                count = 0
                continue
            else:
                pics.append(get_photos_list(produto))
                print(f'{produto} {count}')
                count += 1

    return pics, alb, coll


pics, alb, coll = iter_photos('https://copy-brand.x.yupoo.com/albums')
print(f'listas contidas: {pics}')
#
#
# with open('photo_teste_2.jpg', 'wb') as f:
#     f.write(get_photos(79583795, 3210698, 'a00cee22'))
#     f.close()