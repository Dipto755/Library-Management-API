# Library-Management-API

TO RUN THE API:
1. Clone the repository
2. Install the required packages by running `pip install -r requirements.txt` in the terminal
3. Run the server by executing `python manage.py runserver` in the terminal
4. Open a new terminal follow the instructions.
5. To Generate API Token:
    i. Run the command `http POST http://127.0.0.1:8000/get-token/ username=<"your_username"> password=<"your_password">` without angular brackets
    ii. The response will contain the API token, copy it and use it in the subsequent requests
6. To Refresh API Token:
    i. Run the command `http POST http://127.0.0.1:8000/refresh-token/ refresh=<"Refresh Token">` without angular brackets
    ii. The response will contain the API token, copy it and use it in the subsequent requests
7. To verify API Token:
    i. Run the command `http POST http://127.0.0.1:8000/verify-token/ token=<"API Token">` without angular brackets
8. To test the API open terminal and run as follow:
    i. For CRUD Operation (Need to be logged in as Superuser):
        a. For getting all data `http http://127.0.0.1:8000/books/ 'Authorization:Bearear <Generated Api token>'` without angular brackets
        b. For getting data by id `http http://127.0.0.1:8000/books/<id>/ 'Authorization:Bearear <Generated Api token>'` without angular brackets
        c. For creating new data `http -f POST http://127.0.0.1:8000/books/ title=<Book Title> author=<Book Author> 'Authorization:Bearear <Generated Api token>'` without angular brackets
        d. For updating data `http PUT http://127.0.0.1:8000/books/<id>/ title=<Book Title> author=<Book Author> is_available=<Availability status> 'Authorization:Bearear <Generated Api token>'` without angular brackets
        e. For deleting data `http DELETE http://127.0.0.1:8000/books/<id>/ 'Authorization:Bearear <Generated Api token>'` without angular brackets
    ii. To borrow a book (Can be done by any user):
        Run the command `http POST http://127.0.0.1:8000/borrow/<Book id>/ 'Authorization:Bearear <Generated Api token>'` without angular brackets
    iii. To return a book (Can be done by any user):
        Run the command `http POST http://127.0.0.1:8000/return/<Borrow id>/ 'Authorization:Bearear <Generated Api token>'` without angular brackets