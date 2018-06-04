#include "array"
#include "common.hpp"
#include "discrete_time.hpp"

struct MonitorExpr {

	std::array<timed_set,1> tstates = std::array<timed_set,1>{timed_set()};
	std::array<timed_set,1> tstates_pre = std::array<timed_set,1>{timed_set()};

	int now = 0;

	void update(double yaw){

		now = now + 1;
		tstates_pre = tstates;

		tstates[0] = update_timed_since_unbounded(tstates[0], true, not(lt(yaw,5.5)), 40, now);
	}

	bool output(){
		return not(output_timed_since(tstates[0], 40, now));
	}
};