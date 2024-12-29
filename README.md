   # VLM app

**VLM** is a streaming visual question-answering app using the BLIP vision language model from Hugging Face. 

---

## Features

- Asking questions in webcam video

---

## Requirements

Before using the project, ensure you have the following:

- Streamlit
- Transformers
- Torch
- OpenCV
- Pillow
- Flask

Install required libraries with:

```bash
   pip install -r requirements.txt
   ```

---

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ericliang1/VLM-app.git
   cd VLM-app
   ```
---

## Usage

### Run the Project Locally

To ask questions in webcam video:

1. In app.py change cv2.VideoCapture("http://host.docker.internal:5000/video") to cv2.VideoCapture(0)

2. Run app.py in terminal using:
   
```bash
streamlit run app.py
```

3. Go to http://localhost:8501/ on web browser

4. Ask questions in textbox under webcam video

---
### Run the Project in Docker

To ask questions in webcam video:

1. Build a docker image in terminal using:

```bash
docker build -t vlm_app .
```

2. Run camera_app.py in terminal using:
   
```bash
python camera_app.py
```

3. Run docker image in terminal using:

```bash
docker run -p 8501:8501 vlm_app
```

4. Go to http://localhost:8501/ on web browser

5. Ask questions in textbox under webcam video

---
