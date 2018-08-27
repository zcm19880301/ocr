#this py is used for combine images
# -*- coding: utf-8 -*-
#usage
# python combine_image.py --first images\\SEA_1.jpg --second images\\SEA_2.jpg
from pyimagesearch.panorama_SIFT import Stitcher_SIFT
from pyimagesearch.panorama_SURF import  Stitcher_SURF
import imutils
import cv2
import numpy as np
import pandas as pd
import argparse
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="path to the first image")
ap.add_argument("-s", "--second", required=True,
	help="path to the second image")
args = vars(ap.parse_args())
#define some functions
def combine_image_with_SIFT(image_route1,image_route2):
    #####using SIFT to combine images#####
    # load the two images and resize them to have a width of 400 pixels
    # (for faster processing)
    imageA = cv2.imread(image_route1)
    imageB = cv2.imread(image_route2)
    imageA = imutils.resize(imageA, width=400)
    imageB = imutils.resize(imageB, width=400)
    # stitch the images together to create a panorama
    stitcher = Stitcher_SIFT()
    (result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
    return (result,vis,imageA,imageB)

def combine_image_with_SURF(image_route1,image_route2):
    #####using SIFT to combine images#####
    # load the two images and resize them to have a width of 400 pixels
    # (for faster processing)
    imageA = cv2.imread(image_route1)
    imageB = cv2.imread(image_route2)
    imageA = imutils.resize(imageA, width=400)
    imageB = imutils.resize(imageB, width=400)
    # stitch the images together to create a panorama
    stitcher_SURF = Stitcher_SURF()
    (result, vis) = stitcher_SURF.stitch([imageA, imageB], showMatches=True)
    return (result,vis,imageA,imageB)

def combine_image_with_direct(route1,route2):
    img1 = cv2.imread(route1)
    img2 = cv2.imread(route2)
    img1 = imutils.resize(img1, width=400)
    img2 = imutils.resize(img2, width=400)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # ====使用numpy的数组矩阵合并concatenate======
    # image = np.concatenate((gray1, gray2))  # 纵向连接=np.vstack((gray1, gray2))
    image = np.concatenate([gray1, gray2], axis=1)#横向连接
    # ====使用pandas数据集处理的连接concat========
    df1 = pd.DataFrame(gray1)
    df2 = pd.DataFrame(gray2)  # ndarray to dataframe
    #df = pd.concat([df1, df2])
    # 纵向连接,横向连接=pd.concat([df1, df2], axis=1)
    df=pd.concat([df1, df2], axis=1)
    image = np.array(df)  # dataframe to ndarray
    # =============
    return image
#
# def combine_image_with_cut_similar_area(route1,route2):
#     img1 = cv2.imread(route1)
#     img2 = cv2.imread(route2)
#     img1 = imutils.resize(img1, width=400)
#     img2 = imutils.resize(img2, width=400)
#
#
#     bf=cv2.BFMatcher(cv2.NORM_L2)


def combine_image_all(route1,route2):
    (result_SIFT, vis_SIFT, imageA, imageB) = combine_image_with_SIFT(route1, route2)
    (result_SURF, vis_SURF, imageA, imageB) = combine_image_with_SURF(route1, route2)
    # print(vis)
    image = combine_image_with_direct(route1, route2)
    # show the images
    cv2.imshow("Original Image A", imageA)
    cv2.imshow("Original Image B", imageB)
    cv2.imshow("Keypoint Matches with SIFT", vis_SIFT)
    cv2.imshow("SIFT Result", result_SIFT)
    cv2.imshow("Keypoint Matches with SURF", vis_SURF)
    cv2.imshow("SURF Result", result_SURF)
    cv2.imshow('Direct Combine Image', image)
    cv2.waitKey(0)


# def drawMatchesKnn_cv2(img1_gray, kp1, img2_gray, kp2, goodMatch):
#     h1, w1 = img1_gray.shape[:2]
#     h2, w2 = img2_gray.shape[:2]
#
#     vis = np.zeros((max(h1, h2), w1 + w2, 3), np.uint8)
#     vis[:h1, :w1] = img1_gray
#     vis[:h2, w1:w1 + w2] = img2_gray
#
#     p1 = [kpp.queryIdx for kpp in goodMatch]
#     p2 = [kpp.trainIdx for kpp in goodMatch]
#
#     post1 = np.int32([kp1[pp].pt for pp in p1])
#     post2 = np.int32([kp2[pp].pt for pp in p2]) + (w1, 0)
#
#     for (x1, y1), (x2, y2) in zip(post1, post2):
#         cv2.line(vis, (x1, y1), (x2, y2), (0, 0, 255))
#
#     cv2.namedWindow("match", cv2.WINDOW_NORMAL)
#     cv2.imshow("match", vis)


# route1='images\\grand_canyon_left_01.png'
# route2='images\\grand_canyon_right_01.png'
# route1='images\\SEA_1.png'
# route2='images\\SEA_2.png'
route1=args["first"]
route2=args["second"]
combine_image_all(route1,route2)
