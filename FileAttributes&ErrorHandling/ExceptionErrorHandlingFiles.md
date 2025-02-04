
# **File Attributes & Error Handling in Python**

Python provides various built-in modules, such as `os` and `pathlib`, for inspecting file attributes and handling errors efficiently. Understanding these aspects ensures smooth file operations and prevents unexpected crashes.

---

## **Checking File Attributes** 📝

Python's `os` and `pathlib` modules allow you to inspect file properties before performing operations on them.

### **1. Checking if a File Exists**
Before working with a file, it's best to check whether it exists to prevent `FileNotFoundError`.

#### **Using `os.path.exists()`**
```python
import os

file_name = "output.txt"
if os.path.exists(file_name):
    print(f"{file_name} exists.")
else:
    print(f"{file_name} does not exist.")
```

#### **Using `pathlib.Path.exists()`**
```python
from pathlib import Path

file_path = Path("output.txt")
if file_path.exists():
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exist.")
```

---

### **2. Getting File Size**
Checking a file's size helps determine whether it contains data.

#### **Using `os.path.getsize()`**
```python
import os

file_name = "output.txt"
if os.path.exists(file_name):
    size = os.path.getsize(file_name)
    print(f"File size: {size} bytes")
else:
    print("File does not exist.")
```

#### **Using `pathlib.Path.stat()`**
```python
from pathlib import Path

file_path = Path("output.txt")
if file_path.exists():
    print(f"File size: {file_path.stat().st_size} bytes")
else:
    print("File does not exist.")
```

---

### **3. Checking Last Modified Time**
You can check the last modified time of a file to determine if it has been recently updated.

#### **Using `os.path.getmtime()`**
```python
import os
import time

file_name = "output.txt"
if os.path.exists(file_name):
    last_modified = os.path.getmtime(file_name)
    print(f"Last modified: {time.ctime(last_modified)}")
else:
    print("File does not exist.")
```

#### **Using `pathlib.Path.stat()`**
```python
from pathlib import Path
import time

file_path = Path("output.txt")
if file_path.exists():
    last_modified = file_path.stat().st_mtime
    print(f"Last modified: {time.ctime(last_modified)}")
else:
    print("File does not exist.")
```

---

### **4. Checking File Permissions**
You can verify if you have the necessary permissions to read or write to a file.

#### **Using `os.access()`**
```python
import os

file_name = "output.txt"

if os.access(file_name, os.R_OK):
    print(f"{file_name} is readable.")
else:
    print(f"{file_name} is not readable.")

if os.access(file_name, os.W_OK):
    print(f"{file_name} is writable.")
else:
    print(f"{file_name} is not writable.")
```

---

## **Handling File Errors** 🚨

Errors can occur while working with files due to various reasons like missing files, insufficient permissions, or disk issues. Python’s `try-except` blocks help handle such errors gracefully.

---

### **1. Handling `FileNotFoundError`**
Occurs when trying to open a file that does not exist.

```python
try:
    with open("non_existent.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
```

🔹 **Solution:** Check for the file’s existence using `os.path.exists()` before opening it.

```python
import os

file_name = "non_existent.txt"

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        print(file.read())
else:
    print("Error: The file does not exist.")
```

---

### **2. Handling `PermissionError`**
Occurs when trying to read or write a file without sufficient permissions.

```python
try:
    with open("protected_file.txt", "w") as file:
        file.write("Test content")
except PermissionError:
    print("Error: You do not have permission to write to this file.")
```

🔹 **Solution:** Check if you have write permissions using `os.access()`.

```python
import os

file_name = "protected_file.txt"

if os.access(file_name, os.W_OK):
    with open(file_name, "w") as file:
        file.write("Test content")
    print("File written successfully.")
else:
    print("Error: You do not have permission to write to this file.")
```

---

### **3. Handling `IsADirectoryError`**
Occurs when trying to open a directory as a file.

```python
try:
    with open("some_directory", "r") as file:
        content = file.read()
except IsADirectoryError:
    print("Error: The specified path is a directory, not a file.")
```

---

### **4. Handling `IOError` (General File I/O Errors)**
Covers a broad range of file-related errors.

```python
try:
    with open("output.txt", "r") as file:
        content = file.read()
except IOError:
    print("Error: An I/O error occurred.")
```

---

## **Best Practices Summary** ✅

✔ **Use `with open()`** to manage file resources efficiently.  
✔ **Check file existence** using `os.path.exists()` or `pathlib.Path.exists()`.  
✔ **Verify permissions** using `os.access()` before reading/writing files.  
✔ **Use `try-except` blocks** to handle errors gracefully.  
✔ **Specify encoding (`encoding="utf-8"`)** when working with text files.  
✔ **Use `pathlib` for modern and object-oriented file handling.**  

---

## **Additional Example: Complete File Handling with Error Checks**
This example checks if a file exists, reads its content, and handles errors.

```python
import os

file_name = "example.txt"

try:
    if os.path.exists(file_name) and os.access(file_name, os.R_OK):
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            print("File Content:\n", content)
    else:
        print("Error: File does not exist or is not readable.")
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: Insufficient permissions to read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
