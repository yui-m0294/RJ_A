import shutil
shutil.unpack_archive('kabeposter.zip', '')
input_folder = "./kabeposter"
file_name = "kabeposter"

import json

with open('{}/{}_{:0>12d}_keypoints.json'.format(input_folder,file_name,0)) as f:
    df = json.load(f)
print("1人目の鼻のX座標：",df['people'][0]['pose_keypoints_2d'][0])
print("1人目の鼻のY座標：",df['people'][0]['pose_keypoints_2d'][1])
print("1人目の鼻の信頼度：",df['people'][0]['pose_keypoints_2d'][2])
print("1人目の首のX座標：",df['people'][0]['pose_keypoints_2d'][3])
print("1人目の首のY座標：",df['people'][0]['pose_keypoints_2d'][4])
print("1人目の首の信頼度：",df['people'][0]['pose_keypoints_2d'][5])

print("2人目の鼻のX座標：",df['people'][1]['pose_keypoints_2d'][0])
print("2人目の鼻のY座標：",df['people'][1]['pose_keypoints_2d'][1])
print("2人目の鼻の信頼度：",df['people'][1]['pose_keypoints_2d'][2])
print("2人目の首のX座標：",df['people'][1]['pose_keypoints_2d'][3])
print("2人目の首のY座標：",df['people'][1]['pose_keypoints_2d'][4])
print("2人目の首の信頼度：",df['people'][1]['pose_keypoints_2d'][5])
