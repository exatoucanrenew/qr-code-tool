cmake_minimum_required(VERSION 3.10)
project(qr-code-tool)

set(CMAKE_CXX_STANDARD 17)

find_package(OpenCV REQUIRED)
find_package(ZXing REQUIRED)

add_executable(qr-generator src/generator.cpp)
target_link_libraries(qr-generator PRIVATE OpenCV::OpenCV ZXing::ZXing)

add_executable(qr-scanner src/scanner.cpp)
target_link_libraries(qr-scanner PRIVATE OpenCV::OpenCV ZXing::ZXing)

enable_testing()
add_subdirectory(tests)