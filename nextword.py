import gradio as gr
from collections import defaultdict

# ==================================
# TRAINING TEXT
# ==================================

text = """
the cat sat on the mat
the cat ate fish
the dog sat on the rug
the dog ate food
the bird sat on the tree
the bird ate seeds
"""

# ==================================
# PART 1
# COUNT WHICH WORD FOLLOWS WHICH
# (BIGRAMS)
# ==================================

bigrams = defaultdict(lambda: defaultdict(int))

words = text.lower().split()

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    bigrams[current_word][next_word] += 1

# ==================================
# PART 2
# COUNTS -> PROBABILITIES
# ==================================

probabilities = {}

for word, followers in bigrams.items():

    total = sum(followers.values())

    probabilities[word] = {}

    for next_word, count in followers.items():
        probabilities[word][next_word] = count / total

# ==================================
# PART 3
# PREDICT NEXT WORD
# TOP SUGGESTION + BACKOFF
# ==================================

def predict_next(word):

    word = word.lower().strip()

    if word not in probabilities:
        return "the"

    followers = probabilities[word]

    prediction = max(
        followers,
        key=followers.get
    )

    return prediction

# ==================================
# PART 4
# TEST 6 WORDS
# ==================================

test_cases = [
    ("cat", "sat"),
    ("dog", "sat"),
    ("bird", "sat"),
    ("sat", "on"),
    ("ate", "fish"),
    ("unknown", "the")
]

def evaluate():

    mistakes = 0
    report = ""

    for word, expected in test_cases:

        predicted = predict_next(word)

        if predicted != expected:
            mistakes += 1

        report += (
            f"Word: {word}\n"
            f"Predicted: {predicted}\n"
            f"Expected: {expected}\n\n"
        )

    report += f"Mistakes: {mistakes}/{len(test_cases)}"

    return report

# ==================================
# GRADIO FUNCTIONS
# ==================================

def predict_ui(word):
    return predict_next(word)

# ==================================
# UI
# ==================================

with gr.Blocks(title="Bigram Word Predictor") as demo:

    gr.Markdown("# Bigram Next Word Predictor")

    word_input = gr.Textbox(
        label="Enter a Word"
    )

    output = gr.Textbox(
        label="Predicted Next Word"
    )

    predict_btn = gr.Button("Predict")

    predict_btn.click(
        fn=predict_ui,
        inputs=word_input,
        outputs=output
    )

    gr.Markdown("## Evaluation")

    test_output = gr.Textbox(
        label="Test Results",
        lines=15
    )

    eval_btn = gr.Button(
        "Run 6 Tests"
    )

    eval_btn.click(
        fn=evaluate,
        outputs=test_output
    )

demo.launch()