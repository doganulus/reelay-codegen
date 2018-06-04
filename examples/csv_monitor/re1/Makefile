CC=g++
CFLAGS=-o monitor -O2 -pthread -std=c++11 

PATTERN="p2;p1+"
# PATTERN="p2;p1+"

all: generate
	$(CC) $(CFLAGS) main.cpp 

generate:
	re2cpp --with-headers $(PATTERN)

test:
	./monitor example.csv

clean:
	rm monitor Monitor*.hpp common.hpp discrete_time.hpp 