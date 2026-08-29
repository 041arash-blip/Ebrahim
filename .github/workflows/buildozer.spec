[app]
title = Test App
package.name = testapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 33
android.minapi = 23
android.ndk = 25b
