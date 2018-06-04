
PATTERN="always[>=40] lt(yaw:double, 5.5)"

# PATTERN="lt(yaw:double, 2.4) since[20,35] gt(roll:double, 2.5)"

all: generate

generate:
	tl2cpp --with-headers --outdir monitor/include $(PATTERN)

test:
	rosrun monitor monitor

clean:
	rm monitor/include/Monitor*.hpp monitor/include/common.hpp monitor/include/discrete_time.hpp 