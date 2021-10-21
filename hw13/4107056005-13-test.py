import os
import cv2
import numpy as np
import csv


def getMean(X):
    return np.round(np.mean(X), 2)


def getVar(X):
    return np.round(np.var(X), 2)


def getCovXY(X, Y):
    return np.round(np.cov(X, Y)[0, 1], 2)


def getCovXY_2(X, Y, x_bar, y_bar):
    cov_xy = 0
    for i in range(len(X)):
        cov_xy += X[i]*Y[i]
    cov_xy -= len(X)*x_bar*y_bar
    cov_xy /= (len(X)-1)

    return np.round(cov_xy, 2)


def getCorrelationXY(X, Y):
    return np.round(np.corrcoef(X, Y)[0, 1], 6)


def caculate(X, Y):
    x = getMean(X)
    y = getMean(Y)
    var_x = getVar(X)
    var_y = getVar(Y)
    cov_x_y = getCovXY(X, Y)
    # cov_x_y = getCovXY_2(X, Y, x, y)
    correlation_x_y = getCorrelationXY(X, Y)
    return x, y, var_x, var_y, cov_x_y, correlation_x_y


def getHD(name, channel, arr):
    X = arr[:, :arr.shape[1]-1].reshape(-1)
    Y = arr[:, 1:].reshape(-1)
    print("HD")
    print('X:', end='')
    print(X)
    print('Y:', end='')
    print(Y)

    x, y, var_x, var_y, cov_x_y, correlation_x_y = caculate(X, Y)
    return [name, 'HD', channel, x, y, var_x, var_y, cov_x_y, correlation_x_y]


def getVD(name, channel, arr):
    X = arr[:arr.shape[0]-1, :].reshape(-1)
    Y = arr[1:, :].reshape(-1)
    print("VD")
    print('X:', end='')
    print(X)
    print('Y:', end='')
    print(Y)
    x, y, var_x, var_y, cov_x_y, correlation_x_y = caculate(X, Y)
    return [name, 'VD', channel, x, y, var_x, var_y, cov_x_y, correlation_x_y]


def getDD(name, channel, arr):
    X = arr[:arr.shape[0]-1, :arr.shape[1]-1].reshape(-1)
    Y = arr[1:, 1:].reshape(-1)
    print("DD")
    print('X:', end='')
    print(X)
    print('Y:', end='')
    print(Y)

    x, y, var_x, var_y, cov_x_y, correlation_x_y = caculate(X, Y)
    return [name, 'DD', channel, x, y, var_x, var_y, cov_x_y, correlation_x_y]


def getOutput(name="test"):
    csv_output = []
    img = np.array([[88, 27, 196], [21, 61, 12], [183, 113, 125]])
    print("img")
    print(img)
    csv_output.append(getHD(name, 'R', img))
    csv_output.append(getVD(name, 'R', img))
    csv_output.append(getDD(name, 'R', img))

    return csv_output


def toCsvOutput(csv_name):
    csv_text = [['Image Name', 'Mode', 'Channel', 'x_bar', 'y_bar',
                 'VAR(X)', 'VAR(Y)', 'COV(X, Y)', 'Correlation(X,Y)']]
    for i in getOutput():
        csv_text.append(i)

    with open(csv_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_text)


toCsvOutput("test13.csv")
