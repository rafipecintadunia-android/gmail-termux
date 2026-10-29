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

# (android) 
[app:android]
p4a.url = https://github.com/kivy/python-for-android
p4a.branch = master
