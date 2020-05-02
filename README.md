# photograph-location
A python script that allows you to see the information such as the time,location,manufactor of the camera and so on.
这是一个简单但十分有效的Python脚本，用来调取图片文件中的EXIF信息并提取出拍摄时间、摄像机型号，拍摄地址等信息。
原本我设想的是写一个调取图片拍摄时间的小工具，在经过了一番研究之后，我发现了EXIFREAD这个好用的库，顺藤摸瓜，就写出了这个功能更加完善的小工具。不过介于我的电脑操作系统限制，无法封装为Windows/Dos可执行文件，只能提供源代码，不过如果老师可以运行Linux系统下的可执行文件，我也愿意提供。
运行依赖：Python3，requests库，exifread库
使用百度地图开放平台的全球逆地理编码服务（http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding）
