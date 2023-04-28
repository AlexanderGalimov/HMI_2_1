import tkinter as tk
from tkinter import filedialog, messagebox

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy


class Window:
    root = tk.Tk()

    def __init__(self):
        self.root.title("Phase Portrait Drawing")
        self.root.geometry('1000x700')
        self.path = None
        button1 = tk.Button(self.root, text="Select ASC File", command=self.select_file)
        button2 = tk.Button(self.root, text="Detection beta activations", command=self.draw_function)
        button1.pack()
        button2.pack()

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("ASC file", "*.asc")])
        self.path = file_path

    def start(self):
        self.root.mainloop()

    def roll_mean(self, ser, prev=0):
        res = ser.mean() + 2 * ser.std()
        prev = ser.mean() + 2 * ser.std() - prev
        return res, prev

    def draw_function(self):
        if self.path is not None and self.path != '':

            data = np.loadtxt(self.path, skiprows=4)
            eeg_data = data[:, 1]

            f, t, Sxx = scipy.signal.spectrogram(eeg_data, 5000, nperseg=1000, noverlap=0)
            ind = (f > 14) & (f < 30)
            beta = Sxx[ind]
            power = pd.Series(np.sum(beta ** 2, axis=0)) ** 0.5
            #threshold = power.rolling(50, min_periods=1).apply(lambda ser, prev: self.roll_mean(ser, )).rolling(50,min_periods=1).mean()

            threshold = power.mean() + power.std()

            beta_activations = power >= threshold

            # peaks, _ = scipy.signal.find_peaks(beta_activations.astype(float), distance=30)
            fig, axes = plt.subplots(2)
            axes[0].plot(power, 'r')
            axes[0].plot(power + power.subtract(power[~beta_activations]), 'b')
            # axes[0].plot(peaks, power.iloc[peaks], linestyle='none', marker='D')
            axes[1].plot(eeg_data)

            plt.show()

        else:
            messagebox.showinfo("Error", "Choose file correctly")


window = Window()
window.start()
