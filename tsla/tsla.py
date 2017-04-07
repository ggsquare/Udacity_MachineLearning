import pandas as pd
import matplotlib.pyplot as plt

#Getting all data for rows 10-20
'''
def testrun():
    df = pd.read_csv("tsla.csv")
    print(df[10:21])
'''

#Getting mean volume
'''
def get_mean_volume():
    df = pd.read_csv("tsla.csv")
    return df['Volume'].mean()

def testrun():
    print("Mean Volume:", get_mean_volume())
'''

#plotting prices
'''
def testrun():
    df = pd.read_csv("tsla.csv")
    print(df['Adj Close'])
    df['Adj Close'].plot()
    plt.show()
'''

def testrun():
    df = pd.read_csv("tsla.csv")
    df[['Low', 'Adj Close']].plot()
    plt.show()

if __name__ == "__main__":
    testrun()