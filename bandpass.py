import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import pandas as pd

def bandpass(df):
    low_freq = 1
    high_freq = 40
    fs = 250
    order = 6
    nyquist = 0.5 * fs
    low = low_freq/nyquist
    high = high_freq/nyquist

    b,a = signal.butter(order, [low,high], btype= 'band')

    filtered_signal = signal.lfilter(b,a, df)

    return filtered_signal



# if __name__ == "__main__":
        
#     df1 = pd.read_csv("notch_data/patient1.csv")
#     df2 = pd.read_csv("notch_data/patient2.csv")
#     df3 = pd.read_csv("notch_data/patient3.csv")
#     df4 = pd.read_csv("notch_data/patient4.csv")
#     df5 = pd.read_csv("notch_data/patient5.csv")

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
#     for key, value in channels_dict.items():
#         if value < 18:
#             patient1[patient1.columns[value]] = bandpass(df1[df1.columns[value]])
#             patient2[patient2.columns[value]] = bandpass(df2[df2.columns[value]])
#             patient3[patient3.columns[value]] = bandpass(df3[df3.columns[value]])
#             patient4[patient4.columns[value]] = bandpass(df4[df4.columns[value]])
#             patient5[patient5.columns[value]] = bandpass(df5[df5.columns[value]])


#     patient1.to_csv("/Users/zeidsmac/Desktop/Frontiers_project/bandpass_data/patient1_bandpass.csv", index = False)
#     patient2.to_csv("/Users/zeidsmac/Desktop/Frontiers_project/bandpass_data/patient2_bandpass.csv", index = False)
#     patient3.to_csv("/Users/zeidsmac/Desktop/Frontiers_project/bandpass_data/patient3_bandpass.csv", index = False)
#     patient4.to_csv("/Users/zeidsmac/Desktop/Frontiers_project/bandpass_data/patient4_bandpass.csv", index = False)
#     patient5.to_csv("/Users/zeidsmac/Desktop/Frontiers_project/bandpass_data/patient5_bandpass.csv", index = False)


