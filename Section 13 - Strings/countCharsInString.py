def count_letter(word, letter):
  times = 0
  
  for index in word:
      if index == letter:
          times += 1
      else:
          continue
  return times
        

print(count_letter("geniuses", "g"))