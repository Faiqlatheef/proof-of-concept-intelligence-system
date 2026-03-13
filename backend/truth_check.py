import requests

BASE_URL = "http://127.0.0.1:8000"

TEST_CASES = [
    {
        "question": "What were my LDL levels for the last 3 years?",
        "valid_outcomes": ["LDL", "I don't know"]
    },
    {
        "question": "What was my LDL level in 2022?",
        "valid_outcomes": ["mg", "I don't know"]
    },
    {
        "question": "What was my blood sugar in 2010?",
        "valid_outcomes": ["I don't know"]
    }
]

def run():
    for t in TEST_CASES:
        response = requests.post(
            f"{BASE_URL}/query",
            json={"question": t["question"]},
            timeout=30
        )

        assert response.status_code == 200, (
            f"API ERROR {response.status_code}: {response.text}"
        )

        data = response.json()
        answer = data.get("answer", "")

        assert any(v in answer for v in t["valid_outcomes"]), (
            f"FAILED\nQuestion: {t['question']}\nAnswer: {answer}"
        )

        print(f"PASS: {t['question']}")

    print("\n✅ All grounding tests passed")

if __name__ == "__main__":
    run()
