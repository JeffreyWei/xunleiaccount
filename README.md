#抓取当日VIP账号


##迅雷会员


* 迅雷数据源1

	[http://521xunlei.com](http://521xunlei.com)
	
		$ curl https://raw.githubusercontent.com/JeffreyWei/xunleiaccount/master/xunlei.py > xunlei.py		
	![](http://images.weiphone.net/data/attachment/forum/201505/29/113947kl6hwllwwwwbx3bt.png)
	
		$ python  xunlei.py
	![](http://images.weiphone.net/data/attachment/forum/201505/28/140212h82thg0at899z4bi.png)
	
* 迅雷数据源2
	
	[http://http://xlfans.com](http://http://xlfans.com)
	
		$ curl https://raw.githubusercontent.com/JeffreyWei/xunleiaccount/master/xunlei2.py > xunlei2.py
		$ python  xunlei2.py

* 视频站点数据源

	[http://www.vipfenxiang.com](http://www.vipfenxiang.com)
	
		$ curl https://raw.githubusercontent.com/JeffreyWei/xunleiaccount/master/video.py > video.py
		$ python  video.py

##快速执行

	$ curl https://raw.githubusercontent.com/JeffreyWei/xunleiaccount/master/xunlei.py | python
   
   
   
   
**依赖安装**
	
	$ sudo pip install beautifulsoup