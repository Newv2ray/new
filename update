import random
import requests

# لینک ساب گیت‌هاب
url = "https://raw.githubusercontent.com/Newv2ray/new/refs/heads/main/iSegaro.txt"
r = requests.get(url)
configs = r.text

# ساخت متادیتا رندوم
upload = random.randint(0, 200) * 1024*1024*1024
download = random.randint(0, 500) * 1024*1024*1024
total = 1099511627776  # 1 ترابایت
expire = 2546249531

meta = f"""//profile-update-interval: 1
//subscription-userinfo: upload={upload}; download={download}; total={total}; expire={expire}
"""

with open("sub_with_metadata.txt", "w") as f:
    f.write(meta + "\n" + configs)

print("sub_with_metadata.txt updated!")
