import qrcode
from qrcode.image.pil import PilImage
from pathlib import Path
from PIL import Image


class QRGenerator:
    """Generate QR codes with custom data and save as PNG images."""

    def __init__(self, box_size: int = 10, border: int = 4):
        self.box_size = box_size
        self.border = border

    def generate(self, data: str, output_path: str, fill_color: str = "black", back_color: str = "white") -> str:
        """Create a QR code image from data and save to output_path. Returns the path."""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=self.box_size,
            border=self.border,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img: Image.Image = qr.make_image(
            fill_color=fill_color,
            back_color=back_color,
            image_factory=PilImage,
        )
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        img.save(str(path))
        return str(path)