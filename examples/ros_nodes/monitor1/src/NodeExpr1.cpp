#include "ros/ros.h"
#include "std_msgs/Bool.h"
#include "geometry_msgs/Twist.h"

#include "MonitorExpr1.hpp"

struct MonitorExpr1Handler : MonitorExpr1 {

	ros::NodeHandle nh;

	ros::Subscriber sub = nh.subscribe("GyroData", 1, &MonitorExpr1Handler::callback, this);
	ros::Publisher pub = nh.advertise<std_msgs::Bool>("Expr1", 1);
	std_msgs::Bool msgout;

	void callback(const geometry_msgs::Twist &msg){

		this->update(msg.angular.z, msg.angular.y, msg.angular.x);
		msgout.data = this->output();
		ROS_INFO("%d", msgout.data);
		pub.publish(msgout);
	}
};

int main(int argc, char **argv){

	ros::init(argc, argv, "Expr1");
	MonitorExpr1Handler mh = MonitorExpr1Handler();
	ros::spin();
	return 0;
}