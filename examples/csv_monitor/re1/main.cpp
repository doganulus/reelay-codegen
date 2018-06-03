#include "iostream"
#include "array"
#include "../csv.h"

#include "MonitorExpr.hpp"

int main(int argc, char **argv){
    
    int output = 0;
    
    io::CSVReader<2> reader(argv[1]);
    reader.read_header(io::ignore_extra_column, "p1", "p2");
    int p1, p2;

    MonitorExpr monitor = MonitorExpr();
    
    std::cout << "p1" << " " << "p2" << " " << "output" << std::endl;    
    while(reader.read_row(p1, p2)){
        monitor.update(p1, p2);
        output = monitor.output();
        std::cout << p1 << "  " << p2 << "  " <<output << std::endl;
    }
}
