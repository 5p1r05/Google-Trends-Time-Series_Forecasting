from pytrendsdaily import getDailyData
data = getDailyData('\"pneumonia symptoms\"', 2009, 2019)

data.to_csv("pneumonia2.csv")