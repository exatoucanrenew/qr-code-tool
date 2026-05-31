#include <gtest/gtest.h>
#include <opencv2/opencv.hpp>
#include "../src/scanner.cpp"

TEST(QRScannerTest, DecodesValidQR) {
    cv::Mat qrImage = cv::imread("test_qr.png", cv::IMREAD_GRAYSCALE);
    ASSERT_FALSE(qrImage.empty());

    auto result = ZXing::ReadBarcode(
        {qrImage.data, qrImage.cols, qrImage.rows, ZXing::ImageFormat::Lum},
        ZXing::DecodeHints().setFormats(ZXing::BarcodeFormat::QRCode)
    );

    EXPECT_TRUE(result.isValid());
    EXPECT_EQ(result.text(), "test123");
}

TEST(QRScannerTest, FailsOnInvalidImage) {
    cv::Mat emptyImage;
    auto result = ZXing::ReadBarcode(
        {emptyImage.data, emptyImage.cols, emptyImage.rows, ZXing::ImageFormat::Lum},
        ZXing::DecodeHints().setFormats(ZXing::BarcodeFormat::QRCode)
    );

    EXPECT_FALSE(result.isValid());
}