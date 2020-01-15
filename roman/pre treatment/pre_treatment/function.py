import numpy as np
import scipy.signal as signal
import math
import pywt
import pandas as pd
import matplotlib.pyplot as plt

def get_average(records):
    return sum(records) / len(records)

def get_rms(records):
    return math.sqrt(sum([x ** 2 for x in records]) / len(records))

def wavelet_transform(Relative_intensity,a):
    w = pywt.Wavelet('db8')  # 选用Daubechies8小波

    maxlev = pywt.dwt_max_level(len(Relative_intensity), w.dec_len)
    #print("maximum level is " + str(maxlev))

    threshold = a  # Threshold for filtering

    coeffs = pywt.wavedec(Relative_intensity, 'db8', level=maxlev)  # 将信号进行小波分解
                                                        # data为要处理的数据，列表存储
    for i in range(1, len(coeffs)):
        #print(i)
        coeffs[i] = pywt.threshold(coeffs[i], threshold*max(coeffs[i]))  # 将噪声滤波
    datarec = pywt.waverec(coeffs, 'db8')  # 将信号进行小波重构
    mintime = 1
    maxtime = mintime + len(Relative_intensity) + 1
    datas=np.arange(0,Relative_intensity.shape[0],1)
    for i in range(0,Relative_intensity.shape[0]):
        datas[i] = datarec[i]
    #print(datarec)
    #print(wave_number.shape)
    return datas

def fft(Relative_intensity):
    b, a = signal.butter(8,0.4, 'lowpass',analog=False)
    filtedData = signal.filtfilt(b, a, Relative_intensity)#data为要过滤的信号
    filtedData = signal.filtfilt(b, a, filtedData)#data为要过滤的信号
    filtedData = signal.filtfilt(b, a, filtedData)#data为要过滤的信号
    filtedData = signal.filtfilt(b, a, filtedData)#data为要过滤的信号
    return filtedData

def med(Relative_intensity,n,a):  #中值滤波，data表示信号，n表示滤波器阶数，a表示邻域大小
    med_data=np.arange(0,Relative_intensity.shape[0],1)
    for idx in range(0, len(Relative_intensity)-1):
        med_data[idx] = Relative_intensity[idx]
    med_data[Relative_intensity.shape[0]-1] = Relative_intensity[Relative_intensity.shape[0]-2]
    med_data = signal.medfilt(Relative_intensity,3) #一维中值滤波
    for i in range(1, n):
        med_data = signal.medfilt(med_data,a) #一维中值滤波
    return med_data

def pull_baseline(Relative_intensity):
    wt_1 = wavelet_transform(Relative_intensity,5)
    data_1= Relative_intensity-wt_1
    wt_2 = wavelet_transform(data_1,0.4)
    data_2 = data_1-wt_2
    data_2 = Relative_intensity-abs(data_2)
    #print(get_rms(Relative_intensity/max(Relative_intensity)))
    for x in range(0,10000):
        wt_1 = wavelet_transform(data_2,5)
        #plt.plot(wave_number,wt_1)
        data_1 = Relative_intensity-wt_1
        #plt.plot(wave_number,data_1)
        data_2= Relative_intensity-abs(data_1)
        #print(get_rms(data_1/max(Relative_intensity)))
        if get_rms(data_1/max(Relative_intensity)) > 0.04:
            print(x)
            break

    data_wt = fft(data_1)
    data_wt = med(data_wt,1000,7)
    for i in range(0,5):
        data_wt = wavelet_transform(data_wt,0.005)
    return  (data_wt-min(data_wt))


