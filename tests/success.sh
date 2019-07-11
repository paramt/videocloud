#!/bin/sh

videos=(https://www.youtube.com/watch\?v=MHTizZ_XcUM)

for video in "${videos[@]}"
do
    # Defaults
    videocloud --url=$video

    # Custom filepath (PNG)
    videocloud --url=$video --filepath=1.png

    # Custom filepath (JPG)
    videocloud --url=$video --filepath=2.jpg

    # Custom filepath (JPEG)
    videocloud --url=$video --filepath=3.jpeg

    # Custom filepath (BMP)
    videocloud --url=$video --filepath=4.bmp

    # Custom language code (English)
    videocloud --url=$video --filepath=5.png --language=en

    # Custom language code (Spanish)
    videocloud --url=$video --filepath=6.png --language=es

    # Custom font (Noto Sans)
    videocloud --url=$video --filepath=7.png --font=https://github.com/paramt/videocloud/blob/master/assets/fonts/NotoSans/NotoSans.ttf?raw=true

    # Custom font (Press Start 2P)
    videocloud --url=$video --filepath=8.png --font=https://github.com/paramt/videocloud/blob/master/assets/fonts/PressStart2P/PressStart2P-Regular.ttf\?raw=true

    # Custom mask (Cloud)
    videocloud --url=$video --filepath=9.png --mask=https://github.com/paramt/videocloud/blob/master/assets/masks/cloud.png\?raw=true

    # Custom mask (YouTube logo)
    videocloud --url=$video --filepath=10.png --mask=https://github.com/paramt/videocloud/blob/master/assets/masks/youtube.jpg\?raw=true
done
