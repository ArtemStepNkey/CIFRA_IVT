from captcha.image import ImageCaptcha
import random
import string
import base64
import io


def generate_captcha_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def generate_captcha_image(text):
    image_captcha = ImageCaptcha(width=200, height=70)

    image = image_captcha.generate_image(text)

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")

    img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return img_base64


print("BLYAT")
captcha_text = generate_captcha_text()
captcha_image_base64 = generate_captcha_image(captcha_text)
print(f"Captcha Image (Base64): {captcha_image_base64}")
