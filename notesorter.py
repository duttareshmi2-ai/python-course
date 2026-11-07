import gradio as gr
from collections import Counter
import math

# =====================
# PART 1: FINGERPRINTS
# =====================

def fingerprint(text):
    words = text.lower().split()
    return Counter(words)

# Training notes in boxes
boxes = {
    "sports": [
        "football team match goal",
        "basketball player score",
        "cricket tournament wicket"
    ],

    "science": [
        "physics experiment energy",
        "chemistry reaction lab",
        "biology research cells"
    ],

    "music": [
        "guitar concert song",
        "piano recital performance",
        "drums rhythm band"
    ]
}

# Create box fingerprints
box_fingerprints = {}

for box_name, notes in boxes.items():
    combined_text = " ".join(notes)
    box_fingerprints[box_name] = fingerprint(combined_text)

# =====================
# PART 2: COSINE SIMILARITY
# =====================

def cosine_similarity(fp1, fp2):
    words = set(fp1.keys()) | set(fp2.keys())

    dot_product = sum(
        fp1.get(word, 0) * fp2.get(word, 0)
        for word in words
    )

    magnitude1 = math.sqrt(
        sum(v * v for v in fp1.values())
    )

    magnitude2 = math.sqrt(
        sum(v * v for v in fp2.values())
    )

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product / (magnitude1 * magnitude2)

# =====================
# PART 3: BEST MATCH
# =====================

THRESHOLD = 0.20

def classify_note(note):
    note_fp = fingerprint(note)

    best_box = "unknown"
    best_score = 0

    for box_name, box_fp in box_fingerprints.items():

        score = cosine_similarity(
            note_fp,
            box_fp
        )

        if score > best_score:
            best_score = score
            best_box = box_name

    if best_score < THRESHOLD:
        best_box = "unknown"

    return best_box, round(best_score, 3)

# =====================
# PART 4: TEST NOTES
# =====================

test_notes = [
    ("football goal team", "sports"),
    ("basketball score player", "sports"),
    ("physics energy lab", "science"),
    ("chemistry reaction", "science"),
    ("guitar song concert", "music"),
    ("banana pizza random", "unknown")
]

def evaluate_system():
    mistakes = 0
    report = ""

    for note, actual in test_notes:

        predicted, score = classify_note(note)

        if predicted != actual:
            mistakes += 1

        report += (
            f"Note: {note}\n"
            f"Predicted: {predicted}\n"
            f"Actual: {actual}\n"
            f"Similarity: {score}\n\n"
        )

    report += f"\nTotal Mistakes: {mistakes}/6"

    return report

# =====================
# GRADIO FUNCTIONS
# =====================

def sort_note(note):
    category, score = classify_note(note)

    return (
        f"Best Box: {category}\n"
        f"Cosine Similarity: {score}"
    )

# =====================
# UI
# =====================

with gr.Blocks(title="Note Sorter") as demo:

    gr.Markdown("# Note Sorter")
    gr.Markdown("Classify a school notice into the most suitable box.")

    note_input = gr.Textbox(
        label="Enter Note"
    )

    result_output = gr.Textbox(
        label="Result"
    )

    classify_btn = gr.Button("Classify Note")

    classify_btn.click(
        sort_note,
        inputs=note_input,
        outputs=result_output
    )

    gr.Markdown("## Evaluation")

    evaluation_output = gr.Textbox(
        lines=20,
        label="Test Results"
    )

    evaluate_btn = gr.Button(
        "Run 6 Test Notes"
    )

    evaluate_btn.click(
        evaluate_system,
        outputs=evaluation_output
    )

demo.launch()