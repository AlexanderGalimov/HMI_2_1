import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy

data = np.loadtxt("b1Саня.asc", skiprows=4)
eeg_data = data[:, 1]

f, t, Sxx = scipy.signal.spectrogram(eeg_data, 5000, nperseg=512 * 8, noverlap=2048+1024)
ind = (f > 13) & (f < 30)
beta = Sxx[ind]
power = pd.Series(np.sum(beta ** 2, axis=0))**0.5
threshold = power.rolling(100, min_periods=1).apply(lambda ser: ser.mean() + 2 * ser.std()).rolling(100,  min_periods=1).mean()
#threshold = power.mean() + 2 * power.std()
beta_activations = power >= threshold

#peaks, _ = scipy.signal.find_peaks(beta_activations.astype(float), distance=30)
b_a = power[~beta_activations]
fig, axes = plt.subplots(4)
axes[0].plot(power, 'r')
axes[0].plot(power + power.subtract(power[~beta_activations]), 'b')
#axes[0].plot(peaks, power.iloc[peaks], linestyle='none', marker='D')
axes[1].plot(threshold)
axes[2].plot(beta_activations)
axes[3].plot(eeg_data)
plt.show()







