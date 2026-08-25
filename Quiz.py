print("🎮 Welcome to my quiz game")
print("🎮 Welcome to My Quiz Game!")

answer = input("What is the capital of India? ")

if answer.lower() == "delhi":
    print("✅ Correct!")
else:
    print("❌ Wrong answer!")
print("🎮 Welcome to My Quiz Game!")

score = 0

answer = input("What is the capital of India? ")

if answer.lower() == "delhi":
    print("✅ Correct!")
    score = score + 1
else:
    print("❌ Wrong answer!")

print("Your score is:", score)
