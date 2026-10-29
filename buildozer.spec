[app]
title = Gmail Pamekasan
package.name = gmailpamekasan
package.domain = com.pamekasan.gmail
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
p4a.branch = v2023.11.12
p4a.bootstrap = sdl2
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
