import requests

API_URL = "http://127.0.0.1:8000/predict"


def predict_comment(text: str):
    try:
        response = requests.post(
            API_URL,
            json={"text": text},
            timeout=20
        )

        response.raise_for_status()

        return response.json(), None

    except requests.exceptions.ConnectionError:
        return None, "❌ Could not connect to FastAPI server."

    except requests.exceptions.Timeout:
        return None, "⏳ Request timed out."

    except Exception as e:
        return None, str(e)