error_num = 45457984738
name = "Edy"

# "old style" formatting (% operator)
print("Hello, %s" %name)
print("%x"%error_num)

print("Hello, %s, there is a 0x%x error!" %(name, error_num))
print("Hello, %(name)s, there is a 0x%(error_num)x error!" %{"name": name, "error_num":error_num})


# "new style" formatting (str.format)
print("Hello, {}".format(name))

print("Hello, {}, there is a 0x{} error!".format(name, error_num))
print("Hello, {}, there is a 0x{:x} error!".format(name, error_num))
print("Hello, {name}, there is a 0x{error_num:x} error!".format(name=name, error_num=error_num))


# "f-strings" - Nu kan vi også lave calculations i brackets osv
print(f"Hello, {name}")
print(f"Hello, {name}, there is a {error_num:#x} error!")
