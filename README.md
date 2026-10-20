# Hand Gesture Recognition

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

A real-time webcam application that recognizes hand poses using MediaPipe and TensorFlow Lite. Most of the hand-tracking and classifier implementation is from [Kazuhito00's hand-gesture-recognition-using-mediapipe](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe). This fork adds the **Rock n roll** gesture and includes custom gesture-sequence action handling.
![Uploading image.png…]()


## Features

- Detects up to two hands and displays their landmarks and recognized pose.
- The included model labels are **Thumbs up**, **Peace sign**, **Rock n roll**, **Open**, **Closed**, **Pointer**, and **Finger gun**. **Rock n roll** is the gesture added in this project.
- Includes TensorFlow Lite models for hand-pose and point-history classification, plus an on-screen fingertip trail intended for pointer-based air drawing.
- Provides notebooks and CSV datasets for exploring classifier training.
- Lets you customize gesture-to-action behavior in [`input.py`](input.py).

## Get started

### Requirements

- Python 3.10 is recommended for compatibility with the included TensorFlow Lite-based classifiers.
- A working webcam.
- MediaPipe, OpenCV, NumPy, and TensorFlow.

The pre-trained classifier models and gesture labels are included in [`model/`](model/), so you do not need to train the models to run the demo.

### Install

Create and activate a virtual environment from the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux, activate it with:

```bash
source .venv/bin/activate
```

Install the runtime dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install mediapipe opencv-python numpy tensorflow
```

On Windows, use a Python/TensorFlow combination with a native Windows TensorFlow wheel; Python 3.10 with TensorFlow 2.10 is a compatible option:

```powershell
python -m pip install "tensorflow==2.10.*"
```

### Run

Start the webcam application from the project root so that its model and label paths resolve correctly:

```bash
python app.py
```

The default camera device is `0`. Choose another camera or adjust capture dimensions with:

```bash
python app.py --device 1 --width 1280 --height 720
```

Press **Esc** in the application window to exit. The script also supports keyboard controls for collecting training samples: **k** selects keypoint collection, **h** selects point-history collection, and **0–9** selects the sample class. The data is appended to the corresponding CSV under `model/`.

## Customize gestures and actions

Gesture names are stored in [`model/keypoint_classifier/keypoint_classifier_label.csv`](model/keypoint_classifier/keypoint_classifier_label.csv). The app passes each recognized pose and handedness to [`input.py`](input.py), where you can define gesture sequences and their actions.

The app also contains point-history logic that is intended to show a short fingertip trail while pointing, like a basic air-drawing trace in the camera preview. In the current code, that trail is gated by a check for the string `"Off"`, but the classifier returns an integer and the current label is `"Pointer"`. As a result, the pointer trail is not activated unless this check is updated in `app.py`.

The checked-in action examples in `input.py` use macOS AppleScript (sleep and Spotify), and their sample sequence includes an `OK` label that is not in the current gesture list. They do not launch Telegram. Update the sequences and commands for your setup if you want different actions. Review any action before running it, since it can control applications or the operating system.

For model and dataset experiments, see the [keypoint classification notebook](keypoint_classification_EN.ipynb), [keypoint dataset](model/keypoint_classifier/keypoint.csv), and [point-history classification notebook](point_history_classification.ipynb).

## Help and documentation

- Open an issue in the repository's issue tracker for bug reports or usage questions.
- See the [upstream project](https://github.com/Kazuhito00/hand-gesture-recognition-using-mediapipe) for details about the original MediaPipe hand-tracking approach.
- Refer to the notebooks linked above for classifier data and training workflows.

## Maintainers and contributions

This is a personal extension of Kazuhito00's project, with most of the underlying implementation retained from upstream and the **Rock n roll** gesture added here. No separate maintainer contact is listed in this repository. Contributions are welcome: open an issue to discuss a substantial change, then submit a focused pull request. Include the affected gesture labels or action mappings in your description, and update the related notebooks or documentation when relevant. There is no separate contribution guide at present.

## License

Distributed under the [Apache License 2.0](LICENSE). The hand-tracking and classifier foundation is based on the upstream project linked above.
