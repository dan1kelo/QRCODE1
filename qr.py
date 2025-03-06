from numpy import imag
import qrcode
from PIL import Image

data = input('Введите данные для генерации QR-кода: ')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

Image = qr.make_image(fill_color='red', back_color='blue')  # noqa: F811

imag.save('qr.png')
print('QR-код успешно сгенерирован и сохранен в формате в файле.png' )
