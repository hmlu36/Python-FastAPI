from fastapi import FastAPI

import imageio
import pygifsicle 


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Hello from FastAPI!"}

@app.get("/gif")
def read_root():
    filenames = [
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131600.png', 
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131610.png', 
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131620.png', 
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131630.png', 
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131640.png', 
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131650.png',
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131700.png',
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131710.png', 
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131720.png', 
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131730.png', 
        'https://www.cwb.gov.tw/Data/radar/CV1_3600_202307131740.png']
    images = [ ]

    for filename in filenames:
    images.append(imageio.imread(filename))

    imageio.mimsave('radar.gif', images, duration = 60)
    pygifsicle.optimize('radar.gif', 'radar-opt.gif') 
    return {"gif": "radar-opt.gif"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}