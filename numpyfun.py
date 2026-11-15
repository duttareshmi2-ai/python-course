import numpy as np

def confidence_explorer(objectness, class_scores):
    print("🚀 Scoring every prediction...")

    # Part 1: objectness × class score
    scores = objectness[:, np.newaxis] * class_scores

    print("🎯 Finding each prediction's favorite class...")

    # Part 2: best class and confidence
    best_class = np.argmax(scores, axis=1)
    best_score = np.max(scores, axis=1)

    print("\nTop predictions:")
    for i in range(len(best_class)):
        print(
            f"Prediction {i:2d}: "
            f"Class {best_class[i]} "
            f"(confidence = {best_score[i]:.4f})"
        )

    print("\n🔍 Testing confidence thresholds...")

    # Part 4: try three thresholds
    for threshold in [0.30, 0.50, 0.70]:
        keep = best_score >= threshold

        print(
            f"Threshold {threshold:.2f}: "
            f"{np.sum(keep)} predictions kept"
        )

    return scores, best_class, best_score


# Example usage
objectness = np.array([0.9, 0.6, 0.8])

class_scores = np.array([
    [0.1, 0.8, 0.2],
    [0.7, 0.2, 0.1],
    [0.3, 0.4, 0.9]
])

confidence_explorer(objectness, class_scores)