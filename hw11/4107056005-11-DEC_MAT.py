import os
import cv2
import numpy as np
import math
import csv


def getMIrgb(img):
    # 像素值
    # 與直接用mean結果相同
    MI = np.round(np.mean(img.reshape(-1, 3), axis=0), 2)
    return MI[2], MI[1], MI[0]
    # V = img.shape[0]
    # H = img.shape[1]
    # MI = []
    # for channel in range(3):
    #     I = 0
    #     for i in range(V):
    #         for j in range(H):
    #             I += img[i,j,channel]
    #     MI.append(I/(V*H))
    # return MI[0], MI[1], MI[2]


def getVH(arr):
    counts = np.bincount(arr, minlength=256)
    # 與直接算std相同
    VH = np.round(np.std(counts)**2, 2)
    # print(VH)

    # # 論文上的公式
    # vh = 0
    # for i in range(256):
    #     for j in range(256):
    #         vh += 0.5*(counts[i]-counts[j])**2
    # VH = np.round(vh/arr.shape[0], 2)
    # print(VH)

    # # 老師說同等的公式
    # vh1 = 0
    # for i in range(256):
    #     vh1 += counts[i]**2
    # vh1 = vh1/256

    # vh2 = 0
    # for i in range(256):
    #     vh2 += counts[i]
    # vh2 = (vh2/256)**2

    # VH = np.round(vh1 - vh2, 2)
    # print(VH)
    # print()

    return VH


def getVHrgb(img):
    # 值方圖bin 𝑧0, 𝑧1, … , 𝑧255之個數(count)。
    img = img.reshape(-1, 3)  # 是BGR
    return getVH(img[:, 2]), getVH(img[:, 1]), getVH(img[:, 0])


def getSE(arr):
    counts = np.bincount(arr, minlength=256)
    Pz = counts/arr.shape[0]
    SE = 0
    for i in range(256):
        if Pz[i] == 0:
            continue
        SE += Pz[i]*math.log(Pz[i], 2)
    return np.round(-SE, 6)


def getSErgb(img):
    img = img.reshape(-1, 3)
    return getSE(img[:, 2]), getSE(img[:, 1]), getSE(img[:, 0])


def getOutput(i, name, img):
    MIr, MIg, MIb = getMIrgb(img)
    VHr, VHg, VHb = getVHrgb(img)
    SEr, SEg, SEb = getSErgb(img)
    return [i, name, MIr, MIg, MIb, VHr, VHg, VHb, SEr, SEg, SEb]


def toCsvOutput(dir_name, csv_name):
    csv_text = [['No', 'Images', 'MIR', 'MIG', 'MIB',
                 'VHR', 'VHG', 'VHB', 'SER', 'SEG', 'SEB']]
    i = 1
    for name in os.listdir(dir_name):
        img = cv2.imread(dir_name+name, cv2.IMREAD_COLOR)
        csv_text.append(getOutput(i, name, img))
        i += 1

    with open(csv_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_text)


toCsvOutput("11-images/Origi_image/", "output11.csv")
toCsvOutput("11-images/Encry_image/", "output11_en.csv")
toCsvOutput("11-images/Decry_image/", "output11_de.csv")
