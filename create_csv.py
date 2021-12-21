import sklearn
import pandas as pd
class preprocessing:
    def __init__(self, prob_type, train_path, test_path):
        '''
        prob_type(str) : 'regression', binary', 'multiclass'
        train_path(str): path of the train csv file, for example : "C:\Users\Desktop\df_train.csv"
        test_path(str):  path of the test csv file, for example : "C:\Users\Desktop\df_test.csv"

        '''
        self.prob_type = prob_type
        self.train_path = train_path 
        self.test_path = test_path
        self.df = pd.read_csv(self.train_path)
        self.cat_feats = self.df.select_dtypes(include=['object','str']).columns.tolist() 

    # Manage the missing values in df

    # The functions for managing categorical features taken
    # from https://github.com/abhishekkrthakur/mlframework/blob/master/src/categorical.py

    