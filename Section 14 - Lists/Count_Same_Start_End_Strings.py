# return the count of the number of strings where the string length is 2 or more 
# and the first and last character are the same from a given list of strings.

def count_words(p_list):
    count = 0
    
    for string in p_list:
        if string[0] == string[-1] and len(string) > 2:
            count += 1
            
    return count
            
    
    
list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']

print(count_words(list1))
