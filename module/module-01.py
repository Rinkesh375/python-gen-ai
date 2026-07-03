import arrow

time = arrow.utcnow()

local_time = time.to("Asia/Kolkata")

print(time)
print(local_time)