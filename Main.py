from ApiHandler import ApiHandler
import datetime

api_handler = ApiHandler()
newPost = {"title": "Security Interview Post", "userId": 500,
           "body": "This is an insertion test with a known API"}

print("\nGoal 1. Print the value of the title for post number 99")
data = api_handler.get("posts", 99)
print("Title:", data["title"], "\n")

print("Goal 2. Inject a field called time into the results")
data = api_handler.get("posts", 100)
print("Retrieved data:")
print(data, "\n")
data["time"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print("Modified data:")
print(data, "\n")

print("Goal 3. Create a new /posts entry")
data = api_handler.post("posts", newPost)
print("A new /posts entry has been created\n")
print("Goal 4. Determine if your post was successful")
print("Yes, the post was successful")
print(newPost, "\n")

print("Goal 5. Print the tuple from #4")
print(data, "\n")

print("Goal 6. Delete the record you created in #3")
data = api_handler.delete("posts", data[0])

print(data, "\n")
