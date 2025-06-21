# 🔍 Real-Time Object Detection with YOLOv8

This project is a real-time object detection system using the YOLOv8 model from Ultralytics. It allows users to detect and classify multiple objects in images, videos, or live webcam streams with high accuracy and speed through a user-friendly web interface built with Streamlit.

![YOLOv8 Detection Demo](images/sample_detection.png)

---

## 🚀 Features

- 🔎 Detects multiple objects in real-time
- 🎥 Supports live webcam feed and file uploads (images/videos)
- 📦 Selectable YOLOv8 model sizes: `yolov8n`, `yolov8s`, `yolov8m`, `yolov8l`, `yolov8x`
- 🧠 Uses pretrained COCO weights (80+ object classes)
- 🌐 Web-based UI using **Streamlit** (or optionally Gradio)

---

## 🛠️ Tech Stack

- Python
- OpenCV
- [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- Streamlit / Gradio
- NumPy

---

## 📦 Installation

1. **Clone the repository**  
   git clone https://github.com/yourusername/yolov8-object-detection.git
   cd yolov8-object-detection
   
2. Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt
▶️ Usage
Run the app using Streamlit:

streamlit run app.py
Then open the link that appears in your terminal (usually http://localhost:8501).

📂 File Structure
yolov8-object-detection/
│
├── app.py                  # Streamlit application
├── yolov8_model/           # YOLOv8 loading and inference logic
├── images/                 # Example input/output images
├── requirements.txt        # Python dependencies
└── README.md               # Project description and setup
🖼️ Example Output

💡 Use Cases
🛡️ Security & Surveillance

📦 Inventory & Object Counting

🚗 Traffic & Vehicle Monitoring

🤖 Robotics & Smart Systems

🙌 Acknowledgements
Ultralytics YOLOv8
Streamlit
OpenCV

📬 Contact
For questions or suggestions, feel free to reach out via GitHub Issues or contact me at mukulsinghbbsr@gmail.com.

---
