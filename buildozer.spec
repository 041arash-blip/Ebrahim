[app]
title = SmartRisk
package.name = smartrisk
package.domain = org.test
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,urllib3,chardet,certifi,filetype,six,idna,requests
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 23
android.ndk = 25b
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
