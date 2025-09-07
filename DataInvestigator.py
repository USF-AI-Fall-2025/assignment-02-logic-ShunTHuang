import pandas as pd


class DataInvestigator:
    def __init__(self, df):
        self.df = df
        if not isinstance(df, pd.DataFrame):
            self.df = None

    def baseline(self, col):
        if self.df is None or not len(self.df.columns) > col >= 0: return None

        try:
            return self.df.iloc[:, col].mode().tolist()[0]
        except:
            return None

    def corr(self, col1, col2):
        if self.df is None: return None

        if (not len(self.df.columns) > col1 >= 0 or
            not len(self.df.columns) > col2 >= 0):
            return None

        try:
            return self.df.iloc[:, col1].corr(self.df.iloc[:, col2])
        except:
            return None


    def zeroR(self, col):
        return self.baseline(col)




df = pd.read_csv('gallstone.csv')
di = DataInvestigator(df)
print(di.baseline(1))
print(di.zeroR(1))
print(di.corr(2, 3))