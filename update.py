import random
import requests
import base64

# دانلود ساب اصلی
url = "https://raw.githubusercontent.com/Newv2ray/new/refs/heads/main/iSegaro.txt"
r = requests.get(url)
configs = r.text

# ساخت متادیتا رندوم
upload = random.randint(0, 200) * 1024*1024*1024
download = random.randint(0, 500) * 1024*1024*1024
total = 1099511627776
expire = 2546249531

meta = f"""//profile-update-interval: 1
//subscription-userinfo: upload={upload}; download={download}; total={total}; expire={expire}
"""

# فایل نهایی با متادیتا
full_config = meta + "\n" + configs

# تبدیل به Base64 (اگر کلاینت نیاز داشته باشه)
encoded = base64.b64encode(full_config.encode()).decode()

# ذخیره در فایل
with open("sub_ready.txt", "w") as f:
    f.write(encoded)

print("ساب آماده شد: sub_ready.txt")
