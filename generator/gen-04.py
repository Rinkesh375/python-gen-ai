def attendance():

    print("📚 Attendance started...")

    while True:
        student = yield

        print(f"✅ Present: {student}")


teacher = attendance()

next(teacher)          # Start the generator

teacher.send("Rinkesh")
teacher.send("Nitish")
teacher.send("Manish")
teacher.send("Abhishek")