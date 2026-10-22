messages = [
    "URGENT: customer complaint about burnt bread",
    "Normal: request for cake recipe",
    "URGENT: refund needed for wrong delivery",
    "Normal: feedback about croissant taste",
    "Normal: inquiry about opening hours",
]

urgent_keywords = ["urgent", "refund", "complaint", "error", "wrong", "issue"]

def score_message(msg):
    msg_lower = msg.lower()
    score = sum(word in msg_lower for word in urgent_keywords)
    return score

urgent_msgs = []
normal_msgs = []

for msg in messages:
    if score_message(msg) > 0:
        urgent_msgs.append(msg)
    else:
        normal_msgs.append(msg)

print("=== URGENT MESSAGES ===")
for m in urgent_msgs:
    print("-", m)

print("\n=== NORMAL MESSAGES ===")
for m in normal_msgs:
    print("-", m)

# Simple accuracy test
expected_urgent = 2
mistakes = abs(len(urgent_msgs) - expected_urgent)
print(f"\nSorter mistakes: {mistakes}")
