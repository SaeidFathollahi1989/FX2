
# app.py

import math

# اطلاعات نمونه برای EUR/USD
current_price = 1.14038
target_price = 1.14370
atr = 0.0050  # 50 pip
p0 = 1.13500  # قیمت مرکزی چرخه
pi = math.pi

# محاسبه زاویه موقعیت قیمت
try:
    normalized = (current_price - p0) / atr
    if abs(normalized) <= 1:
        theta_rad = math.asin(normalized)
        theta_deg = math.degrees(theta_rad)
        full_theta = 180 + theta_deg  # چون مرکز چرخه 180° است
    else:
        full_theta = 'خارج از دامنه موج'

    print("زاویه فعلی:", full_theta)
except Exception as e:
    print("خطا در محاسبه:", e)

# محاسبه زمان رسیدن به سقف (فرض سرعت میانگین 5 پیپ/ساعت)
remaining_pips = (target_price - current_price) * 10000
speed_per_hour = 5  # pip/hour
if remaining_pips > 0:
    estimated_hours = remaining_pips / speed_per_hour
    print(f"زمان تقریبی رسیدن به سقف {target_price}: حدود {estimated_hours:.1f} ساعت")
else:
    print("قیمت فعلی بالاتر از هدف است.")
