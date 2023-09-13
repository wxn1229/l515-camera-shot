
import pyrealsense2 as rs
import numpy as np
import cv2 as cv
from PIL import Image
import csv


#設定

img_num = 1 

pipeline = rs.pipeline()
config = rs.config()
output_path = "img"





#調整解析度
config.enable_stream(rs.stream.color, 960, 540, rs.format.bgr8, 30)
config.enable_device('f0233004')



# 啟動深度攝影機
profile = pipeline.start(config)



#pipeline.start(config)
for repeat in range(20):

#影像
    while True:
        #取得照片frame
        frame = pipeline.wait_for_frames()
        #把兩種frames對齊
        color = frame.get_color_frame()

        #轉換成圖片img
        color_img = np.asanyarray(color.get_data())

    
        # depth_cmap = cv.applyColorMap(cv.convertScaleAbs(depth_img, alpha = 0.25),cv.COLORMAP_JET)
    

        


        #
        
        
        
        
        #顯示圖片
        cv.imshow('rgb',color_img)
        
        #cv.imshow('depth',depth_cmap)
        #print(dist)
        #print(real_height, ' meter')
        
        
        #按Q就會拍照
        


        key = cv.waitKey(1)
        if key == ord('s'):

            cv.imwrite(output_path + f"/image_{img_num}.jpg" ,color_img)
            print("Image:", img_num )
            

            

            

            img_num += 1
        elif key == ord('q'):
            break
    
    #print(real_height_map)





    
    
    
    



        
#取得拍照當下的照片
# color_save_img = Image.fromarray(np.uint8(color_img))
# color_save_img.save("img/color_img.jpg","JPEG")
#print('height,width' , (height,width))


        

pipeline.stop()
