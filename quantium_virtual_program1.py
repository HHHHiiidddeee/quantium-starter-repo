import pandas as pd

def read_file(inputFile):
    df = pd.read_csv(inputFile)
    df = df.iloc[df[df["product"] == "pink morsel"].index]
    df["sales"] = df["price"].apply(lambda x: float(x.replace("$", "")))
    df["sales"] = df["sales"] * df["quantity"]
    df["sales"] = df["sales"].apply(lambda x: "$" + str(x))
    return df

def write_file(outputFile):
    df0 = read_file("./data/daily_sales_data_0.csv")
    df1 = read_file("./data/daily_sales_data_1.csv")
    df2 = read_file("./data/daily_sales_data_2.csv")

    df_total = pd.concat([df0,df1,df2])
    df_total = df_total.loc[:,["sales", "date", "region"]]
    df_total.to_csv(outputFile)


def main():
    write_file("output.csv")

if __name__ == "__main__":
    main()