import pandas as pd
import numpy as np
from notch import notch
from bandpass import bandpass
from ICA import ICA


def pre_process(df):
    patient = df.copy()

    n_samples = 45500
    channels_dict = {"Fp1" : 0, 
                    "Fp2" : 1,
                    "F7" : 2,
                    "F3" : 3,
                    "Fz" : 4,
                    "F4": 5,
                    "F8": 6,
                    "T3": 7,
                    "C3": 8,
                    "C4": 9,
                    "T4": 10,
                    "T5": 11,
                    "P3": 12,
                    "Pz": 13,
                    "P4": 14,
                    "T6": 15,
                    "O1": 16,
                    "O2": 17,
                    "Epilepsy": 18}
    
    for key, value in channels_dict.items():
        if value < 18:
            patient[patient.columns[value]] = notch(patient[patient.columns[value]])
            patient[patient.columns[value]] = bandpass(patient[patient.columns[value]])

    patient = ICA(patient)
    return patient
    


if __name__ == "__main__":
    df1 = pd.read_csv("original_data/patient1.csv")
    df2 = pd.read_csv("original_data/patient2.csv")
    df3 = pd.read_csv("original_data/patient3.csv")
    df4 = pd.read_csv("original_data/patient4.csv")
    df5 = pd.read_csv("original_data/patient5.csv")



    patient1 = pre_process(df1)
    patient2 = pre_process(df2)
    patient3 = pre_process(df3)
    patient4 = pre_process(df4)
    patient5 = pre_process(df5)



    patient1.to_csv("data_preprocessed/patient1_processed.csv", index = False)
    patient2.to_csv("data_preprocessed/patient2_processed.csv", index = False)
    patient3.to_csv("data_preprocessed/patient3_processed.csv", index = False)
    patient4.to_csv("data_preprocessed/patient4_processed.csv", index = False)
    patient5.to_csv("data_preprocessed/patient5_processed.csv", index = False)
    

