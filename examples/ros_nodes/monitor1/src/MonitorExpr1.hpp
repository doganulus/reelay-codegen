#include "array"
#include "common.hpp"
#include "discrete_time.hpp"

struct MonitorExpr1 {

	std::array<bool,2> states = std::array<bool,2>{0,0};
	std::array<bool,2> states_pre = std::array<bool,2>{0,0};

	std::array<timed_set,1> tstates = std::array<timed_set,1>{timed_set()};
	std::array<timed_set,1> tstates_pre = std::array<timed_set,1>{timed_set()};

	int now = 0;

	void update(double pitch, double roll, double yaw){

		now = now + 1;
		states_pre = states;
		tstates_pre = tstates;

		states[0] = (lt(roll,5.5) and lt(yaw,5.5));
		states[1] = (states[0] and lt(pitch,5.5));
		tstates[0] = update_timed_since_unbounded(tstates[0], true, not(states[1]), 40, now);
	}

	bool output(){
		return not(output_timed_since(tstates[0], 40, now));
	}
};