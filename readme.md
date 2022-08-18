# PyChange My Uniandes Password
Python script for changing my university credentials. Created using Selenium

## How to run?
1. Create a file named <strong>config.json</strong> file with the following content, and replace the content between <> with your data:
```
  {
    "website": "https://cuenta.uniandes.edu.co/Cuenta2/cambioclave.jsp",
    "user":"<your email>"
    "current": 0,
    "passwords": [
      "<current password>",
      "<new password 1>",
      "<new password 2>",
      "<new password 3>",
    ]
  }
```
Note: You can add as many passwords you like. Just add a comma (,) in the last password, and then add the new password

Note: If you are having any trouble, paste the file content in this website [JSONFormatter](https://jsonformatter.curiousconcept.com/)
2. Open and IDE, or a terminal in the current folder and run the following commands

Mac OS or Linux
```
source ./venv/bin/activate
```
Windows Command Prompt
```
.\venv\bin\activate.bat
```
Windows Powershell
```
.\venv\bin\activate.ps1
```

3. Install required dependencies
```
pip install -r requirements.txt
```

4. Execute the script
```
python main.py
```

5. Remember New Password (If forgotten, check the current property)