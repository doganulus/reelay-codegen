#include "array"
#include "common.hpp"
#include "discrete_time.hpp"

struct MonitorExpr {

	std::array<bool,2> states = std::array<bool,2>{0,0};
	std::array<bool,2> states_pre = std::array<bool,2>{0,0};

	void update(bool p2, double x){

		states_pre = states;

		states[0] = (true and lt(x,4.5));
		states[1] = (states_pre[0] and p2);
	}

	bool output(){
		return states[1];
	}
};