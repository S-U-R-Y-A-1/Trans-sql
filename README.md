# Translate-sql

Translate-sql is a Python application designed to leverage the Google Gemini AI to generate SQL queries based on given text inputs. The application utilizes the following tech stack:

1. Python
2. Gemini-api
3. Streamlit
4. SQLite-3

The application is powered by the **Gemini-pro** generative key and interacts with a SQLite database containing student records.

Within the SQLite database, there are two tables categorized based on departments. The schema sample of the table is as follows:

```
(Roll number, Name, Department, Marks of Subject 1, Subject 2, Subject 3, Subject 4, and Subject 5, Total Marks)
```

Users can access tables based on the department they provide as input. It's important to note that one department cannot access details of another department.

The application allows users to input text queries, which are then translated into SQL queries by the Google Gemini AI. The Streamlit interface provides a user-friendly environment for interacting with the application.

