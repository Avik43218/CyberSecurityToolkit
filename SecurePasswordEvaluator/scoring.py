import common_patterns
import string
import math
import re

def calculate_entropy(passwd):
    
    charset = 0
    if any(c.isdigit() for c in passwd): charset += 10
    if any(c.islower() for c in passwd): charset += 26
    if any(c.isupper() for c in passwd): charset += 26
    if any(c in string.punctuation for c in passwd): charset += len(string.punctuation)

    return len(passwd) * math.log2(charset)

def brute_force(entropy, guesses=1e6):

    total_guesses = 2 ** entropy
    return total_guesses / guesses

    
def detect_patterns(passwd):

    issues = []

    if len(passwd) < 8:
        issues.append(("Too Short", 1))
    if re.search(r'(.)\1{2,}', passwd):
        issues.append(("Repeated Characters", 0.5))
    if re.search(common_patterns.sequential_chars, passwd):
        issues.append(("Sequential Characters", 0.5))
    if any(word in passwd.lower() for word in common_patterns.common_words):
        issues.append(("Common Words", 1))
    if any(kp in passwd.lower() for kp in common_patterns.keyboard_patterns):
        issues.append(("Keyboard Patterns", 0.5))

    return issues

def categorize_passwd(passwd):

    entropy = calculate_entropy(passwd)
    estd_time = brute_force(entropy)

    # Entropy Score
    if entropy < 40:
        score = 1
    elif entropy < 60:
        score = 2
    elif entropy < 80:
        score = 3
    elif entropy < 100:
        score = 4
    else:
        score = 5

    patterns = detect_patterns(passwd)
    total_sum = sum(p[1] for p in patterns)
    final_score = max(1, min(5, score - total_sum))

    rating = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    return {
        "score": final_score,
        "rating": rating[int(final_score)],
        "entropy": f"{entropy:.2f} bits",
        "brute_force_time": estd_time,
        "issues": [p[0] for p in patterns]
    }

