# get()
# Returnerer værdien, hvis nøglen findes.
# Ellers returnerer den standardværdien (None, hvis intet er angivet).
# Ændrer ikke dictionaryen.

# setdefault()
# Returnerer værdien, hvis nøglen findes.
# Ellers opretter den nøglen med standardværdien og returnerer den.
# Standardværdien er None, hvis intet er angivet.
# Eksisterende værdier overskrives ikke — heller ikke None.


items = {
    "computer": 10,
    "printer": 8,
    "mouse": 15,
    "keyboard": 12,
    "webcam": 7
}

print(items["computer"])
# print(items["microphone"])  # Giver KeyError, fordi nøglen ikke findes.


# get() med en eksisterende nøgle: returnerer 10.
quantity_computer = items.get("computer")
print(f"Number of computers in the store: {quantity_computer}")

# Nøglen findes ikke: returnerer None.
quantity_microphone = items.get("microphone")
print(f"Number of microphones in the store: {quantity_microphone}")

# Nøglen findes ikke: returnerer standardværdien 0.
quantity_microphone_zero = items.get("microphone", 0)
print(f"Number of microphones in the store: {quantity_microphone_zero}")

# Nøglen findes ikke: returnerer teksten som standardværdi.
quantity_microphone_text = items.get("microphone", "The item is not in store")
print(f"Number of microphones in the store: {quantity_microphone_text}")

# "microphone" er ikke blevet tilføjet af get().
print(items)


# setdefault() opretter "mousepad" med værdien None og returnerer None.
quantity_mousepad = items.setdefault("mousepad")
print(f"Number of mousepads in the store: {quantity_mousepad}")
print(items)

# Opretter "headset" med værdien 0 og returnerer 0.
quantity_headset = items.setdefault("headset", 0)
print(f"Number of headsets in the store: {quantity_headset}")
print(items)

# Opretter "monitor" med værdien 2 og returnerer 2.
quantity_monitor = items.setdefault("monitor", 2)
print(f"Number of monitors in the store: {quantity_monitor}")
print(items)

# "monitor" findes allerede: returnerer 2 og ændrer ikke værdien til 10.
quantity_monitor_existing = items.setdefault("monitor", 10)
print(f"Number of monitors in the store: {quantity_monitor_existing}")
print(items)

# "mousepad" findes allerede: returnerer None og ændrer ikke værdien til 0.
quantity_mousepad_existing = items.setdefault("mousepad", 0)
print(f"Number of mousepads in the store: {quantity_mousepad_existing}")
print(items)