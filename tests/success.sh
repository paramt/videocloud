#!/bin/sh

videos=(https://www.youtube.com/watch\?v=MHTizZ_XcUM)

for video in "${videos[@]}"
do
    # Defaults
    videocloud $video

    # Custom filepath (PNG)
    videocloud $video 1.png

    # Custom filepath (JPG)
    videocloud $video 2.jpg

    # Custom filepath (JPEG)
    videocloud $video 3.jpeg

    # Custom filepath (BMP)
    videocloud $video 4.bmp

    # Custom language code (English)
    videocloud $video 5.png en

    # Custom language code (Spanish)
    videocloud $video 6.png es

    # Custom font (Noto Sans)
    videocloud $video 7.png en \
    https://github.com/paramt/videocloud/blob/master/assets/fonts/NotoSans/NotoSans.ttf?raw=true

    # Custom font (Press Start 2P)
    videocloud $video 7.png en \
    https://github.com/paramt/videocloud/blob/master/assets/fonts/PressStart2P/PressStart2P-Regular.ttf\?raw=true
done
