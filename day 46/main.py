# from bs4 import BeautifulSoup
# import requests
# date_input=input("Which Year Do You Want To Travel To?Enter The Date in YYYY-MM-DD Format.")
# URL=f"https://www.billboard.com/charts/hot-100/{date_input}"
# response1=requests.get(URL)
# data=response1.text
# soup=BeautifulSoup(data,"html.parser")
# song_titles = soup.find(class_="pmc-paywall")
# # print(song_titles)
# # soup = BeautifulSoup(song_titles, "html.parser")
# song_title=song_titles.find_all(name='h3', id="title-of-a-story", class_="a-font-primary-bold-s")
# song_name=[]
# for item in song_title:
#     t=item.text.strip()
#     song_name.append(t)
# print(song_name[2:10])
# # # print(URL)
# # print(song_title)

from bs4 import BeautifulSoup
import requests

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("http://data.revizify.com/api/v1/courses/create_course",headers={"Authorization":"JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwOTA4NDU3LCJpYXQiOjE2NDkxODA0NTcsImp0aSI6ImY5NjBkZjVkMTVjZjRkMWQ4ZWM5MTY5YWJiNThmZjM0IiwiZW1haWwiOiJhYmhpbmF2c3RjZXRAZ21haWwuY29tIn0.761rPoJfdXaLyzNlMxcIdJXK1t9Y9MoNkDEVO5mngDs"})

# print(response)
print(response.json()["results"][1]["course_name"])
print(response.json()["results"][2]["course_name"])