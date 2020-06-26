import requests
import json

def aimagazine():
    output=[]
    response=requests.get("https://ai-magazine.com/~api/papers/d3d6f972-fd0b-4bcd-a97c-53de828ee59e?")
    data=json.loads(response.text)
    for i in range(0,15):
        #print(data['data']['edition']['headlines']['content'])
        opdict={
        "url" : data['data']['edition']['headlines']['content'][i]['url'] ,
        "image" : data['data']['edition']['headlines']['content'][i]['img'] ,
        "title" : data['data']['edition']['headlines']['content'][i]['title'] ,
        "des" :  data['data']['edition']['headlines']['content'][i]['content'] ,
        "time" : data['data']['edition']['headlines']['content'][i]['source']['timestamp']
        }
        output.append(opdict)
            

       
    return print(output)



if __name__ == "__main__":
    aimagazine()