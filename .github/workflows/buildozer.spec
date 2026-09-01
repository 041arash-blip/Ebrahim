[app]
# استفاده از نسخه پایدار API
android.api = 31
android.minapi = 21
# تنظیم NDK برای جلوگیری از دانلود خودکار معیوب
android.ndk = 25b
android.ndk_api = 24[app]
# (str) Title of your application
title = SmartRisk

# (str) Package name
package.name = smartrisk

# (str) Package domain (needed for android packaging)
package.domain = org.smartrisk

# (list) Application requirements
# حتماً نسخه kivy را ثابت نگه دار
requirements = python3,kivy==2.2.1

# (list) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (list) Target architectures - این بخش برای سازگاری با گوشی‌های جدید حیاتی است
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (int) NDK API level to target
android.ndk_api = 24

# (list) Include extensions
source.include_exts = py,png,jpg,kv,atlas,json
