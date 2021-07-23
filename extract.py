import requests
import lxml.html
from PIL import Image








'''url = 'https://copy-brand.x.yupoo.com/albums/95226093?uid=1&isSubCate=false&referrercate=3508732'
with open('photo.jpg', 'wb') as f:
    f.write(get_photos(url))
    f.close()


image = Image.open('photo.jpg')
image.show() '''

photos_html = requests.get('https://copy-brand.x.yupoo.com/albums/95226093?uid=1')

photos = lxml.html.fromstring(photos_html.content)

lst_photos = []


for i in photos.xpath('.//div[@class="showalbum__children image__main"]//div//img/@src'):
    if len(i.split('/')[4]) == 8:
        lst_photos.append(i.split('/')[4])
    else:
        pass


print(lst_photos)