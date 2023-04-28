import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

# data = np.loadtxt("b1Саня.asc", skiprows=4)
# eeg_data = data[:, 1]
#
# # Определение частоты дискретизации
# fs = 5000
#
# # Рассчитываем спектр мощности
# freqs, psd = welch(eeg_data, fs=fs)
#
# # Находим частотный диапазон бета-ритма
# beta_idx = np.logical_and(freqs >= 13, freqs <= 30)
#
# # Вычисляем среднее значение спектра мощности в частотном диапазоне бета-ритма
# beta_power = np.mean(psd[beta_idx])
#
# # Определяем пороговое значение для детекции активации бета-ритма
# threshold = beta_power * 1.5 # Пример значения порога
#
# # Вычисляем изменение амплитуды
# delta_amp = np.abs(np.diff(eeg_data))
#
# # Детекция активации бета-ритма
# beta_activation = np.where(delta_amp > threshold)[0]
#
# # Отображение данных и результатов
# plt.figure(figsize=(12, 6))
# plt.subplot(2, 1, 1)
# plt.plot(eeg_data)
# plt.title("EEG data")
# plt.xlabel("Sample")
# plt.ylabel("Amplitude")
# # plt.subplot(2, 1, 2)
# plt.plot(delta_amp)
# plt.plot([0, len(delta_amp)], [threshold, threshold], "--r")
# plt.plot(beta_activation, delta_amp[beta_activation], "ro")
# plt.title("Beta activation detection")
# plt.xlabel("Sample")
# plt.ylabel("Delta amplitude")
# plt.show()

x = np.linspace(0, 20*np.pi, 5000)
y = []
for num in x:
    y.append(np.sin(num))

x = np.linspace(20*np.pi, 40*np.pi, 5000)
for num in x:
    y.append(2*np.sin(num))

x = np.linspace(40*np.pi, 60*np.pi, 5000)
for num in x:
    y.append(np.sin(num))

x = np.linspace(60*np.pi, 80*np.pi, 5000)
for num in x:
    y.append(2*np.sin(num))

x = np.linspace(80*np.pi, 100*np.pi, 5000)
for num in x:
    y.append(np.sin(num))

with open("синусоида.asc", 'w') as f:
    for num in y:
        f.write(str(num) + "\n")

