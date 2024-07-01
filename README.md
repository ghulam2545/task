### Test for Backend Role

Our API supports two types of users: Operational Users and Client Users. Below are the functionalities available to each user type.

### Operational User

Operational Users have the following capabilities:

- [x] **Login**: Authenticate to the system to gain access to additional functionalities.
- [x] **Upload File**: Upload files to the system for storage or processing.

### Client User

Client Users have access to a broader set of functionalities:

- [x] **Signup**: Register a new user account.
- **Email Verify**: Verify the email address used during the signup process.
- [x] **Login**: Authenticate to the system to gain access to additional functionalities.
- [x] **Download File**: Download files from the system.
- [x] **List of All Uploaded Files**: View a list of all files that have been uploaded to the system.


### How to
Create a virtual environment and activate it
```bash
python3 -m venv venv
source venv/bin/activate
```

Listing of all project dependencies
```bash
pip freeze > requirements.txt
```

Download all project dependencies
```bash
pip install -r requirements.txt
```