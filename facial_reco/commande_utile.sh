ffmpeg -i video/dimitri.mp4 dimitri/dimitri-%d.jpeg -f image2
ffmpeg -i video/negatif.mp4 negatif/negatif-%d.jpeg -f image2

export OPENCV_LOG_LEVEL=OFF