UK_countries = ["England", "Scotland", "Wales", "Nothern Ireland"] 

print(UK_countries[0]) 
print(UK_countries[0 + 1]) 

print("-----------") 

wales = UK_countries[2] 
print(wales) 

print("-----------") 

last = UK_countries[-1] 
print(last) 

print("-----------") 

print(UK_countries[-3]) 

print("-----------") 

UK_countries[1] = "Skotland" 
print(UK_countries) 
UK_countries[1] = "Scotland" 

print("-----------") 

for country in UK_countries: 
    print(country) 
    
print("-----------") 

UK_countries.append("Denmark") 
print(UK_countries)