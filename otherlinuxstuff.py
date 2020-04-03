
# Creating videos from command line
ffmpeg -start_number 0  -r 16 -f image2 -s 1920x1080 -i snap_%6d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" output.mp4

# Trying to locate files in directories [may not work...]
grep --include=\*.py -rnw '/home/louis_couston/workdir/' -e "Gatherv"
find -name "data_0.20*"
