import gradio as gr

# ===================================
# PART 1: RECIPES
# ===================================

recipes = {
    "Pasta": "pasta cheese tomato garlic sauce",
    "Cake": "chocolate flour sugar butter vanilla",
    "Soup": "vegetable carrot potato onion broth",
    "Salad": "apple banana orange grapes fruit",
    "Curry": "chicken onion garlic spice curry"
}

# ===================================
# PART 1: BUILD INVERTED INDEX
# ===================================

index = {}

for recipe_name, text in recipes.items():

    words = text.lower().split()

    for word in words:

        if word not in index:
            index[word] = {}

        if recipe_name not in index[word]:
            index[word][recipe_name] = 0

        index[word][recipe_name] += 1

# ===================================
# PART 2: TF SCORING

# ===================================

def search_recipes(query):

    scores = {}
    words = query.lower().split()

    for word in words:

        if word in index:

            for recipe, count in index[word].items():

                if recipe not in scores:
                    scores[recipe] = 0

                scores[recipe] += count

    if len(words) > 0:
        for recipe in scores:
            scores[recipe] /= len(words)

    return scores

# ===================================
# PART 3: BEST RECIPE
# ===================================

def best_recipe(query):

    scores = search_recipes(query)

    if not scores:
        return "no match", 0

    best = max(scores, key=scores.get)

    return best, round(scores[best], 3)

# ===================================
# PART 4: TEST QUERIES
# ===================================

test_queries = [
    ("cheese tomato", "Pasta"),
    ("chocolate sugar", "Cake"),
    ("carrot potato", "Soup"),
    ("apple orange", "Salad"),
    ("chicken spice", "Curry"),
    ("pizza burger", "no match")
]

def evaluate_search():

    mistakes = 0
    report = ""

    for query, expected in test_queries:

        prediction, score = best_recipe(query)

        if prediction != expected:
            mistakes += 1

        report += (
            f"Query: {query}\n"
            f"Prediction: {prediction}\n"
            f"Expected: {expected}\n"
            f"Score: {score}\n\n"
        )

    report += f"\nTotal Mistakes: {mistakes}/6"

    return report

# ===================================
# SEARCH FUNCTION
# ===================================

def search_ui(query):

    prediction, score = best_recipe(query)

    if prediction == "no match":
        return "No Match Found"

    return (
        f"Best Recipe: {prediction}\n"
        f"Score: {score}\n\n"
        f"Recipe Words:\n{recipes[prediction]}"
    )

# ===================================
# GRADIO UI
# ===================================

with gr.Blocks(title="Recipe Box Search") as demo:

    gr.Markdown("# Recipe Box Search")
    gr.Markdown("Mini Search Engine using Inverted Index")

    query_input = gr.Textbox(
        label="Search Query"
    )

    result_output = gr.Textbox(
        label="Search Result",
        lines=6
    )

    search_btn = gr.Button("Search")

    search_btn.click(
        fn=search_ui,
        inputs=query_input,
        outputs=result_output
    )

    gr.Markdown("## Evaluation")

    test_output = gr.Textbox(
        label="6 Test Queries",
        lines=20
    )

    test_btn = gr.Button(
        "Run Test Queries"
    )

    test_btn.click(
        fn=evaluate_search,
        outputs=test_output
    )

demo.launch()