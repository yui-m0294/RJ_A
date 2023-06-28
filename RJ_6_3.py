import os
import json
import numpy as np
from PIL import Image, ImageDraw


input_folder = "./kabeposter"
movie_name = "kabeposter"
num_of_frames = 100

pictures=[]

a = [i*0 for i in range(num_of_frames)]
b = [i*0 for i in range(num_of_frames)]
#ディレクトリ作成
os.makedirs('./kabeposter_coordinate',exist_ok=True)
       


for i in range(0,num_of_frames):
    img = Image.new('RGB', (2000, 2000), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    file_name = "{}/{}_{:0>12d}_keypoints.json".format(input_folder,movie_name,i)
    json_open = open(file_name,'r')
    json_load = json.load(json_open) #jsonファイル読み込み

    if (len(json_load["people"]) == 2):
        a = np.array(json_load['people'][0]['pose_keypoints_2d']).reshape(25, 3)
        b = np.array(json_load['people'][1]['pose_keypoints_2d']).reshape(25, 3)

#左
#肩1直線
        draw.line(((a[2][0],a[2][1]),(a[1][0],a[1][1]),(a[5][0],a[5][1])),fill=(0, 0,0))
            #右肩から右腕
        draw.line(((a[2][0],a[2][1]),(a[3][0],a[3][1]),(a[4][0],a[4][1])),fill=(0, 0,0))
        #左肩から左腕
        draw.line(((a[5][0],a[5][1]),(a[6][0],a[6][1]),(a[7][0],a[7][1])),fill=(0, 0,0))
        
            
        #体の中央
        draw.line(((a[1][0],a[1][1]),(a[8][0],a[8][1]),(a[9][0],a[9][1])),fill=(0, 0,0))
        draw.line(((a[8][0],a[8][1]),(a[12][0],a[12][1])),fill=(0, 0,0))
        #顔
        draw.line(((a[1][0],a[1][1]),(a[0][0],a[0][1]),(a[15][0],a[15][1])),fill=(0, 0,0))
        draw.line(((a[0][0],a[0][1]),(a[16][0],a[16][1])),fill=(0, 0,0))
        
        #右
        draw.line(((b[2][0],b[2][1]),(b[1][0],b[1][1]),(b[5][0],b[5][1])),fill=(0, 0,0))
        #右肩から右腕
        draw.line(((b[2][0],b[2][1]),(b[3][0],b[3][1]),(b[4][0],b[4][1])),fill=(0, 0,0))
        #左肩から左腕
        draw.line(((b[5][0],b[5][1]),(b[6][0],b[6][1]),(b[7][0],b[7][1])),fill=(0, 0,0))
    
        
        #体の中央
        draw.line(((b[1][0],b[1][1]),(b[8][0],b[8][1]),(b[9][0],b[9][1])),fill=(0, 0,0))
        draw.line(((b[8][0],b[8][1]),(b[12][0],b[12][1])),fill=(0, 0,0))
        #顔
        draw.line(((b[1][0],b[1][1]),(b[0][0],b[0][1]),(b[15][0],b[15][1])),fill=(0, 0,0))
        draw.line(((b[0][0],b[0][1]),(b[16][0],b[16][1])),fill=(0, 0,0))
    
        #img.show()
        img.save('kabeposter_coordinate/kabeposter_'+str(i)+'.png', quality=95) #全フレーム画像保存

import tkinter as tk
a = 0
def animation():
    global a
    a = (a+1)%100
    # 前フレームの描画を削除
    canvas.delete("kabeposter")
    # 描画する位置を設定
    canvas.create_image(1000,800,image = pictures[a],tag="kabeposter")
    # アニメーションの実行
    root.after(100,animation)
    if(a==0):
        root.destroy()
    
root = tk.Tk()
root.title("Animation")

# canvasを作成
canvas = tk.Canvas(width=2000,height=5000)
# canvasを配置
canvas.pack()

for i in range(0,num_of_frames):
    pic_name = tk.PhotoImage(file ='kabeposter_coordinate/kabeposter_'+str(i)+'.png')
    pictures.append(pic_name)

#出力
animation()
root.mainloop()