# Counting wood.

text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a Mr. Smith could chuck wood\n\r\t."""

#Replace line break with white space.
text = text.replace("\n", " ")

#loop each characters and join if it is a alphanumeric or white space
text_only_alphanum = ''.join(c for c in text if c.isalnum() or c == " " )

#split text
splitted_text = text_only_alphanum.lower().split(" ")

#declare counter and count words
counter = 0

for word in splitted_text:
    if word == "wood":
        counter += 1

print(counter, "words")