import gradio as gr
import joblib
import numpy as np

model = joblib.load("model.pkl")

def predict(sepal_length, sepal_width, petal_length, petal_width):
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    pred = model.predict(data)[0]
    return f"Predicted class: {pred}"

ui = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Sepal Length"),
        gr.Number(label="Sepal Width"),
        gr.Number(label="Petal Length"),
        gr.Number(label="Petal Width")
    ],
    outputs="text",
    title="Iris Classifier",
    description="Enter flower measurements to predict the Iris species."
)

if __name__ == "__main__":
    ui.launch(server_name="0.0.0.0", server_port=8000)