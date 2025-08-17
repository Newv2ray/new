import random
import time

# مسیر فایل اصلی
file_path = "iSegaro.txt"

# خواندن محتوای اصلی
with open(file_path, "r") as f:
    configs = f.read()

# ساخت حجم رندوم با بایت
upload = random.randint(0, 200) * 1024 * 1024 * 1024
download = random.randint(0, 500) * 1024 * 1024 * 1024
total = 1099511627776
expire = int(time.time()) + 30*24*3600  # ۳۰ روز بعد

# خط متادیتا
meta = f"""//profile-update-interval: 1
//subscription-userinfo: upload={upload}; download={download}; total={total}; expire={expire}
"""

# اضافه کردن متادیتا به ابتدای فایل
full_config = meta + "\n" + configs

# ذخیره مجدد همان فایل
with open(file_path, "w") as f:
    f.write(full_config)

print("ساب اصلی با متادیتا داینامیک آماده شد!")
