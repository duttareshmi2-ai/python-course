import gradio as gr
import re

# ==================================
# PART 1
# CLEAN WORDS
# ==================================

def clean_text(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words

# ==================================
# PART 2
# LEXICON + NEGATION
# ==================================

lexicon = {
    "good": 2,
    "great": 3,
    "happy": 2,
    "love": 3,
    "excellent": 3,
    "bad": -2,
    "terrible": -3,
    "sad": -2,
    "hate": -3,
    "awful": -3
}

def sentiment_score(comment):

    words = clean_text(comment)

    score = 0
    negate = False

    for word in words:

        if word == "not":
            negate = True
            continue

        value = lexicon.get(word, 0)

        if negate:
            value = -value
            negate = False

        score += value

    return score

# ==================================
# PART 3
# SCORE -> MOOD
# ==================================

def mood(comment):

    score = sentiment_score(comment)

    if score > 1:
        return "HAPPY", score

    elif score < -1:
        return "UNHAPPY", score

    else:
        return "OK", score

# ==================================
# PART 4
# TESTING
# ==================================

test_comments = [
    ("i love this", "HAPPY"),
    ("this is great", "HAPPY"),
    ("i hate this", "UNHAPPY"),
    ("this is terrible", "UNHAPPY"),
    ("not bad", "HAPPY"),
    ("book table chair", "OK")
]

def run_tests():

    mistakes = 0
    report = ""

    for comment, expected in test_comments:

        prediction, score = mood(comment)

        if prediction != expected:
            mistakes += 1

        report += (
            f"Comment: {comment}\n"
            f"Predicted: {prediction}\n"
            f"Expected: {expected}\n"
            f"Score: {score}\n\n"
        )

    report += f"Mistakes: {mistakes}/{len(test_comments)}"

    return report

# ==================================
# UI FUNCTION
# ==================================

def analyze(comment):

    result, score = mood(comment)

    return (
        f"Mood: {result}\n"
        f"Score: {score}"
    )

# ==================================
# GRADIO UI
# ==================================

with gr.Blocks(title="Comment Mood Analyzer") as demo:

    gr.Markdown("# Comment Mood Analyzer")

    comment_input = gr.Textbox(
        label="Enter Comment"
    )

    result_output = gr.Textbox(
        label="Result"
    )

    analyze_btn = gr.Button("Analyze")

    analyze_btn.click(
        analyze,
        inputs=comment_input,
        outputs=result_output
    )

    gr.Markdown("## Evaluation")

    test_output = gr.Textbox(
        label="Test Results",
        lines=20
    )

    test_btn = gr.Button(
        "Run 6 Tests"
    )

    test_btn.click(
        run_tests,
        outputs=test_output
    )

demo.launch()