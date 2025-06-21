import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import time

st.title("🔴 Real-Time Object Detection with YOLOv8")

# Model selection
model_size = st.selectbox("Choose YOLOv8 model size", ["yolov8n.pt", "yolov8s.pt", "yolov8m.pt"], index=0)
model = YOLO(model_size)

# Confidence threshold slider
conf_threshold = st.slider("Confidence threshold", 0.0, 1.0, 0.25, 0.05)

# Toggle bounding boxes & labels
show_labels = st.checkbox("Show bounding boxes and labels", True)

# Upload image option
uploaded_file = st.file_uploader("Upload an image for detection", type=["jpg", "jpeg", "png"])

# Placeholder for output
image_placeholder = st.empty()

# FPS display
fps_placeholder = st.empty()

def process_frame(frame):
    results = model(frame, conf=conf_threshold)[0]
    annotated_frame = frame.copy()

    if show_labels:
        annotated_frame = results.plot()

    return annotated_frame, results

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    annotated_img, res = process_frame(img)
    annotated_img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
    image_placeholder.image(annotated_img, caption="Detection Result", use_column_width=True)
    classes = [model.names[int(cls)] for cls in res.boxes.cls]
    st.write("Detected classes:", classes)

elif st.button("Start Webcam Detection"):
    cap = cv2.VideoCapture(0)
    run = True
    prev_time = 0

    stop_button = st.button("Stop Webcam Detection")

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame")
            break

        annotated_frame, res = process_frame(frame)
        annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        image_placeholder.image(annotated_frame)

        # Calculate and display FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time else 0
        prev_time = curr_time
        fps_placeholder.text(f"FPS: {fps:.2f}")

        # Check for stop button press
        if stop_button:
            run = False
            break

    cap.release()
    cv2.destroyAllWindows()
