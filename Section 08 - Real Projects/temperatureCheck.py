def check_temp(temp): 
    if temp > 28: 
        return "Hot" 
    elif 28 >= temp >= 18: 
        return "Warm" 
    else: 
        return "Cold"

temp = int(input("Enter temperature: ")) 
print(check_temp(temp))