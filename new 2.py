df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]


Transposing your data:
df.T

Sorting by an axis:
df.sort_index(axis=1, ascending=False)


Sorting by values:
df.sort_values(by="B")

/!\
Selecting via [], which slices the rows.


For getting a cross section using a label:
df.loc[dates[0]]
Selecting on a multi-axis by label:
df.loc[:, ["A", "B"]]
Showing label slicing, both endpoints are included:
df.loc["20130102":"20130104", ["A", "B"]]

For getting a scalar value:
df.loc[dates[0], "A"]
For getting fast access to a scalar (equivalent to the prior method):
df.at[dates[0], "A"]


Selection by position
df.iloc[3]
df.iloc[3:5, 0:2]
df.iloc[[1, 2, 4], [0, 2]]
df.iloc[1:3, :]
df.iloc[:, 1:3]
df.iloc[1, 1]
df.iat[1, 1]



Boolean indexing
df2[df2["E"].isin(["two", "four"])]


Setting
https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#setting

df2[df2 > 0] = -df2


Reindexing allows you to change/add/delete the index on a specified axis. 
This returns a copy of the data.
In [55]: df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
In [56]: df1.loc[dates[0] : dates[1], "E"] = 1


To drop any rows that have missing data.
In [58]: df1.dropna(how="any")
Filling missing data.
In [59]: df1.fillna(value=5)

df.to_excel("foo.xlsx", sheet_name="Sheet1")

