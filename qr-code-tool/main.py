import sys
from src import QRGenerator, QRScanner


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  Generate: python main.py generate <data> [output.png]")
        print("  Scan:     python main.py scan <image.png>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "generate":
        data = sys.argv[2]
        output = sys.argv[3] if len(sys.argv) > 3 else "output.png"
        gen = QRGenerator()
        path = gen.generate(data, output)
        print(f"QR code saved to: {path}")

    elif command == "scan":
        image_path = sys.argv[2]
        scanner = QRScanner()
        results = scanner.scan_file(image_path)
        if results:
            for r in results:
                print(f"Decoded: {r}")
        else:
            print("No QR code found.")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()