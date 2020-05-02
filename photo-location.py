import requests
import exifread
import random
title = ['''
 ___                                 _                    _   _             
|_ _|_ __ ___   __ _  __ _  ___     | |    ___   ___ __ _| |_(_) ___  _ __  
 | || '_ ` _ \ / _` |/ _` |/ _ \    | |   / _ \ / __/ _` | __| |/ _ \| '_ \ 
 | || | | | | | (_| | (_| |  __/    | |__| (_) | (_| (_| | |_| | (_) | | | |
|___|_| |_| |_|\__,_|\__, |\___|    |_____\___/ \___\__,_|\__|_|\___/|_| |_|
                     |___/                                               
''', '''
 mmmmm                             
   #    mmmmm   mmm    mmmm   mmm  
   #    # # #  "   #  #" "#  #"  # 
   #    # # #  m"""#  #   #  #"""" 
 mm#mm  # # #  "mm"#  "#m"#  "#mm" 
                       m  #        
                        ""                                                                 

 m                             m      m                 
 #       mmm    mmm    mmm   mm#mm  mmm     mmm   m mm  
 #      #" "#  #"  "  "   #    #      #    #" "#  #"  # 
 #      #   #  #      m"""#    #      #    #   #  #   # 
 #mmmmm "#m#"  "#mm"  "mm"#    "mm  mm#mm  "#m#"  #   # 

''']

class GetPhotoInfo:
    def __init__(self, photo):
        self.photo = photo
        # 百度地图ak
        #self.ak = 'nYPs4LQ9a4VhVxj55AD69K6zgsRy9o4z'
        self.ak='G3i59YOR4pVp0GIKnSXNTzwoRO65rPtZ'
        self.location = self.get_photo_info()

    def get_photo_info(self, ):
        with open(self.photo, 'rb') as f:
            tags = exifread.process_file(f)
        try:
            # 打印照片其中一些信息
            print('拍摄时间：', tags['EXIF DateTimeOriginal'])
            print('照相机制造商：', tags['Image Make'])
            print('照相机型号：', tags['Image Model'])
            print('照片尺寸：', tags['EXIF ExifImageWidth'], tags['EXIF ExifImageLength'])
            # 纬度
            lat_ref = tags["GPS GPSLatitudeRef"].printable
            lat = tags["GPS GPSLatitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
            lat = float(lat[0]) + float(lat[1]) / 60 + float(lat[2]) / float(lat[3]) / 3600
            if lat_ref != "N":
                lat = lat * (-1)
            # 经度
            lon_ref = tags["GPS GPSLongitudeRef"].printable
            lon = tags["GPS GPSLongitude"].printable[1:-1].replace(" ", "").replace("/", ",").split(",")
            lon = float(lon[0]) + float(lon[1]) / 60 + float(lon[2]) / float(lon[3]) / 3600
            if lon_ref != "E":
                lon = lon * (-1)
        except KeyError:
            return "ERROR:请确保照片包含经纬度等EXIF信息。"
        else:
            print("经纬度：", lat, lon)
            return lat, lon

    def get_location(self):
        url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak={}&output=json' \
              '&coordtype=wgs84ll&location={},{}'.format(self.ak, *self.location)
        response = requests.get(url).json()
        status = response['status']
        if status == 0:
            address = response['result']['formatted_address']
            print('详细地址：', address)
        else:
            print('baidu_map error')


if __name__ == '__main__':
    print(random.choice(title))
    Main = GetPhotoInfo(input("filename:"))
    Main.get_location()

