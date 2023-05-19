import pandas as pd


def perprocess(df, region_df):
    #filtering for summer olymppics
    df = df[df['Season'] == "Summer"]
    #merge with region_df
    df = df.merge(region_df, on = "NOC", how = "left")
    #droping duplicates
    df.drop_duplicates(inplace=True)
    #one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df["Medal"])], axis=1)
    return df

