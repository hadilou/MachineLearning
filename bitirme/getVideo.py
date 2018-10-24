import cv2 as cv
import numpy as np
import argparse
import os.path
import sys

parser = argparse.ArgumentParser(description='Parse arguments')
parser.add_argument('--video', help = 'Path to video file.')
args = parser.parse_args()

if (args.video):
    #lets open the video file
    if not os.path.isfile(args.video):
        print("The video file",args.video ," doesnt exist")
        sys.exit(1)
    cap = cv.VideoCapture(args.video)
    outputFile = args.video[:-4]+'_mask_rcnn_out_py.avi'
else:
    #start video capturing
    cap = cv.VideoCapture(0)

#writing the output video with cv.videowriter
if(not args.image):
    vid_writer = cv.VideoWriter(outputFile, cv.VideoWriter_fourcc('M','J','P','G'), 28, (round(cap.get(cv.CAP_PROP_FRAME_WIDTH)),round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))))
    
while cv.waitKey(1) < 0:
        
    #video to frames
    containFrame, frame = cap.read()
    #stop if end of video    
    if not containFrame:
        print("Done extracting frames from video")
        print("Video saved at",outputFile)
        cv.waitKey(3000)
        break