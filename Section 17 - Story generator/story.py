# Step 1 - Create sentence maker function
# Step 2 - Create a loop which asks input from user continously
# Step 3 - Combine everything together

def sentence_maker(text):
    question_words = ["what", "how", "how's", "have", "where", "when"]
    capitalized_text = text.capitalize()
    for word in question_words:
        if text.startswith(word):
            return "{}?".format(capitalized_text)
    return "{}.".format(capitalized_text)

result = []

while True:
    user_input = input("What is on your mind? ")

    if user_input == "q":
        break
    else:
        complete_sentence = sentence_maker(user_input)
        result.append(complete_sentence)

story = " ".join(result)
print(story)

