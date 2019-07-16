# LenovoY 7000安装、配置Ubuntu16.04记录
## 1.安装Ubuntu16.04
参考：https://blog.csdn.net/flyyufenfei/article/details/79187656  
**注意**：   
1.安装类型；  
2.分区、类型及容量。

## 2.初次启动
**注意**：  
在选择启动项时按e进入启动项修改，在quiet splash后添加nomodeset，然后按F10进入ubuntu系统。  
如果没此步骤，可能无法进入ubuntu系统。

## 3.无线网设置
参考：https://blog.csdn.net/u011133135/article/details/78722440    
**注意**：  
1.sudo touch /etc/modprobe.d/ideapad.conf  
2.sudo gedit ideapad.conf  
3.添加：blacklist ideapad_laptop   
4.sudo modprobe -r ideapad_laptop
5.reboot

## 4.安装显卡驱动
参考：https://blog.csdn.net/u014682691/article/details/80605201  
**注意**：  
1.若修改了启动/etc/defeat/grub(添加nomodeset)，在安装显卡驱动后删除nomodeset；  
2.安装显卡后可以调节屏幕亮度；
3.若安装后终端nvidia-smi无显卡驱动信息输出，则重启再输入，若仍无输出则安装存在问题。

## 5.安装cuda
参考：https://blog.csdn.net/myg22/article/details/84029924  
**注意**：  
1.安装cudnn:
2.注意cuda,cudnn版本对应关系（如果安装tensorflow-gpu，则考虑三者之间的关系）；
3.若已安装显卡驱动，则是否安装显卡加速时选择n。

## 6.安装搜狗输入法  
参考：https://blog.csdn.net/areigninhell/article/details/79696751
**注意**：  
1.添加搜狗输入法时注意去掉“只显示当前语言”选项。

## 7.安装ROS
参考：http://wiki.ros.org/cn/kinetic/Installation/Ubuntu  
**注意**：  
ROS和ubuntu对应版本

## 8.安装anaconda
参考：https://blog.csdn.net/lwplwf/article/details/79162470
**注意**：  
1.下载：https://www.anaconda.com/download/#linux  
2.安装： bash Anaconda3-xxx-Linux-x86_64.sh  
3.路径：source ~/.bashrc  
4.验证：（终端）which python，输出/home/(user)/anaconda3/bin/python

## 9.安装tensorflow-gpu
注意：  
1.conda create -n tensorflow python=3.5；  
2.source activate tensorflow;  
3.pip install tensorflow-gpu==1.12.0；  
4.验证：
~~~python
python
import tensorflow as tf
tf.__version__
~~~

