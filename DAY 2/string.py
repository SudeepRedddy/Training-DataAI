# string = "Welcome to Uber"
# driver = "Ravi"
# pickup = "Kompally"
# drop = "Miyapur"
# fare = 250.75
# status = "completed"
# summary = f"Driver {driver} has picked you from {pickup} and dropped you at {drop} and the total fare is Rs {fare} Your ride status is {status.upper()}."
# print(summary)

# mobile = "9876543210"
# masked = mobile[:2] + "XXXXXX" + mobile[-2:]
# print(masked)

# song = "shape OF you"
# artist = "Ed ShEErAn"
# formated = f"{song.title()} - {artist.title()}"
# print(formated)

# location = "chenai central"
# fixed_location = location.replace("chenai", "chennai")
# print(fixed_location)


# message = "Your Uber booking ID:UB1234. please keep it safe."
# booking_id = message.split(":")[1].split(".")[0]
# print(booking_id)

# promo_mesaage = "Use code ZOMATO100 to get 100 off on your first order!"
# if "ZOMATO100" in promo_mesaage:
#     print("Promo code applied successfully!")

# feedback = "The driver was polite and ride was smooth"
# print(feedback.find("polite"))

full_name = "Sudeep Reddy"
initials = "".join(full_name.split(" ")[0][0] + full_name.split(" ")[1][0])
print(initials)
