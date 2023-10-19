from sklearn.decomposition import FastICA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from notch import notch
from bandpass import bandpass

def ICA_opp(X):
    ica = FastICA(n_components = 18)
    out_ICA = pd.DataFrame(ica.fit_transform(X))
    
    return out_ICA, ica

def remove_epilepsy(df):
    df_y = df['Epilepsy'].copy()
    df_x = df.drop('Epilepsy', axis=1).copy()   

    return df_x, df_y


def remerge_epilepsy(X, Y):
    merged_df = X.join(Y)
    return merged_df

def remove_comp(df, comp):
    df[comp] = 0
    return df

def reconstruct(df, ica):
    column_names = ["Fp1", "Fp2", "F7", "F3", "Fz", "F4", "F8", "T3","C3", "C4", "T4", "T5","P3", "Pz", "P4", "T6", "O1", "O2"]
    return pd.DataFrame(np.dot(df, ica.mixing_.T), columns=column_names)


def ICA(df):
    df_copy = df.copy()
    df_x, df_y = remove_epilepsy(df_copy)
    out_ica, ica = ICA_opp(df_x)
    out_ica = remove_comp(out_ica, 0)
    df_x = reconstruct(out_ica, ica)
    df_copy = remerge_epilepsy(df_x, df_y)    
    return df_copy

# if __name__ == "__main__":
#     patient = pd.read_csv("original_data/patient1.csv")

    
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
#             patient[patient.columns[value]] = notch(patient[patient.columns[value]])
#             patient[patient.columns[value]] = bandpass(patient[patient.columns[value]])

#     patient = ICA(patient)
#     print(patient)
    # print(patient.columns[0])



    
    # patient = ICA(patient)
    # print(patient)


