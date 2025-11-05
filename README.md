# 📡 RFID / NFC Card Reader

A lightweight and elegant **RFID / NFC HID Reader GUI** built with Python and Tkinter.  
It listens to **keyboard-emulated RFID or NFC readers** and displays both **Decimal (DEC)** and **Hexadecimal (HEX)** card IDs in real time.

## ✨ Features

- 🧠 Automatically detects keyboard input from RFID / NFC HID readers
- 💾 Displays scanned tag ID in both **Decimal** and **Hexadecimal** formats
- 🧹 Auto-clears invalid or noisy inputs
- 🎨 Modern minimalist UI (SF Pro fonts, soft edges, clean layout)
- ⚡ Real-time decoding and GUI update
- 💡 Built-in tip to avoid layout errors (supports English US keyboard layout)

## 🖥️ Requirements

| Component  | Description                                           |
| ---------- | ----------------------------------------------------- |
| **Python** | ≥ 3.8                                                 |
| **OS**     | Windows / macOS / Linux                               |
| **Input**  | RFID / NFC Reader emulating keyboard input (HID mode) |

## 📦 Installation

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/yourusername/rfid-nfc-reader.git
   cd rfid-nfc-reader
   ```
2. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .venv\Scripts\activate         # Windows
   ```
3. Install required packages:

   ```bash
   pip install keyboard
   ```

4. Scan Card:  
   The interface will display:

   <img width="462" height="327" alt="image" src="https://github.com/user-attachments/assets/6218d827-a39f-4c72-a849-e7bcf544ec97" />

   ```bash
   DEC: 0004098643
   HEX: 3E8A53
   ```
