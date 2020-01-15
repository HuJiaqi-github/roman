import matplotlib.pyplot as plt
import pandas as pd
import pre_treatment
import time


start = time.time()
data = pd.read_csv('C:\\Users\\86178\\Desktop\\test\data\\duojunling.csv',encoding = 'gbk')

wave_number = data["wave number"]
Relative_intensity = data["-5_1"]

plt.figure()
plt.xlabel("wave number(cm${^-}$${^1}$)")
plt.ylabel("Relative intensity")
plt.title("Raman spectra",fontdict={'weight':'normal','size': 20})
plt.plot(wave_number,Relative_intensity,color = 'blue',label = 'Preliminary data')

Relative_intensity = pre_treatment.pull_baseline(Relative_intensity)
plt.plot(wave_number,Relative_intensity,color = 'red',label = 'Data after processing')

plt.legend(loc = 'best')
end = time.time()
print("运行时间："+str(end-start)+"秒")
plt.show()
plt.show()