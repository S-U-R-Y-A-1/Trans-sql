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

![Screenshot (79)](https://github.com/S-U-R-Y-A-1/Trans-sql/assets/126397104/e09b4176-46be-47d7-adec-c60b37d663ec)![Screenshot (80)](https://github.com/S-U-R-Y-A-1/Trans-sql/assets/126397104/87ec41b7-6913-4c4c-b6c8-a754e88a8b2a)
![Screenshot (81)](https://github.com/S-U-R-Y-A-1/Trans-sql/assets/126397104/c389a8fd-9ded-4825-b7a7-2b737e16ef41)![Screenshot (84)](https://github.com/S-U-R-Y-A-1/Trans-sql/assets/126397104/a5b407a8-5238-4041-b36e-02b68b4d61b8)



![Screenshot (86)](https://github.com/S-U-R-Y-A-1/Trans-sql/assets/126397104/a016648d-4349-428f-bfe1-bf192d6fa972)
