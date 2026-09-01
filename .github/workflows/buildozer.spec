[app]
title = SmartRisk
package.name = smartrisk
package.domain = org.smartrisk

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,json

# کتابخانه‌های لازم (پایتون، کیوی و کدهای کمکی)
requirements = python3,kivy==2.2.1,requests,urllib3,charset-normalizer,idna,certifi

# تنظیمات معماری و نسخه‌های اندروید (بهینه‌سازی شده برای جلوگیری از خطا)
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

# توضیحات مربوط به فایل‌های دیگر در buildozer.spec که تغییری نکرده‌اند
# ... (بقیه تنظیمات شما که تغییری نکرده است)
