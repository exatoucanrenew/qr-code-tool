import tempfile
from pathlib import Path
from src import QRGenerator, QRScanner


def test_generate_and_scan():
    gen = QRGenerator(box_size=8, border=2)
    scanner = QRScanner()

    test_data = "Hello QR World! 123"

    with tempfile.TemporaryDirectory() as tmpdir:
        img_path = str(Path(tmpdir) / "test_qr.png")
        gen.generate(test_data, img_path)

        results = scanner.scan_file(img_path)
        assert len(results) == 1
        assert results[0] == test_data


def test_generate_multiple():
    gen = QRGenerator()
    scanner = QRScanner()

    with tempfile.TemporaryDirectory() as tmpdir:
        data1 = "First"
        data2 = "Second"
        p1 = str(Path(tmpdir) / "a.png")
        p2 = str(Path(tmpdir) / "b.png")
        gen.generate(data1, p1)
        gen.generate(data2, p2)

        assert scanner.scan_file(p1) == [data1]
        assert scanner.scan_file(p2) == [data2]


def test_scan_empty_image():
    scanner = QRScanner()
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a plain white image with no QR
        from PIL import Image
        img = Image.new("RGB", (100, 100), "white")
        path = str(Path(tmpdir) / "blank.png")
        img.save(path)

        results = scanner.scan_file(path)
        assert results == []


def test_generator_custom_colors():
    gen = QRGenerator()
    with tempfile.TemporaryDirectory() as tmpdir:
        path = str(Path(tmpdir) / "color_qr.png")
        gen.generate("colors", path, fill_color="red", back_color="yellow")
        from pathlib import Path
        assert Path(path).exists()