data = "From example@hotmail.com Sat Sep 5 09:14:16 20212"

at_index = data.find("@")
print(at_index)

after_mail = data.find(" ", at_index)
print(after_mail)

domain = data[at_index + 1 : after_mail]
print(domain)