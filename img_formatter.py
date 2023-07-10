import os
import numpy as np
from tqdm import tqdm
import cv2

folder_path = "IMG"
savefolder_path="EXPORT"
file_list = [filename for filename in os.listdir(folder_path) if filename.endswith(('.jpg', '.png'))]

w,h = 2048, 2048

frame = cv2.imread("frame.png",-1)
frame_img, frame_op=frame[:,:,:3], frame[:,:,3]
print(f"# of photo : {len(file_list)}")
for filename in tqdm(file_list):
    img_path = os.path.join(folder_path, filename)

    img = cv2.imread(img_path)
    
    r=img.shape[0]/img.shape[1] 
    
    (new_w, new_h) =  (2048, int(2048 * r)) if r<1 else ( int( 2048 / r), 2048) 

    resized_img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    
    x, y = int((w - new_w) / 2), int((h - new_h) / 2)

    bg = np.full((2048, 2048, 3), 255, dtype=np.uint8)        
    bg[y:y+new_h, x:x+new_w] = resized_img
    bg=np.where(frame_op[...,None]>0, frame_img,bg)

    save_path = os.path.join(savefolder_path,"picdonghyuk_"+filename)
    cv2.imwrite(save_path, bg)
