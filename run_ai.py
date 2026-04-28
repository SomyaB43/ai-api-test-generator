from clients.client import get_user
from utils.ai_test_generator import generate_tests_from_api

print("Starting script...")

response = get_user()
print("API called")

data = response.json()
print("Data received:", data)

tests = generate_tests_from_api(data)
print("AI response received")

print("\n===== GENERATED TESTS =====\n")
print(tests)

with open("tests/test_ai_users_generated.py", "w") as f:
        f.write(tests)

print("\n Saved to tests/test_ai_users_generated.py")