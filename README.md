AI-Powered API Test Generator

Overview
The project uses AI to automatically generate test cases from API responses. The program fetches data from a Public API, the data is then sent to an AI model via Groq and generates dynamic test cases that validate types, fields and edge cases. 
How It Works:
1.	The program sends a request to an API endpoint. 
2.	The API response is captured and passed to an AI model. 
3.	The AI model analyzes the response JSON and generates relevant test cases. 
4.	The generated test cases are returned to the local application. 
5.	The application writes these tests into a Python test file. 
6.	The tests can then be executed using pytest for validation.
Setup: 
Install dependencies
•	pip install requests pytest
Set API key
•	export GROQ_API_KEY=your_api_key_here
Usage:
Step 1: Run the generator
python run_ai.py
This will:
•	Call the API
•	Generate test cases using AI
•	Save them to: tests/test_ai_users_generated.py
Step 2: Run generated tests
pytest tests/test_ai_users_generated.py
•	Example Output
•	Test functions validating
•	Required fields
•	Data types
•	Email format
•	Edge cases
Future Improvements: 
•	Automatically run tests after generation
•	Add CLI interface
•	Integrate with CI/CD pipelines
