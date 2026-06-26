#Sample Python Project
#Kevin Gonzalez - June 2025

import random
from datetime import datetime

# Simulated messages and responses
simulated_messages = [
    "Hey, are you available to help with this ticket?",
    "Can you review my PR when you get a chance?",
    "Are we still on for the 3 PM meeting?",
    "I think the server went down again.",
    "Do you have access to the shared folder?"
]

response_templates = [
    "Sure, give me a sec!",
    "Can't right now, sorry.",
    "Let me check and get back to you.",
    "I'll look into it ASAP.",
    "Yes, I'm on it.",
    "Not sure, checking now.",
    "Let's circle back in a few minutes."
]

def simulate_response_round():
    incoming = random.choice(simulated_messages)
    suggestions = random.sample(response_templates, 3)

    print("\n📥 Incoming message:\n", incoming)
    print("\n💬 Suggested replies:")
    for i, reply in enumerate(suggestions, 1):
        print(f"[{i}] {reply}")

    while True:
        choice = input("\nChoose a response (1-3): ")
        if choice in {"1", "2", "3"}:
            selected = suggestions[int(choice) - 1]
            break
        print("Invalid choice. Try again.")

    log_entry = f"{datetime.now()} | INCOMING: {incoming} | RESPONSE: {selected}\n"
    with open("response_log.txt", "a") as f:
        f.write(log_entry)

    print("\n✅ Response sent and logged!")

# Run the simulator
if __name__ == "__main__":
    simulate_response_round()
