def first_last_characters(word):
  if len(word) < 2:
    quit()
  word_begin = word[0:2]
  word_end = word[-2:]
  return word_begin + word_end
    

print(first_last_characters("Apmillers"))
    