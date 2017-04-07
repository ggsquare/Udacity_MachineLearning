import pandas as pd

def get_mean_volume():
    df = pd.read_csv("tsla.csv")
    return ['Volume'].mean()

def testrun():
    print(get_mean_volume())

if __name__ == "__main__":
    testrun()