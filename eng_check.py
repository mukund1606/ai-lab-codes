import spacy


def check_grammar(sentence):
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the input sentence
    doc = nlp(sentence)

    # Check for syntax and grammar errors
    errors = []
    for token in doc:
        if token.pos_ == "VERB" and token.dep_ == "ROOT" and token.tag_ != "VBG":
            errors.append(
                "Possible grammar issue: Are you using the correct verb form?"
            )
        if token.tag_ == "NNS" and token.dep_ != "poss":
            errors.append("Possible grammar issue: Check plural nouns.")
        # Add more grammar checks as needed

    return errors


# Test the function
sentence = "He goes to schools."
errors = check_grammar(sentence)
if errors:
    print("Sentence:", sentence)
    print("Grammar errors found:")
    for error in errors:
        print(error)
else:
    print("Sentence:", sentence)
    print("No grammar errors found.")

print("\n")
sentence = "He is going to school."
errors = check_grammar(sentence)
if errors:
    print("Sentence:", sentence)
    print("Grammar errors found:")
    for error in errors:
        print(error)
else:
    print("Sentence:", sentence)
    print("No grammar errors found.")
