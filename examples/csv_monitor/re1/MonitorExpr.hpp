#include "array"
#include "common.hpp"
#include "discrete_time.hpp"

struct MonitorExpr {

	std::array<bool,2> states = std::array<bool,2>{0,0};
	std::array<bool,2> states_pre = std::array<bool,2>{0,0};

	void update(bool p1, bool p2){

		states_pre = states;

		states[0] = (true and p2);
		states[1] = ((states_pre[0] or states_pre[1]) and p1);
	}

	bool output(){
		return states[1];
	}
};