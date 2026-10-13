import streamlit as st
import plotly.express as px
import pandas as pd


# -----------------------------
# Prediction Card
# -----------------------------
def prediction_card(category, risk):

    st.markdown(
        f"""
        <div class="card">
            <div class="prediction">
                🛡 Primary Category<br>
                <span style="color:#38bdf8">{category}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if risk == "High":
        css = "high"
        emoji = "🔴"

    elif risk == "Medium":
        css = "medium"
        emoji = "🟡"

    else:
        css = "low"
        emoji = "🟢"

    st.markdown(
        f"""
        <div class="{css}">
            {emoji} Risk Level : {risk}
        </div>
        """,
        unsafe_allow_html=True,
    )


# -----------------------------
# Progress Bars
# -----------------------------
def confidence_bars(scores):

    st.subheader("📊 Confidence Scores")

    for label, score in scores.items():

        st.write(f"**{label.replace('_',' ').title()}**")

        st.progress(min(score / 100, 1.0))

        st.caption(f"{score:.2f}%")



# -----------------------------
# Plotly Chart
# -----------------------------
def score_chart(scores):

    df = pd.DataFrame({
        "Category": list(scores.keys()),
        "Confidence": list(scores.values())
    })

    fig = px.bar(
        df,
        x="Category",
        y="Confidence",
        text="Confidence",
        title="Toxicity Distribution"
    )

    fig.update_layout(
        height=450,
        template="plotly_dark",
        xaxis_title="",
        yaxis_title="Confidence (%)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# -----------------------------
# History
# -----------------------------
def show_history():

    st.subheader("🕒 Prediction History")

    if "history" not in st.session_state:
        st.session_state.history = []

    if len(st.session_state.history) == 0:

        st.info("No predictions yet.")

    else:

        for item in reversed(st.session_state.history[-10:]):

            st.markdown(
                f"""
                **Comment**

                {item['text']}

                **Prediction**

                {item['prediction']}

                ---
                """
            )


# -----------------------------
# Download JSON
# -----------------------------
def download_json(result):

    st.download_button(
        label="⬇ Download JSON",
        data=str(result),
        file_name="prediction.json",
        mime="application/json"
    )


# -----------------------------
# Footer
# -----------------------------
def footer():

    st.markdown(
        """
        <div class="footer">

        Built with ❤️ using

        FastAPI • DistilBERT • Streamlit

        </div>
        """,
        unsafe_allow_html=True
    )