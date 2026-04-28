# AI-Powered API Test Generator

## Overview
This project uses AI to automatically generate test cases from API responses. The program fetches data from a public API, sends it to an AI model via Groq, and generates dynamic test cases that validate types, fields, and edge cases.

---

## How It Works

1. The program sends a request to an API endpoint  
2. The API response is captured and passed to an AI model  
3. The AI model analyzes the JSON response and generates relevant test cases  
4. The generated test cases are returned to the local application  
5. The application writes these tests into a Python test file  
6. The tests are executed using pytest for validation  

---

## Setup

### Install dependencies
