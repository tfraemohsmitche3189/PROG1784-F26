total_minutes = 75.0
technician_available = True
if technician_available:
    if total_minutes <= 60:
        print("Use a standard period.")
    else:
        print("Use an extended work period.")
else:
    print("Arrange technician cover.")
