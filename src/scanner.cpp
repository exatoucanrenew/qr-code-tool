#include <opencv2/opencv.hpp>
#include <ZXing/ReadBarcode.h>
#include <iostream>

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <image_path>\n";
        return 1;
    }

    cv::Mat image = cv::imread(argv[1], cv::IMREAD_GRAYSCALE);
    if (image.empty()) {
        std::cerr << "Could not open image\n";
        return 1;
    }

    auto result = ZXing::ReadBarcode(
        {image.data, image.cols, image.rows, ZXing::ImageFormat::Lum},
        ZXing::DecodeHints().setFormats(ZXing::BarcodeFormat::QRCode)
    );

    if (result.isValid()) {
        std::cout << "Decoded text: " << result.text() << "\n";
    } else {
        std::cout << "No QR code found\n";
    }

    return 0;
}