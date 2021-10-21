import os
import cv2
import numpy as np
import csv


def getMean(X):
    return np.round(np.mean(X), 2)


def getVar(X):
    return np.round(np.var(X), 2)


def getCovXY(X, Y):
    return np.round(np.cov(X, Y,)[0, 1], 2)
    # return np.round(np.cov(X, Y, bias=True)[0, 1], 2) 原本的


def getCorrelationXY(var_x, var_y, cov_x_y):
    correlation_x_y = cov_x_y/((var_x*var_y)**(1/2))
    return np.round(correlation_x_y, 6)
    # return np.round(np.corrcoef(X,Y)), 6) 原本的


def caculate(X, Y):
    x = getMean(X)
    y = getMean(Y)
    var_x = getVar(X)
    var_y = getVar(Y)
    cov_x_y = getCovXY(X, Y)
    correlation_x_y = getCorrelationXY(var_x, var_y, cov_x_y)
    # print(x, y, var_x, var_y, cov_x_y, correlation_x_y)
    return x, y, var_x, var_y, cov_x_y, correlation_x_y


def getHD(name, channel, arr):
    # test
    # print(arr.shape)
    # print(arr[0, 1])
    # print(arr[2, 1])
    X = arr[:, :arr.shape[1]-1].reshape(-1)
    # print(X)
    Y = arr[:, 1:].reshape(-1)
    # print(Y)

    x, y, var_x, var_y, cov_x_y, correlation_x_y = caculate(X, Y)
    return [name, 'HD', channel, x, y, var_x, var_y, cov_x_y, correlation_x_y]


def getVD(name, channel, arr):
    Y = arr[:arr.shape[0]-1, :].reshape(-1)
    # print(X)
    X = arr[1:, :].reshape(-1)
    # print(Y)
    x, y, var_x, var_y, cov_x_y, correlation_x_y = caculate(X, Y)
    return [name, 'VD', channel, x, y, var_x, var_y, cov_x_y, correlation_x_y]


def getDD(name, channel, arr):
    Y = arr[:arr.shape[0]-1, :arr.shape[1]-1].reshape(-1)
    # print(X)
    X = arr[1:, 1:].reshape(-1)
    # print(Y)
    x, y, var_x, var_y, cov_x_y, correlation_x_y = caculate(X, Y)
    return [name, 'DD', channel, x, y, var_x, var_y, cov_x_y, correlation_x_y]


def getOutput(name, img):
    csv_output = []
    # print(img.shape)

    # test
    # img = np.array([[88, 27, 196], [21, 61, 12], [183, 113, 125]])
    # csv_output.append(getHD(name, 'R', img))
    # csv_output.append(getVD(name, 'R', img))
    # csv_output.append(getDD(name, 'R', img))

    csv_output.append(getHD(name, 'R', img[:, :, 2]))
    csv_output.append(getHD(name, 'G', img[:, :, 1]))
    csv_output.append(getHD(name, 'B', img[:, :, 0]))

    csv_output.append(getVD(name, 'R', img[:, :, 2]))
    csv_output.append(getVD(name, 'G', img[:, :, 1]))
    csv_output.append(getVD(name, 'B', img[:, :, 0]))

    csv_output.append(getDD(name, 'R', img[:, :, 2]))
    csv_output.append(getDD(name, 'G', img[:, :, 1]))
    csv_output.append(getDD(name, 'B', img[:, :, 0]))
    # for i in csv_output:
    #     print(i)
    return csv_output


def toCsvOutput(ori_dir, enc_dir, csv_name):
    csv_text = [['Image Name', 'Mode', 'Channel', 'x_bar', 'y_bar',
                 'VAR(X)', 'VAR(Y)', 'COV(X, Y)', 'Correlation(X,Y)']]
    for ori_name, enc_name in zip(os.listdir(ori_dir), os.listdir(enc_dir)):
        ori_img = cv2.imread(ori_dir+ori_name, cv2.IMREAD_COLOR)
        enc_img = cv2.imread(enc_dir+enc_name, cv2.IMREAD_COLOR)
        for i in getOutput(ori_name, ori_img):
            csv_text.append(i)

        for i in getOutput(enc_name, enc_img):
            csv_text.append(i)
        # break

    with open(csv_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_text)


toCsvOutput("13-Images/Origi_image/",
            "13-Images/Encry_image/", "output13_v2.csv")
