import random
import requests

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

# ذخیره در فایل
with open("sub_ready.txt", "w") as f:
    f.write(full_config)

print("ساب آماده شد: sub_ready.txt")
