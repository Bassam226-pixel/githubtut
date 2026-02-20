import pandas as pd



# Replace with your file path
df = pd.read_csv("annual-enterprise-survey-2024-financial-year-provisional.csv")



df.columns = df.columns.str.strip().str.lower()



df["value"] = pd.to_numeric(df["value"], errors="coerce")



df_2024 = df[df["year"] == 2024]



print("Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nMissing values:\n", df.isnull().sum())



financial_df = df_2024[df_2024["variable_category"] == "Financial performance"]



pivot = financial_df.pivot_table(
    index="industry_name_nzsioc",
    columns="variable_name",
    values="value",
    aggfunc="sum"
)

print("\nPivot Table:\n")
print(pivot)



if "Total income" in pivot.columns and "Total expenditure" in pivot.columns:
    pivot["Profit"] = pivot["Total income"] - pivot["Total expenditure"]

print("\nWith Profit:\n")
print(pivot)



expenses = financial_df.sort_values(by="value", ascending=False)
print("\nTop Financial Values:\n")
print(expenses[["variable_name", "value"]].head())



df.to_csv("my_project/financial_summary_2024.csv", index=False)

print("\n✅ Analysis Complete")