# Get clock-in and clock-out time from the user in military time
clock_in_time = input("What is the military time for when you clocked in? ")
clock_out_time = input("What is the military time for when you clocked out? ")

# Split time format into hours and minutes variable
in_list = clock_in_time.split(":")
out_list = clock_out_time.split(":")
in_hour = in_list[0]
in_minute = in_list[1]
out_hour = out_list[0]
out_minute = out_list[1]