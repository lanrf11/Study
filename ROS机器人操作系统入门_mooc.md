---
ROS机器人操作系统入门-中国大学MOOC
中科院软件所柴长坤老师  
https://www.bilibili.com/video/av24585414/?p=1
---
## 1 ROS介绍  
ROS：Robot Operation System  
ROS:中间件/类操作系统，连接系统和软件，提供了类似操作系统的功能，“框架+工具+功能+社区”。  
框架：分布式架构，进程管理，进程间通信  
node节点（进程）  
工具：rviz,gazebo等基础工具，仿真和调试  
功能：基础功能包，控制、规划、视觉、建图。可在roswiki、github中查找  
社区：
IDE:roboware

## 2 ROS文件结构  
### 2.1catkin_ws  
1src:源代码 2build:cmake&make缓存、中间文件 3devel：目标文件 （只需编写1，自动生成23）   
1.1package1 1.2package2 ...（package:catkin编译的基本单元）  
catkin工作空间：组织管理功能包的文件夹  
catkin:ros定制的编译构建系统，对CMake的扩展  
catkin_make：建立工作空间、编译，需在catkin_ws目录下，编译后刷新环境source ～/catkin_ws/devel/setup.bash  
### 2.2package  
package功能包：ros软件的基本组织形式，catkin编译的基本单元，一个package可包含多个可执行文件（节点）  
package：包含CMakeLists.txt、package.xml文件  
CMakeLists.txt:规定catkin编译的规则（源文件、依赖项、目标文件） 
package.xml：定于package属性（包名、版本号、作者、依赖项等），一般只修改依赖项  
manifest.xml:rosbuild编译系统采用的信息清单，类似catkin的package.xml  
代码文件：两种，1脚本（shell、python）2C++(头文件、源文件)
package:放代码，自定义通信格式(消息msg、服务srv、动作action)、lauch（一次性执行多个文件 ）以及配置文件（yaml）  
1CMakeLists.txt 2package.xml 3scripts(*.sh、*.py) 4incude(*.h) 5src(*.cpp)   
此外：自定义通信6msg（*.msg）7.srv(*.srv)8.action(*.action) lauch文件及配置文件9lauch（*.lauch）10config(*.yaml)  
常用指令：
1.rospack：  
$rospack find package_name：查找某个pkg地址  
$rospack list:列出本地所有的pkg  
2.roscd:  
$roscd package_name:跳转到某个pkg路径下  
3.rosls:  
$rosls package_name:列举某个pkg下的文件信息  
4.rosed:  
$rosed package_name file_name:编辑pkg中文件  
5.catkin_create_pkg:  
$catkin_create_pkg <pkg_name>  [deps]:创建一个pkg  
6.rosdep:  
$rosdep install [pkg_name]:安装某个pkg所需的依赖项  
