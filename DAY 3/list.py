# playlist = ["Shape of you","naa ready","see you again","baby","let me love you"]
# fav_food = ["biryani","burger","pizza","pasta","fried rice"]
# recent_locations = ["New York","Los Angeles","Chicago","Houston","Phoenix"]

# print(playlist)
# playlist.append("blinding lights")
# print("Updated playlist:", playlist)
# playlist.insert(2, "perfect")
# print("Playlist after insertion:", playlist)
# playlist.remove("baby")
# print("Playlist after removal:", playlist)
# playlist.pop()
# print("Playlist after popping last song:", playlist)


# list =[3,2,4,32,1,46,2]
# list.sort()
# print(list)
# list.reverse()
# print(list)
# n = list.count(2)
# print(n)
# print(list[0])
# list[0] = 10
# print(list[0]) 
# print(list)

# print(list[-2:])

# for num in list:
#     print(num, end= " ")

# list = ["apple","banana","cherry","date","elderberry"]

# if "cherry" in list:
#     print("Yes, 'cherry' is in the list.")
# else:   
#     print("No, 'cherry' is not in the list.")

# list[1] = "blueberry"
# print(list)

# str = "sudeep"
# print(str[::-1])

# order_summary = ["pizza",2,500.00,True]
# # print(order_summary)
# for index,item in enumerate(order_summary):
#     print(f"Index: {index}, Item: {item}")

# 

# mydic = {"key1":"value1","key2":"value2","key3":"value3"}
# print(type(mydic))
# print(mydic)
# trip = {
#     "destination": "Paris",
#     "duration_days": 5,
#     "accommodation": "Hotel",
#     "activities": ["sightseeing", "museum visits", "dining"]
# }
# print(trip["destination"])
# print(trip.get("duration_days"))
# print(trip.keys())
# print(trip.values())

# for key, value in trip.items():
#     print(f"{key}: {value}")

# trip.update({"duration_days":7})
# trip.pop("accommodation")
# trip["accommodation"] = "Airbnb"
# print(trip)

# for key in trip:
#     print(key,"->" ,trip[key])

# uber_cities = {"chennai","banglore","mumbai","delhi"}
# print(uber_cities)
# uber_cities.add("hyderabad")
# print(uber_cities)
# uber_cities.add("hyderabad")
# print(uber_cities)
# list_cities = list(uber_cities)
# print(list_cities)

uber_cities1 = {"chennai","banglore","mumbai","delhi"}
uber_cities2 = {"delhi","kolkata","pune","chennai"}

# print("Union:", uber_cities1.union(uber_cities2))
# print("Intersection:", uber_cities1.intersection(uber_cities2))
# print("Difference (uber_cities1 - uber_cities2):", uber_cities1.difference(uber_cities2))
uber_cities1.add("hyderabad")
print("Updated uber_cities1:", uber_cities1)
uber_cities1.remove("mumbai")
print("uber_cities1 after removal:", uber_cities1)