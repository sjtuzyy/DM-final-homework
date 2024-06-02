import os
import numpy as np
import pandas as pd
from utils.timefeatures import time_features
from torch.utils.data import Dataset, DataLoader
class Annotation():
    def __init__(self,root_path,file_name):
        self.root_path = root_path
        self.file_name = file_name
    def read_data(self):
        df = pd.read_csv(os.path.join(self.root_path,
                                          self.file_name))
        df_stamp = df[['date']]
        df_stamp['date'] = pd.to_datetime(df_stamp.date)
        if self.timeenc == 0:
            df_stamp['month'] = df_stamp.date.apply(lambda row: row.month, 1)
            df_stamp['day'] = df_stamp.date.apply(lambda row: row.day, 1)
            df_stamp['weekday'] = df_stamp.date.apply(lambda row: row.weekday(), 1)
            df_stamp['hour'] = df_stamp.date.apply(lambda row: row.hour, 1)
            data_stamp = df_stamp.drop(['date'], 1).values
        elif self.timeenc == 1:
            data_stamp = time_features(pd.to_datetime(df_stamp['date'].values), freq=self.freq)
            data_stamp = data_stamp.transpose(1, 0)
        self.data_stamp = data_stamp
        self.data = df.columns[1:]
