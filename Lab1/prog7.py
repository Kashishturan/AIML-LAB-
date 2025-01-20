text="Hello , welcome to world of pyton programming"
length_of_string = len(text)
print(f"Length of the string : {length_of_string}")
upper_case_string = text.upper()
print(f"Uppercase version : {upper_case_string}")
lowercase_string = text.lower()
print(f"Lowercase versio : {lowercase_string}")
substring = "Python"
is_substring_present = substring in text
print(f"Is {substring} present in the string ? {is_substring_present}")
words_list=text.split()
print(f"List of words: {words_list}")

