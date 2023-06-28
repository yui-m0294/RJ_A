import shutil
shutil.unpack_archive('kabeposter.zip', '')
input_folder = "./kabeposter"
file_name = "kabeposter"

import json

with open('{}/{}_{:0>12d}_keypoints.json'.format(input_folder,file_name,0)) as f:
    df = json.load(f)
    
import tkinter as tk

root = tk.Tk()
root.geometry("2000x2000")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_line(df['people'][0]['pose_keypoints_2d'][6], df['people'][0]['pose_keypoints_2d'][7], df['people'][0]['pose_keypoints_2d'][15], df['people'][0]['pose_keypoints_2d'][16], fill = "black")
canvas.create_line(df['people'][1]['pose_keypoints_2d'][6], df['people'][1]['pose_keypoints_2d'][7], df['people'][1]['pose_keypoints_2d'][15], df['people'][1]['pose_keypoints_2d'][16], fill = "black")

root.mainloop()