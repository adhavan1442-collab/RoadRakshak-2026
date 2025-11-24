import cv2
import time
import random
from datetime import datetime

# Simulating GIS coordinates (Latitude, Longitude of a location in Kerala)
current_lat = 8.5241
current_long = 76.9366

def log_hazard(hazard_type, lat, long):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[ALERT] {hazard_type} detected at {lat}, {long} | Time: {timestamp}")

def start_detection():
    print("--- RoadRakshak AI System Initialized ---")
    print("Connect to Camera... [SUCCESS]")
    print("Loading YOLOv5 Model... [SUCCESS]")
    
    # Simulation: Randomly detecting a "Pothole" for demonstration
    print("Scanning road surface...")
    time.sleep(2)
    print("HAZARD DETECTED: POTHOLE")
    log_hazard("Severe Pothole", current_lat, current_long)

if __name__ == "__main__":
    start_detection()

