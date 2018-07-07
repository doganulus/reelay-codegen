cmake_minimum_required(VERSION 2.8.3)
project(csvreader)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES csvreader
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
# add_library(${PROJECT_NAME}
#   src/${PROJECT_NAME}/csvreader.cpp
# )

add_executable(csvreader src/csvreader.cpp)
target_link_libraries(csvreader ${catkin_LIBRARIES})
