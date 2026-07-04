device_status = "active"
temp = 34

if (device_status == "off"):
    print(f"Device is {device_status}")
elif (device_status == "active" and temp > 35):
    print(f"Temperature is high:{temp}")
else:
    print("Temperate is normal")      