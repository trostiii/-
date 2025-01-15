import qrcode
from PIL import Image

# адрес сайта
url = "https://thelastgame.ru/"

# Создаем QR код
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# изображение QR кода
img = qr.make_image(fill='black', back_color='white')

# Отображение
img.show()
