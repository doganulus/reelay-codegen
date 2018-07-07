#include "ros/ros.h"
#include "std_msgs/Bool.h"
#include "geometry_msgs/Twist.h"

#include "MonitorExpr2.hpp"

struct MonitorExpr2Handler : MonitorExpr2 {

	ros::NodeHandle nh;

	ros::Subscriber sub = nh.subscribe("GyroData", 1, &MonitorExpr2Handler::callback, this);
	ros::Publisher pub = nh.advertise<std_msgs::Bool>("Expr2", 1);
	std_msgs::Bool msgout;

	void callback(const geometry_msgs::Twist &msg){

		this->update(msg.angular.z, msg.angular.y, msg.angular.x);
		msgout.data = this->output();
		ROS_INFO("%d", msgout.data);
		pub.publish(msgout);
	}
};

int main(int argc, char **argv){

	ros::init(argc, argv, "Expr2");
	MonitorExpr2Handler mh = MonitorExpr2Handler();
	ros::spin();
	return 0;
}