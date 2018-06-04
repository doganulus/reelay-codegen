#include "ros/ros.h"
#include "std_msgs/Bool.h"
#include "geometry_msgs/Vector3.h"

#include "MonitorExpr.hpp"

struct MonitorExprHandler:MonitorExpr {

  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("GyroData", 1, &MonitorExprHandler::callback, this);
  ros::Publisher pub = nh.advertise<std_msgs::Bool>("ExprHolds", 1);

  std_msgs::Bool msgout;

  void callback(const geometry_msgs::Vector3 &msg){

    this->update(msg.x, msg.y);
    
    msgout.data = this->output();
    ROS_INFO("%d", msgout.data);

    pub.publish(msgout);
    
  }
};

int main(int argc, char **argv)
{

  ros::init(argc, argv, "monitor");

  MonitorExprHandler mh = MonitorExprHandler();

  ros::spin();

  return 0;
}