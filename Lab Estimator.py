# Estimate time for computer work
# One technician works on one computer at a time

computer_count = input("How many computers: ")
computer_count = int(computer_count)

minutes_per_computer = input("How many minutes per computer: ")
minutes_per_computer = int(minutes_per_computer)

setup_time = int(15)

total_minutes = setup_time + (computer_count * minutes_per_computer)
total_hours = total_minutes / 60

print("Estimated work: ", total_minutes, "minutes.")
print("Estimated work: ", total_hours, "hours.")
