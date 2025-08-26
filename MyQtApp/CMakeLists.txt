cmake_minimum_required(VERSION 3.5)

project(MyQtApp)
set(CMAKE_CXX_STANDARD 17)

# Update this path to match your Qt installation
set(CMAKE_PREFIX_PATH "C:/Qt/6.9.1/mingw_64")

find_package(Qt6 REQUIRED COMPONENTS Widgets)

add_executable(MyQtApp main.cpp)
target_link_libraries(MyQtApp Qt6::Widgets)
