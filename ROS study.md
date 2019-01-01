---
cn/ROS/Tutorials  
website:http://wiki.ros.org/cn/ROS/Tutorials  
Made by LANRF11.
---

##1  
rosbuild 和 catkin：目前两种用来组织和编译ROS应用程序的不同的方法。  
一般而言，rosbuild比较简单也易于使用，而catkin使用了更加标准的CMake规则，所以比较复杂，但是也更加灵活，特别是对于那些想整合外部现有代码或者想发布自己代码的人。

##2  
Nodes:节点,一个节点即为一个可执行文件，它可以通过ROS与其它节点进行通信。  
Messages:消息，消息是一种ROS数据类型，用于订阅或发布到一个话题。  
Topics:话题,节点可以发布消息到话题，也可以订阅话题以接收消息。  
Master:节点管理器，ROS名称服务 (比如帮助节点找到彼此)。  
rosout: ROS中相当于stdout/stderr。  
roscore: 主机+ rosout + 参数服务器 。   

##3  
roscore 是你在运行所有ROS程序前首先要运行的命令。   
打开一个新的终端, 可以使用 rosnode 像运行 roscore 一样看看在运行什么...   
rosrun 允许你使用包名直接运行一个包内的节点(而不需要知道这个包的路径)。   

##4ROS Topics  
turtlesim_node节点和turtle_teleop_key节点之间是通过一个ROS话题来互相通信的。turtle_teleop_key在一个话题上发布按键输入消息，而turtlesim则订阅该话题以接收该消息。  
话题之间的通信是通过在节点之间发送ROS消息实现的。对于发布器(turtle_teleop_key)和订阅器(turtulesim_node)之间的通信，发布器和订阅器之间必须发送和接收相同类型的消息。这意味着话题的类型是由发布在它上面的消息类型决定的。  
rostopic list:列出所有当前订阅和发布的话题 rostopic list -h;rostopic list -v  
rostopic type 命令用来查看所发布话题的消息类型。rostopic type [topic]  
rostopic pub可以把数据发布到当前某个正在广播的话题上 rostopic pub [topic] [msg_type] [args]  
  
eg:
$ rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'  
rostopic pub    这条命令将会发布消息到某个给定的话题。   
1    （单个破折号）这个参数选项使rostopic发布一条消息后马上退出。   
/turtle1/command_velocity    这是消息所发布到的话题名称。  
turtlesim/Velocity    这是所发布消息的类型。  
-- （双破折号）这会告诉命令选项解析器接下来的参数部分都不是命令选项。这在参数里面包含有破折号-（比如负号）时是必须要添加的。   
rostopic hz命令可以用来查看数据发布的频率。 rostopic hz [topic]  

