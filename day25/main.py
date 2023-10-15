# import csv
# temp=[]
# with open("C:/Users/ASUS/Downloads/weather_data.csv") as file:
#     data=csv.reader(file)
#     for i in data:
#         if(i[1]!='temp'):
#             temp.append(int(i[1]))
#     print(temp)
import pandas 
data=pandas.read_csv("C:/Users/ASUS/Downloads/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data[data.day=='Monday'])
# print(data[data.temp==(data.temp.max())])
# monday=data[data.day=="Monday"]
# print(monday)
# print(((monday.temp*9)/5)+32)
# v=data.Primary
# print(v)
black=len(data[data.Primary=='Black'])
grey=len(data[data.Primary=='Gray'])
red=len(data[data.Primary=='Cinnamon'])
# print(black)
# print(grey)
# print(red)
d={"FUR":['BLACK','GREY','CINNAMON'],"COUNT":[black,grey,red]}        
d1=pandas.DataFrame(d)
d1.to_csv("new.csv")