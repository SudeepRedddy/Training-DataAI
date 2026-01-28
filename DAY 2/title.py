
song = "shape OF you"
artist = "Ed ShEErAn"
formated = f"{song.title()} - {artist.title()}"
print(formated)

location = "chenai central"
fixed_location = location.replace("chenai", "chennai")
print(fixed_location)


message = "Your Uber booking ID:UB1234. please keep it safe."
booking_id = message.split(":")[1].split(".")[0]
print(booking_id)

promo_mesaage = "Use code ZOMATO100 to get 100 off on your first order!"
if "ZOMATO100" in promo_mesaage:
    print("Promo code applied successfully!")

feedback = "The driver was polite and ride was smooth"
print(feedback.find("polite"))