#include <opencv2/opencv.hpp>
#include <ZXing/BarcodeFormat.h>
#include <ZXing/WriteBarcode.h>
#include <ZXing/BitMatrix.h>
#include <iostream>

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <text>\n";
        return 1;
    }

    std::string text = argv[1];
    auto writer = ZXing::MultiFormatWriter(ZXing::BarcodeFormat::QRCode);
    auto matrix = writer.encode(text, 300, 300);

    cv::Mat qrImage(matrix.height(), matrix.width(), CV_8UC1);
    for (int y = 0; y < matrix.height(); ++y) {
        for (int x = 0; x < matrix.width(); ++x) {
            qrImage.at<uchar>(y, x) = matrix.get(x, y) ? 0 : 255;
        }
    }

    cv::imwrite("qr_code.png", qrImage);
    std::cout << "QR code saved to qr_code.png\n";
    return 0;
}