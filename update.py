import random
import requests
import time

# دانلود ساب اصلی
url = "https://wanmeiwl3.xyz/gywl/945ef01f5d91f355cb3da871436232dc"
r = requests.get(url)
configs = r.text

# ساخت حجم رندوم با بایت
upload = random.randint(0, 200) * 1024 * 1024 * 1024
download = random.randint(0, 500) * 1024 * 1024 * 1024
total = 0
expire = int(time.time()) + 30*24*3600  # ۳۰ روز بعد

meta = f"""//profile-update-interval: 1
//subscription-userinfo: upload={upload}; download={download}; total={total}; expire={expire}
"""

# فایل نهایی با متادیتا
full_config = meta + "\n" + configs

# ذخیره در فایل
with open("sub_ready.txt", "w") as f:
    f.write(full_config)

print("ساب داینامیک آماده شد: sub_ready.txt")
