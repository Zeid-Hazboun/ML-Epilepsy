from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def notch(df): 
    samp_freq = 250  # Sample frequency (Hz)
    notch_freq = 60.0  # Frequency to be removed from signal (Hz)
    quality_factor = 1.0  # Quality factor

    # Design a notch filter using signal.iirnotch
    b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, samp_freq)

    # Compute magnitude response of the designed filter
    freq, h = signal.freqz(b_notch, a_notch, fs=2*np.pi)

    outputSignal = signal.filtfilt(b_notch, a_notch, df)

    return outputSignal

# if __name__ == "__main__":

#     df1 = pd.read_csv("patient1.csv")
#     df2 = pd.read_csv("patient2.csv")
#     df3 = pd.read_csv("patient3.csv")
#     df4 = pd.read_csv("patient4.csv")
#     df5 = pd.read_csv("patient5.csv")

#     patient1 = df1.copy()
#     patient2 = df2.copy()
#     patient3 = df3.copy()
#     patient4 = df4.copy()
#     patient5 = df5.copy()

#     n_samples = 45500
#     channels_dict = {"Fp1" : 0, 
#                     "Fp2" : 1,
#                     "F7" : 2,
#                     "F3" : 3,
#                     "Fz" : 4,
#                     "F4": 5,
#                     "F8": 6,
#                     "T3": 7,
#                     "C3": 8,
#                     "C4": 9,
#                     "T4": 10,
#                     "T5": 11,
#                     "P3": 12,
#                     "Pz": 13,
#                     "P4": 14,
#                     "T6": 15,
#                     "O1": 16,
#                     "O2": 17,
#                     "Epilepsy": 18}



#     # Apply notch filter to the noisy signal using signal.filtfilt
#     # violeta_fp1 = df[df.columns[0]]
#     for key, value in channels_dict.items():
#         if value < 18:
#             patient1[patient1.columns[value]] = notch(df1[df1.columns[value]])
#             patient2[patient2.columns[value]] = notch(df2[df2.columns[value]])
#             patient3[patient3.columns[value]] = notch(df3[df3.columns[value]])
#             patient4[patient4.columns[value]] = notch(df4[df4.columns[value]])
#             patient5[patient5.columns[value]] = notch(df5[df5.columns[value]])


#     patient1.to_csv("/Users/zeidsmac/Desktop/Frontiers_project/notch_data/patient1_notch.csv", index = False)
#     patient2.to_csv("/Users/zeidsmac/Desktop/Frontiers_project/notch_data/patient2_notch.csv", index = False)
#     patient3.to_csv("/Users/zeidsmac/Desktop/Frontiers_project/notch_data/patient3_notch.csv", index = False)
#     patient4.to_csv("/Users/zeidsmac/Desktop/Frontiers_project/notch_data/patient4_notch.csv", index = False)
#     patient5.to_csv("/Users/zeidsmac/Desktop/Frontiers_project/notch_data/patient5_notch.csv", index = False)

