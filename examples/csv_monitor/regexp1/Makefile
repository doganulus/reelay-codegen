CC=g++
CFLAGS=-o monitor -O2 -pthread -std=c++14 

#
# Note: The flag -pthread is required for compiling csv.h
#

all: generate compile

generate:
	reelay spec.yaml

compile:
	$(CC) $(CFLAGS) main.cpp 

test:
	./monitor ../example.csv

clean:
	rm monitor Monitor*.hpp common.hpp discrete_time.hpp 