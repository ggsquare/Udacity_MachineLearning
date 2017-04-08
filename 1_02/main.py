#Analyzing SNAP data
#Grant Gasser, 4/7/2017

import pandas as pd

def testRun():
    #Define date range
    startDate = '2017-03-01'
    endDate = '2017-04-06'
    dates = pd.date_range(startDate,endDate)

    # Create empty dataframe
    df1 = pd.DataFrame(index=dates)

    #Read SPY data into temp dataframe
    dfSPY = pd.read_csv("SPY.csv", index_col="Date",
                        parse_dates=True, usecols=['Date', 'Adj Close'])

    #Rename 'Adj Close' column to 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})

    #join empty dataframe (df1) and SPY dataframe w/ join
    df1 = df1.join(dfSPY, how='inner')

    #Drop NaN vals or could define how='inner' in join() ^
    #df1 = df1.dropna()

    #Read in more stock
    tickers = ['SNAP', 'TSLA', 'GS', 'XOM']
    for ticker in tickers:
        dfTemp = pd.read_csv("{}.csv".format(ticker), index_col='Date',
                             parse_dates=True, usecols=['Date', 'Adj Close'],
                             na_values=['nan'])
        dfTemp = dfTemp.rename(columns={'Adj Close': ticker})
        df1 = df1.join(dfTemp) #use default how='left'

    print(df1)

if __name__ == "__main__":
    testRun()