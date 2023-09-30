[app]
title = hanh
package.name = hanh
package.domain = org.test
#package.domain = org.kivy.hanh21duc@gmail.com
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
#source.include_patterns = .names, .pb, .pbtxt
version = 0.1
#version.regex =v7.1
requirements = python3,kivy,kivymd,opencv,libtool
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
#services = camera:ngduchanh1.ddns.net:554,telepot:"6275415240:AAF3yDdT45-VIn8GdBrQUHH0XmtMXo0MC28",telepot:5877612764
#services = NAME:ngduchanh1.ddns.net:554
# Android specific
fullscreen = 0
#android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18),CAMERA
android.permissions = INTERNET,CAMERA,READ_EXTERNAL_STORAGE
android.allow_backup = True
#services =NAME:ACTION_IMAGE_CAPTURE,NAME2:REQUESt_CODE_CAMERA
android.archs = arm64-v8a, armeabi-v7a
#android.whitelist_src ="rtsp://admin:admin1234@ngduchanh1.ddns.net:554/cam/realmonitor?channel=1&subtype=0"
#android.blacklist_src =
#android.provider="rtsp://admin:admin1234@ngduchanh1.ddns.net:554/cam/realmonitor?channel=1&subtype=0"

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
