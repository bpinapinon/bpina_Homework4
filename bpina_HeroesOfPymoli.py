# Import Dependencies
import pandas as pd 
import numpy as np 

# Store file path in variable
FilePath = "Resources/purchase_data.csv"

# Use Pandas to read CSV and load into Data Frame
DataFrame_Orig = pd.read_csv(FilePath)
# print(DataFrame_Orig.head())
# print(DataFrame_Orig.columns)
# ['Purchase ID', 'SN', 'Age', 'Gender', 'Item ID', 'Item Name', 'Price']



### Player Count
# * Total Number of Players
CountPlayers = DataFrame_Orig["SN"].nunique()
print(f'\nTotal Number of Players = {CountPlayers}')



### Purchasing Analysis (Total)
# * Number of Unique Items
# * Average Purchase Price
# * Total Number of Purchases
# * Total Revenue

# Unique Items
DF_UniqueItems = DataFrame_Orig["Item ID"].unique()
CountUniqueItems = len(DF_UniqueItems)
print(f'\nNumber of Unique Items: {CountUniqueItems}')

# Average Purchase Price
AveragePurchasePrice = round(DataFrame_Orig["Price"].mean() , 2)
print(f'\nAverage Purchase Price = ${AveragePurchasePrice}')

# Total Number of Purchases
CountTotalPurchases = DataFrame_Orig["Price"].count()
print(f'\nTotal Number of Purchases = {CountTotalPurchases}')

# Total Revenue
TotalRevenue = DataFrame_Orig["Price"].sum()
print(f'\nTotal Revenue = ${TotalRevenue}')
 
# Summary Data Frame
Summary_PurchasingAnalysis = pd.DataFrame({"Count of Unique Items"      : CountUniqueItems
                                          ,"Average Purchase Price"     : [AveragePurchasePrice]
                                          ,"Total Number of Purchases"  : [CountTotalPurchases]
                                          ,"Total Revenue"              : [TotalRevenue]
                                          })
print(Summary_PurchasingAnalysis)     



### Gender Demographics
# * Percentage and Count of Male Players
# * Percentage and Count of Female Players
# * Percentage and Count of Other / Non-Disclosed     

GenderTotals = DataFrame_Orig["Gender"].value_counts()
print(GenderTotals)              

GenderPercentages = round((GenderTotals / CountPlayers) * 100 , 2)

# Summary Data Frame
Summary_GenderTotals = pd.DataFrame({"Gender Count"      : GenderTotals
                                    ,"Gender Percentage" : GenderPercentages
                                    })
print(Summary_GenderTotals)                                



### Gender Purchasing Analysis 
# * The below each broken by gender
#   * Purchase Count
#   * Average Purchase Price
#   * Total Purchase Value
#   * Normalized Totals

# Purchase Count
GenderPurchaseCount = DataFrame_Orig.groupby(["Gender"]).count()["Price"]
GenderPurchaseCount = GenderPurchaseCount.rename("Gender Purchase Count")
print(GenderPurchaseCount)

# Average Purchase Price
GenderAveragePurchase = round(DataFrame_Orig.groupby(["Gender"]).mean()["Price"] ,2)
GenderAveragePurchase = GenderAveragePurchase.rename("Gender Average Purchase Price")
print(GenderAveragePurchase)

# Total Purchase Value
GenderTotalPurchaseValue = DataFrame_Orig.groupby(["Gender"]).sum()["Price"]
GenderTotalPurchaseValue = GenderTotalPurchaseValue.rename("Gender Total Purchase Value")
print(GenderTotalPurchaseValue)

# Normalized Totals - Average Total Purchase per Person
GenderNormalizedTotals = round(GenderTotalPurchaseValue / Summary_GenderTotals["Gender Count"] ,2)
GenderNormalizedTotals = GenderNormalizedTotals.rename("Average Total Purchase Per Person")
print(GenderNormalizedTotals)

# Summary Data Frame
Summary_GenderPurchasingAnalysis = pd.DataFrame({"Gender Purchase Count"                         : GenderPurchaseCount
                                                ,"Gender Avg Purchase Price"                     : GenderAveragePurchase
                                                ,"Gender Total Purchase Value"                   : GenderTotalPurchaseValue
                                                ,"Gender Avg Total Purchase/Person (Normalized)" : GenderNormalizedTotals
                                                })
# Data Formatting
Summary_GenderPurchasingAnalysis["Gender Avg Purchase Price"] = Summary_GenderPurchasingAnalysis["Gender Avg Purchase Price"].map("${:,.2f}".format)
Summary_GenderPurchasingAnalysis["Gender Total Purchase Value"] = Summary_GenderPurchasingAnalysis["Gender Total Purchase Value"].map("${:,.2f}".format)
Summary_GenderPurchasingAnalysis["Gender Avg Total Purchase/Person (Normalized)"] = Summary_GenderPurchasingAnalysis["Gender Avg Total Purchase/Person (Normalized)"].map("${:,.2f}".format)
Summary_GenderPurchasingAnalysis["Gender Purchase Count"] = Summary_GenderPurchasingAnalysis["Gender Purchase Count"].map("{:,}".format)

print(Summary_GenderPurchasingAnalysis)




### Age Demographics
# * Percentage and Count     

# Bins
AgeBins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
AgeBinLabels = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# Categorize the players using the Age bins
DataFrame_Orig["Age Range"] = pd.cut(DataFrame_Orig["Age"], AgeBins, labels = AgeBinLabels)
print(DataFrame_Orig.head())


# Determine counts and percentages (similar to Gender Demographics)
AgeTotals = DataFrame_Orig["Age Range"].value_counts()
print(AgeTotals)

AgePercentages = round((AgeTotals / CountPlayers) * 100 , 2)

# Summary Data Frame
Summary_AgeTotals = pd.DataFrame({"Age Count"      : AgeTotals
                                 ,"Age Percentage" : AgePercentages
                                 })

Summary_AgeTotals = Summary_AgeTotals.sort_index()                                 
print(Summary_AgeTotals)



## Age Purchasing Analysis
# * The below each broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.)
#   * Purchase Count
#   * Average Purchase Price
#   * Total Purchase Value
#   * Normalized Totals


# Bin all original data frame records
DataFrame_Orig["Age Range"] = pd.cut(DataFrame_Orig["Age"], AgeBins, labels = AgeBinLabels)

# Purchase Count
AgePurchaseCount = DataFrame_Orig.groupby(["Age Range"]).count()["Price"]
AgePurchaseCount = AgePurchaseCount.rename("Age Purchase Count")
print(AgePurchaseCount)

# Average Purchase Price
AgeAveragePurchase = round(DataFrame_Orig.groupby(["Age Range"]).mean()["Price"] ,2)
AgeAveragePurchase = round(DataFrame_Orig.groupby(["Age Range"]).mean()["Price"] ,2)
AgeAveragePurchase = AgeAveragePurchase.rename("Age Average Purchase Price")
print(AgeAveragePurchase)

# Total Purchase Value
AgeTotalPurchaseValue = DataFrame_Orig.groupby(["Age Range"]).sum()["Price"]
AgeTotalPurchaseValue = AgeTotalPurchaseValue.rename("Age Total Purchase Value")
print(AgeTotalPurchaseValue)

# Normalized Totals - Average Total Purchase per Person
AgeNormalizedTotals = round(AgeTotalPurchaseValue / Summary_AgeTotals["Age Count"] ,2)
AgeNormalizedTotals = AgeNormalizedTotals.rename("Average Total Purchase Per Person")
print(AgeNormalizedTotals)

# Summary Data Frame
Summary_AgePurchasingAnalysis = pd.DataFrame({"Age Purchase Count"                         : AgePurchaseCount
                                             ,"Age Avg Purchase Price"                     : AgeAveragePurchase
                                             ,"Age Total Purchase Value"                   : AgeTotalPurchaseValue
                                             ,"Age Avg Total Purchase/Person (Normalized)" : AgeNormalizedTotals
                                             })
# Data Formatting
Summary_AgePurchasingAnalysis["Age Avg Purchase Price"] = Summary_AgePurchasingAnalysis["Age Avg Purchase Price"].map("${:,.2f}".format)
Summary_AgePurchasingAnalysis["Age Total Purchase Value"] = Summary_AgePurchasingAnalysis["Age Total Purchase Value"].map("${:,.2f}".format)
Summary_AgePurchasingAnalysis["Age Avg Total Purchase/Person (Normalized)"] = Summary_AgePurchasingAnalysis["Age Avg Total Purchase/Person (Normalized)"].map("${:,.2f}".format)
Summary_AgePurchasingAnalysis["Age Purchase Count"] = Summary_AgePurchasingAnalysis["Age Purchase Count"].map("{:,}".format)

print(Summary_AgePurchasingAnalysis)





### Top Spenders
# * Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
#   * SN
#   * Purchase Count
#   * Average Purchase Price
#   * Total Purchase Value

# User Demographics
UserTotal = DataFrame_Orig.groupby(["SN"]).sum()["Price"]
UserTotal = UserTotal.rename("User Total Purchase Value")
print(UserTotal.head())

UserAvg = DataFrame_Orig.groupby(["SN"]).mean()["Price"]
UserAvg = UserAvg.rename("User Average Purchase Value")
print(UserAvg.head())

UserCount = DataFrame_Orig.groupby(["SN"]).count()["Price"]
UserCount = UserCount.rename("User Purchase Count")
print(UserCount.head())

# Summary Data Frame
Summary_UserTotals = pd.DataFrame({"User Total Purchase Value"  : UserTotal
                                  ,"User Avg Purchase Price"    : UserAvg
                                  ,"User Purchase Count"        : UserCount
                                  })

Summary_UserTotals = Summary_UserTotals.sort_values("User Total Purchase Value" , ascending = False)                                

# Data Formatting
Summary_UserTotals["User Avg Purchase Price"] = Summary_UserTotals["User Avg Purchase Price"].map("${:,.2f}".format)
Summary_UserTotals["User Total Purchase Value"] = Summary_UserTotals["User Total Purchase Value"].map("${:,.2f}".format)
Summary_UserTotals["User Purchase Count"] = Summary_UserTotals["User Purchase Count"].map("{:,.2f}".format)

print(Summary_UserTotals.head())






### Most Popular Items
# * Identify the 5 most profitable items by total purchase value, then list (in a table):
#   * Item ID
#   * Item Name
#   * Purchase Count
#   * Item Price
#   * Total Purchase Value


# Pull relevant Item columns into new Data Frame
DF_Items = DataFrame_Orig.loc[: , ["Item ID" , "Item Name" , "Price"]]


# Item Demographics
ItemTotalPurchase = DF_Items.groupby(["Item ID" , "Item Name"]).sum()["Price"]
ItemTotalPurchase = ItemTotalPurchase.rename("Item Total Purchase Value")
print(ItemTotalPurchase.head())

ItemAvgPurchase = DF_Items.groupby(["Item ID" , "Item Name"]).mean()["Price"]
ItemAvgPurchase = ItemAvgPurchase.rename("Item Avg Purchase Value")
print(ItemAvgPurchase.head())

ItemCount = DF_Items.groupby(["Item ID" , "Item Name"]).count()["Price"]
ItemCount = ItemCount.rename("Item Purchase Count")
print(ItemCount.head())

# Summary Data Frame
Summary_ItemTotals = pd.DataFrame({"Item Total Purchase Value"  : ItemTotalPurchase
                                  ,"Item Avg Purchase Price"    : ItemAvgPurchase
                                  ,"Item Purchase Count"        : ItemCount
                                  })

Summary_ItemTotals_MostPopular = Summary_ItemTotals.sort_values("Item Purchase Count" , ascending = False)                                

# Data Formatting
Summary_ItemTotals_MostPopular["Item Avg Purchase Price"] = Summary_ItemTotals_MostPopular["Item Avg Purchase Price"].map("${:,.2f}".format)
Summary_ItemTotals_MostPopular["Item Total Purchase Value"] = Summary_ItemTotals_MostPopular["Item Total Purchase Value"].map("${:,.2f}".format)
Summary_ItemTotals_MostPopular["Item Purchase Count"] = Summary_ItemTotals_MostPopular["Item Purchase Count"].map("{:,.2f}".format)

print(Summary_ItemTotals_MostPopular.head())




### Most Profitable Items
# * Identify the 5 most profitable items by total purchase value, then list (in a table):
#   * Item ID
#   * Item Name
#   * Purchase Count
#   * Item Price
#   * Total Purchase Value


Summary_ItemTotals_MostProfitable = Summary_ItemTotals.sort_values("Item Total Purchase Value" , ascending = False)                                

# Data Formatting
Summary_ItemTotals_MostProfitable["Item Avg Purchase Price"] = Summary_ItemTotals_MostProfitable["Item Avg Purchase Price"].map("${:,.2f}".format)
Summary_ItemTotals_MostProfitable["Item Total Purchase Value"] = Summary_ItemTotals_MostProfitable["Item Total Purchase Value"].map("${:,.2f}".format)
Summary_ItemTotals_MostProfitable["Item Purchase Count"] = Summary_ItemTotals_MostProfitable["Item Purchase Count"].map("{:,.2f}".format)

print(Summary_ItemTotals_MostProfitable.head())





## Analysis
# Heroes Of Pymoli Data Analysis
# Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

# Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).




