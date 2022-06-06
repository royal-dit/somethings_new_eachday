#working with csv data and pandas library

#Reading Csv Data file in python

# with open("Weather_data.csv") as data_files:
#      data = data_files.readlines()
#      print(data)

import  csv

# with open("Weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#          temp.append(int(row[1]))
#     print(temp)

# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])


# Dataframes and seris working with rows and column
import pandas
data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)
#
# avg_temp =sum(temp_list)/len(temp_list)
# print(f"The avg temp is {avg_temp}")
# mean = data['temp'].mean()
# print(f"the mean of the temp is {mean}")
#
# max_value= data['temp'].max()
# print(f"the maximum value is {max_value}")

#set data in condtion

#getting data from row
# print(data[data.Day == 'Monday'])

# print(data[data.temp == data.temp.max()])    #printing the row fro max temp

# monday = data[data.Day == 'Monday']
# print(monday.Condtion)

# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9/5 +32
# print(f"the farenheit for monday is   {monday_temp_f}")

#create data frame from scratch

data_dict = {
    "students":["Any","James","Angela"],
    "Scores":[76,56,65]
}
data1 = pandas.DataFrame(data_dict)
print(data1)
data1.to_csv("new_data.csv")




