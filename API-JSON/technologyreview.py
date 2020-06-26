import requests
import json

def technologyreview():
    output=[]
    response=requests.get("https://wp.technologyreview.com/wp-json/irving/v1/data/the_feed?page=1")
    data=json.loads(response.text)
    for i in range(0,10):
        if(data[i]['name']=="ad-unit"):
            continue


        if(data[i]['name']=="feed-anchor"):
            opdict={
            "url" : data[i]['config']['permalink'],
            "image" : data[i]['children'][1]['config']['src'],
            "title" : data[i]['config']['name'],
            "des" :  data[i]['config']['description'],
            "time" : 'null'
            }
            output.append(opdict)
            for j in range(2,5):
                opdict={
                "url" : data[i]['children'][j]['config']['permalink'] ,
                "image" : 'null',
                "title" : data[i]['children'][j]['config']['title'],
                "des" :  'null',
                "time" : data[i]['children'][j]['config']['publishedDate']
                }
                output.append(opdict)


        if(data[i]['name']=="teaser-item" or data[i]['name']=="sponsored" or data[i]['name']=="feed-item"):
            if(data[i]['name']=="teaser-item"):
                desc=data[i]['config']['excerpt']
            else:
                desc=data[i]['config']['teaserContent']
            print(i)
            try:
                img = data[i]['children'][0]['config']['src']
            except:
                pass
            opdict={
            "url" :   data[i]['config']['permalink'],
            
            # "image" :   data[i]['children'][0]['config']['src'],
            "image" : img,
            
            "title" :   data[i]['config']['title'],
            "des" :  desc,
            "time" :   data[i]['config']['postDate']
            }
            output.append(opdict)
            
    return print(*output,sep="\n")



if __name__ == "__main__":
    technologyreview()