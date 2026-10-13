import streamlit as st
import time

from styles import load_css
from utils import predict_comment
from components import (
    prediction_card,
    confidence_bars,
    score_chart,
    show_history,
    download_json,
    footer
)

st.set_page_config(
    page_title="MR.TJ's AI Toxic Comment Detector",
    page_icon="🛡",
    layout="wide"
)

st.markdown(load_css(), unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:

    st.title("🛡 AI Moderator")

    st.markdown("---")

    st.markdown("### Model")

    st.success("DistilBERT")

    st.markdown("### Backend")

    st.info("FastAPI")

    st.markdown("### Labels")

    st.write("✔ Toxic")
    st.write("✔ Severe Toxic")
    st.write("✔ Obscene")
    st.write("✔ Threat")
    st.write("✔ Insult")
    st.write("✔ Identity Hate")

    st.markdown("---")

    st.markdown("### Example Comments")

    examples = {
        "😊 Positive":
            "Have a wonderful day!",

        "😡 Toxic":
            "You are an idiot.",

        "🚨 Threat":
            "I will kill you.",

        "💀 Hate":
            "People like you should disappear."
    }

    for key, value in examples.items():

        if st.button(key):

            st.session_state["example"] = value

st.markdown(
    """
    <div class='main-title'>
        🛡 MR.TJ's AI Toxic Comment Detection
    </div>

    <div class='sub-title'>
        DistilBERT + FastAPI + Streamlit
    </div>
    """,
    unsafe_allow_html=True
)


default_text = st.session_state.get("example", "")

text = st.text_area(
    "Enter Comment",
    value=default_text,
    height=180
)

col1, col2 = st.columns(2)

predict = col1.button("🔍 Analyze Comment")

clear = col2.button("🗑 Clear")

if clear:

    st.session_state["example"] = ""

    st.rerun()

if predict:

    if text.strip() == "":

        st.warning("Please enter a comment.")

    else:

        start = time.time()

        with st.spinner("Analyzing Comment..."):

            result, error = predict_comment(text)

        end = time.time()

        if error:

            st.error(error)

        else:

            st.session_state.history.append({
                "text": text,
                "prediction": result["primary_category"]
            })

            st.success("Prediction Completed")

            prediction_card(
                result["primary_category"],
                result["risk_level"]
            )

            st.metric(
                "Response Time",
                f"{end-start:.2f} sec"
            )

            confidence_bars(
                result["all_scores"]
            )

            score_chart(
                result["all_scores"]
            )

            with st.expander("Detected Labels"):

                st.json(
                    result["detected_labels"]
                )

            with st.expander("Complete JSON"):

                st.json(result)

            download_json(result)

show_history()

footer()