import gradio as gr

# ==================================
# PET DATABASE
# ==================================

pets = [
    "dog",
    "cat",
    "rabbit",
    "hamster",
    "parrot"
]

# ==================================
# PART 1
# EDIT DISTANCE TABLE
# ==================================

def edit_distance(word1, word2):

    m = len(word1)
    n = len(word2)

    dp = [[0 for _ in range(n + 1)]
          for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[m][n]

# ==================================
# PART 2 & 3
# FIND CLOSEST PET
# ==================================

MAX_ALLOWED_DISTANCE = 2

def find_pet(search_word):

    search_word = search_word.lower().strip()

    best_pet = None
    best_distance = float("inf")

    for pet in pets:

        distance = edit_distance(
            search_word,
            pet
        )

        if distance < best_distance:
            best_distance = distance
            best_pet = pet

    if best_distance > MAX_ALLOWED_DISTANCE:
        return "no match", best_distance

    return best_pet, best_distance

# ==================================
# PART 4
# TESTING
# ==================================

test_cases = [
    ("dog", "dog"),
    ("dag", "dog"),
    ("cot", "cat"),
    ("rabit", "rabbit"),
    ("hamter", "hamster"),
    ("elephant", "no match")
]

def run_tests():

    mistakes = 0
    report = ""

    for query, expected in test_cases:

        prediction, distance = find_pet(query)

        if prediction != expected:
            mistakes += 1

        report += (
            f"Search: {query}\n"
            f"Predicted: {prediction}\n"
            f"Expected: {expected}\n"
            f"Distance: {distance}\n\n"
        )

    report += f"Mistakes: {mistakes}/{len(test_cases)}"

    return report

# ==================================
# GRADIO UI
# ==================================

def search_pet(query):

    match, distance = find_pet(query)

    return (
        f"Suggested Pet: {match}\n"
        f"Edit Distance: {distance}"
    )

with gr.Blocks(title="Pet Search") as demo:

    gr.Markdown("# Pet Search Using Edit Distance")

    search_box = gr.Textbox(
        label="Search Pet"
    )

    output_box = gr.Textbox(
        label="Result"
    )

    search_btn = gr.Button("Search")

    search_btn.click(
        fn=search_pet,
        inputs=search_box,
        outputs=output_box
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
        fn=run_tests,
        outputs=test_output
    )

demo.launch()