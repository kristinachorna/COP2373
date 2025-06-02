# Kristina Chorna
# Programming Exercise 2
# This code will create an application to test an email for spam keywords and notify the user of the likelihood that
# the email message is spam.

# create a list of common spam words and phrases
SPAM_KEYWORDS = [
    "free", "win", "winner", "click here", "urgent", "act now", "congratulations",
    "limited time", "exclusive deal", "call now", "risk-free", "money back", "guarantee",
    "cheap", "easy money", "earn cash", "weight loss", "no cost", "prize", "offer expires",
    "get paid", "work from home", "cash bonus", "trial", "clearance", "miracle", "buy now",
    "income", "unsecured", "credit card"
]


def calculate_spam_score(message):
    # Calculate the spam score and return score as well as the list of keywords found in the email
    score = 0
    matched_keywords = []
    lower_message = message.lower()

    for keyword in SPAM_KEYWORDS:
        if keyword in lower_message:
            score += 1
            matched_keywords.append(keyword)

    return score, matched_keywords


def evaluate_spam_likelihood(score):
    # return the likelihood based on the number of spam words found in the email
    if score == 0:
        return "Highly unlikely to be spam."
    elif score <= 3:
        return "It could be spam."
    elif score <= 6:
        return "Likely spam."
    else:
        return "Highly likely to be spam."


# main function to display the results
def main():
    # prompt user to input an email
    message = input("Enter an email message you wish to check for spam:\n\n")

    score, matches = calculate_spam_score(message)
    likelihood = evaluate_spam_likelihood(score)

    # display the spam score and the likelihood that it is spam
    print("\n--- Spam Analysis Result ---")
    print(f"Spam Score: {score}")
    print(f"Likelihood: {likelihood}")
    if matches:
        print("Spam keywords found:")
        for word in matches:
            print(f"- {word}")
    else:
        print("No spam keywords were found in the email.")


if __name__ == "__main__":
    main()
