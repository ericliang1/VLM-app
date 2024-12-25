import streamlit as st
from transformers import pipeline
from PIL import Image
import cv2


def run_app():
    #load VLM model
    pipe = pipeline("visual-question-answering", model="Salesforce/blip-vqa-base")

    #configure settings
    if "cap" not in st.session_state:
        st.session_state.cap = cv2.VideoCapture(0)

    st.title("VLM Demo")
    stframe = st.empty()
    question = st.text_input("Ask a question: ")

    if not st.session_state.cap.isOpened():
        st.error("Unable to access the webcam. Please refresh the app or check your webcam settings.")
    else:
        ret, frame = st.session_state.cap.read()
        if not ret:
            st.error("Failed to read from webcam. Please refresh the app.")
        else:
            while True:
                #capture video
                ret, frame = st.session_state.cap.read()

                if not ret:
                    st.error("Failed to access the webcam.")
                    break

                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                stframe.image(frame_rgb, channels="RGB", caption="Live Webcam Video", use_container_width=True)

                if question:
                    
                    #generate an answer
                    with st.spinner("Generating Response"):
                        pil_image = Image.fromarray(frame_rgb)

                        try:
                            result = pipe(image=pil_image, question=question)
                            if result:
                                answer = result[0]['answer']
                            else:
                                answer = "No answer could be generated. Try asking a different question."
                        except Exception as e:
                            answer = f"An error occurred: {e}"

                        #display answer to question
                        st.write(f"**Question:** {question}")
                        st.write(f"**Answer:** {answer}")
                        st.write("---")

                    question = "" 

    if st.session_state.cap.isOpened():
        st.session_state.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    run_app()
