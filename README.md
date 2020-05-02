# photograph-location
A python script that allows you to see the information such as the time,location,manufactor of the camera and so on.
<br>这是一个简单但十分有效的Python脚本，用来调取图片文件中的EXIF信息并提取出拍摄时间、摄像机型号，拍摄地址等信息。<br>
原本我设想的是写一个调取图片拍摄时间的小工具，在经过了一番研究之后，我发现了EXIFREAD这个好用的库，顺藤摸瓜，就写出了这个功能更加完善的小工具。<br>
运行依赖：Python3，requests库，exifread库<br>
使用百度地图开放平台的全球逆地理编码服务（http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding）
