#include "ros/ros.h"
#include "std_msgs/Bool.h"
#include "geometry_msgs/Vector3.h"

#include "MonitorExpr.hpp"


/*
 * This node implements a ROS node to monitor an input channel (topic)  
 * for a given temporal pattern. The base monitor is automatically generated 
 * from formal specifications such as regular expressions and temporal logic.
 */

struct MonitorExprHandler:MonitorExpr {

  ros::NodeHandle nh;

  /*
   * The input channel to be monitored. 
   *  (Defined by the user. Here it is GyroData.)
   *
   * The input message type 
   *  (Defined by the user. Here it is geometry_msgs/Vector3.)
   *
   * Callback function is explained below.
   * Queue sizes are not critical at this point and chosen as 1.
   *
   */
  ros::Subscriber sub = nh.subscribe("GyroData", 1, &MonitorExprHandler::callback, this);

  /*
   * The output channel. 
   *  (Defined by the user. Here its name is ExprHolds.)
   * 
   * The output message type is Boolean. 
   *  (Defined by the formalism. Currently it is Boolean for all supported formalisms.)
   *
   */
  ros::Publisher pub = nh.advertise<std_msgs::Bool>("ExprHolds", 1);
  std_msgs::Bool msgout;

  /*
   * The callback function is called whenever an input message is received. It updates 
   * the internal state of the monitor and immediately publishes the current output, 
   * which indicates whether the expression holds at this point in time. 
   * 
   */
  void callback(const geometry_msgs::Vector3 &msg){

    /*
     * Update the internal state of the monitor. Arguments are defined by the pattern 
     * used to generate the monitor at the first place.
     *
     * Here we used a metric temporal logic formula "always[>=40] lt(x:double, 5.5)", 
     * which specify that the variable x is always less than 5.5 at least for 40 time 
     * units.  
     * 
     * Since there is only one variable (which is x) in this pattern, 
     * the update function has one argument accordingly.
     */
    this->update(msg.x);
    
    /*
     * Get the current output from the monitor and publish. 
     */
    msgout.data = this->output();
    ROS_INFO("%d", msgout.data);

    pub.publish(msgout);
    
  }
};

int main(int argc, char **argv)
{

  /* 
   * Nothing special here. Initialize the node and instantiate the monitor.
   */

  ros::init(argc, argv, "monitor");
  MonitorExprHandler mh = MonitorExprHandler();

  ros::spin();

  return 0;
}