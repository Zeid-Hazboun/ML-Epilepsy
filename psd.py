import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch

df=pd.read_csv("patient1.csv")
# df2 = pd.read_csv("Cz_ref_data/sueno.csv")
# notch = pd.read_csv("filters_v_fp1.csv")
# sueno = pd.read_csv("sueno_split/sueno_0.csv")


# n_samples = 54500
sampling_rate = 250

for i in range(1):

    patient1 = df[df.columns[i]]
    # sueno_fp1 = df2[df2.columns[0]]

    # f, psd = welch(violeta_fp1, fs=sampling_rate, nperseg=256)
    f, psd = welch(patient1, fs=sampling_rate, nperseg=256)
    # f, psd = welch(sueno_fp1, fs=sampling_rate, nperseg=256)
    # print("f:" ,f)
    print(" f size: ", f.size)
    print("psd size: ", psd.size)
    print("violeta size: ", patient1.size)
    # print("notch size: ", notch.size)

    # Plot the PSD
    plt.figure(figsize=(8, 4))
    plt.plot(f, psd)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectral Density')
    plt.title('Power Spectral Density')
    plt.grid(True)
    plt.show()