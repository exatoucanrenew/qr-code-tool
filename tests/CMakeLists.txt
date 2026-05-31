add_executable(qr_scanner_test test_scanner.cpp)
target_link_libraries(qr_scanner_test PRIVATE gtest_main OpenCV::OpenCV ZXing::ZXing)
add_test(NAME qr_scanner_test COMMAND qr_scanner_test)