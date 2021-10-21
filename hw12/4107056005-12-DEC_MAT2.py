import os
import cv2
import numpy as np
import csv


def getNPCRrgb(ori_img, enc_img):
    ori_img = ori_img.reshape(-1, 3)
    enc_img = enc_img.reshape(-1, 3)
    return getNPCR(ori_img[:, 2], enc_img[:, 2]), \
        getNPCR(ori_img[:, 1], enc_img[:, 1]), \
        getNPCR(ori_img[:, 0], enc_img[:, 0])


def getNPCR(ori_arr, enc_arr):
    npcr = 0
    for i in range(len(ori_arr)):
        if ori_arr[i] != enc_arr[i]:
            npcr += 1
    NPCR = np.round((npcr/len(ori_arr))*100, 4)
    return NPCR


def getUACIrgb(ori_img, enc_img):
    ori_img = ori_img.reshape(-1, 3)
    enc_img = enc_img.reshape(-1, 3)
    return getUACI(ori_img[:, 2], enc_img[:, 2]), \
        getUACI(ori_img[:, 1], enc_img[:, 1]), \
        getUACI(ori_img[:, 0], enc_img[:, 0])


def getUACI(ori_arr, enc_arr):
    uaci = 0
    for i in range(len(ori_arr)):
        uaci += abs(int(ori_arr[i]) - int(enc_arr[i]))
    UACI = np.round((uaci/(len(ori_arr)*255))*100, 4)
    return UACI


def getOutput(i, ori_name, enc_name, ori_img, enc_img):
    NPCRr, NPCRg, NPCRb = getNPCRrgb(ori_img, enc_img)
    UACIr, UACIg, UACIb = getUACIrgb(ori_img, enc_img)
    return [i, ori_name, enc_name, NPCRr, NPCRg, NPCRb, UACIr, UACIg, UACIb]


def toCsvOutput(ori_dir, enc_dir, csv_name):
    csv_text = [['No', 'ORI Images', 'ENC Image', 'NPCR(R)', 'NPCR(G)',
                 'NPCR(B)', 'UACI(R)', 'UACI(G)', 'UACI(B)']]
    i = 1
    for ori_name, enc_name in zip(os.listdir(ori_dir), os.listdir(enc_dir)):
        ori_img = cv2.imread(ori_dir+ori_name, cv2.IMREAD_COLOR)
        enc_img = cv2.imread(enc_dir+enc_name, cv2.IMREAD_COLOR)
        print(ori_name)
        print(enc_name)
        csv_text.append(getOutput(i, ori_name, enc_name, ori_img, enc_img))
        i += 1

        # break

    with open(csv_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_text)


toCsvOutput("12-Images/Origi_image/", "12-Images/Encry_image/", "output12.csv")
