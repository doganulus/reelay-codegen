#include "array"
#include "common.hpp"
#include "discrete_time.hpp"

struct MonitorExpr2 {

	std::array<bool,3> states = std::array<bool,3>{0,0,0};
	std::array<bool,3> states_pre = std::array<bool,3>{0,0,0};

	void update(double pitch, double roll, double yaw){

		states_pre = states;

		states[0] = (true and lt(yaw,5.5));
		states[1] = (lt(roll,5.5) and states_pre[0]);
		states[2] = (states_pre[1] and lt(pitch,5.5));
	}

	bool output(){
		return states[2];
	}
};