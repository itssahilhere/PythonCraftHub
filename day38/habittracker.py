from datetime import datetime
import requests
pixela_end_point="https://pixe.la/v1/users" 
USERNAME='sahilagarwalsahil'
TOKEN='SAHIL@123420'
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":'yes',
    "notMinor":'yes'
}
today=datetime.now()
format_date=today.strftime("%Y%m%d")
# response=requests.post(url=pixela_end_point,json=user_params)
# print(response.text)
graph_endpoint= f"{pixela_end_point}/{USERNAME}/graphs"
graph_header={
    "X-USER-TOKEN":TOKEN
}
graph_params={
    "id":"graph1",
    "name":"studytracker",
    "unit":"hours",
    "type":"int",
    "color":"momiji"
}
# response=requests.post(url=graph_endpoint,json=graph_params,headers=graph_header)
# print(response.text)
post_endpoint=f"{pixela_end_point}/{USERNAME}/graphs/graph1"
pixel_header={
    "X-USER-TOKEN":TOKEN
}
params={
    "date":format_date,
    "quantity":"10",

}

# response=requests.post(url=post_endpoint,json=params,headers=pixel_header)
# print(response.text)
# print(format_date)
end_point=f"{pixela_end_point}/{USERNAME}/graphs/graph1/{format_date}"
end_par={
    "quantity":"2"
}
response=requests.put(url=end_point,json=end_par,headers=pixel_header)
print(response.text)