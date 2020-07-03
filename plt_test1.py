
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def moving_avg(a,n=3):
    ret = np.cumsum(a)
##    print(ret)
##    print( len(ret[n:]),len(ret[:-n]),type(ret))
##    ret_A=ret
    ret[n:] = ret[n:] - ret[:-n]
##    print('now OK')
##    print(ret)
    return ret[n - 1:]/n




wfm=pd.read_csv('FFT_fromOSC.csv',header=None)
XX=wfm[0].to_numpy()
YY=wfm[1].to_numpy()

plt.subplot(211)
plt.plot(wfm[0],wfm[1])
plt.grid(axis='both',color='cyan',linestyle='-',linewidth=2) #This is grid-on option
plt.annotate("RTS noise",(-0.02,0.018)) #remark at drawing (waveform)
plt.xlabel('time(s)')
plt.ylabel('Voltage')

##plt.subplot(212)
##x=np.arange(-50.0,50.0,0.01)
##y=np.arange(0,100.0,0.01)
##plt.plot(x,y)
##plt.xscale('symlog')
##plt.grid(1)
##plt.gca().xaxis.grid(True, which='minor')

plt.subplot(212) #moving average calculation
YY_ma10=moving_avg(YY,n=50)
##print(len(YY_ma10))
plt.plot(YY_ma10)
plt.grid(1)
plt.annotate("RTS noise, MA50",(0,0))

plt.show()
