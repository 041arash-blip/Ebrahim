[app]

# (str) Title of your application
title = SmartRisk

# (str) Package name
package.name = smartrisk

# (str) Package domain (needed for android packaging)
package.domain = org.smartrisk

# (list) Application requirements
# استفاده از نسخه ثابت برای جلوگیری از تداخل در محیط GitHub Actions
requirements = python3,kivy==2.2.1

# (list) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (list) Target architectures
# اضافه کردن arm64-v8a برای سازگاری با گوشی‌های جدید و armeabi-v7a برای گوشی‌های قدیمی
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API
# تنظیم شده بر اساس آخرین نیازهای استور و پایداری بیلد
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (int) NDK API level to target
android.ndk_api = 24

# (str) Android NDK version
# تعیین نسخه دقیق NDK برای جلوگیری از دانلود خودکار نسخه‌های ناسازگار
android.ndk = 25b

# (list) Include extensions
source.include_exts = py,png,jpg,kv,atlas,json

# (int) Android SDK version
android.sdk = 31

# (bool) Use buildozer to build the app
# در GitHub Actions این مقدار معمولاً true است
android.accept_sdk_license = True
