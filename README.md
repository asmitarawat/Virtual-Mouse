## Vision-Based Virtual Mouse
### Real-Time Hand Gesture Recognition System

A computer vision and real-time inference project that uses hand landmark data to model user intent and translate it into system-level actions.
This project demonstrates end-to-end data flow — from raw visual input → feature extraction → rule-based inference → automated control.

Designed to showcase skills relevant to an Associate Data Scientist role, including data preprocessing, feature engineering, real-time prediction, and decision logic.

#### Problem Statement

Traditional input devices (mouse, touchpad) require physical interaction and may not be accessible or efficient in all environments.

Goal:
Build a vision-driven interaction system that interprets human hand movements as structured data and uses it to predict user actions in real time.

#### Solution Overview

The system:

Captures live video data via webcam

Extracts 21 key hand landmarks per frame

Converts visual signals into numerical features

Applies distance-based and positional logic to infer intent

Executes system actions (cursor movement, clicks) based on predictions

This pipeline closely resembles real-time ML inference systems, replacing trained models with interpretable decision rules.

#### Key Data Science Concepts Demonstrated

Real-time data ingestion

Feature extraction from unstructured data (images → coordinates)

Geometric feature engineering (distance, relative position)

Threshold-based classification

Noise handling using state flags

Mapping prediction outputs to real-world actions

#### Tech Stack

Python

OpenCV – image acquisition & preprocessing

MediaPipe – hand landmark detection (21-point skeleton)

PyAutoGUI – system automation

Mathematical modeling – Euclidean distance & spatial logic

#### Data Pipeline
Webcam Frames
   ↓
Hand Landmark Detection
   ↓
Coordinate Normalization
   ↓
Feature Engineering
   ↓
Gesture Classification (Rule-Based)
   ↓
System Action Execution
#### Gesture Classification Logic
Feature Condition	Predicted Action
Index finger movement	Cursor movement
Thumb–index distance < threshold	Left click
Thumb position right of index finger	Right click
No valid gesture	No action

The use of state variables prevents duplicate predictions and stabilizes outputs across frames.

#### Project Structure
Virtual-Mouse/
│
├── VIRTUALMOUSE.py        # Core inference and control logic
├── README.md              # Project documentation
#### Setup Instructions
Install Dependencies
pip install opencv-python mediapipe pyautogui
Run the Application
python VIRTUALMOUSE.py

Press Q to terminate execution.

#### Results & Observations

Low-latency inference suitable for real-time interaction

Robust tracking under moderate lighting variations

Consistent gesture classification using geometric thresholds

Stable performance using single-hand constraint

#### Future Improvements (Data Science Focused)

Replace rule-based logic with ML classifiers (SVM / Random Forest)

Temporal modeling using frame sequences (LSTM / HMM)

Gesture confidence scoring

Adaptive threshold learning

Dataset creation for supervised training

Performance evaluation metrics (precision, recall)

#### Relevance to Associate Data Scientist Role

This project demonstrates:

Translating raw data into actionable insights

Real-time inference under system constraints

Feature engineering from noisy inputs

Practical application of mathematical modeling

Building interpretable decision systems

#### Author

Asmita Rawat
B.Tech Computer Science Engineering
Aspiring Associate Data Scientist
