import cv2
from pyzbar.pyzbar import decode
from pathlib import Path


class QRScanner:
    """Scan QR codes from image files using OpenCV and pyzbar."""

    def scan_file(self, image_path: str) -> list[str]:
        """Decode QR codes from a static image. Returns list of decoded data strings."""
        path = Path(image_path)
        if not path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")

        img = cv2.imread(str(path))
        if img is None:
            raise ValueError(f"Could not read image: {image_path}")

        barcodes = decode(img)
        results = []
        for barcode in barcodes:
            data = barcode.data.decode("utf-8")
            results.append(data)
        return results

    def scan_camera(self, camera_id: int = 0, timeout_seconds: int = 10) -> str | None:
        """Scan QR code from live camera feed. Returns first decoded string or None."""
        cap = cv2.VideoCapture(camera_id)
        if not cap.isOpened():
            raise RuntimeError("Could not open camera.")

        start_time = cv2.getTickCount()
        result = None

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            barcodes = decode(frame)
            for barcode in barcodes:
                result = barcode.data.decode("utf-8")
                break

            if result is not None:
                break

            elapsed = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
            if elapsed > timeout_seconds:
                break

        cap.release()
        cv2.destroyAllWindows()
        return result