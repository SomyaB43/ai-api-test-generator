from clients.client import get_user
from utils.ai_test_generator import generate_tests_from_api

def test_ai_generated_tests():
    response = get_user(1)
    data = response.json()

    generated_code = generate_tests_from_api(data)

    print("\n Generated Tests:\n")
    print(generated_code)

    with open("tests/test_ai_users_generated.py", "w") as f:
        f.write(generated_code)

    print("\n Saved to tests/test_ai_users_generated.py")