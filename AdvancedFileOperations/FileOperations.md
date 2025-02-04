# **Advanced File Operations in Python** 🚀

Beyond basic file handling, Python offers powerful tools for advanced file operations. These include working with directories, renaming and deleting files, managing file metadata, and handling temporary files.

---

## **1. Working with Directories** 📂

Python’s `os` and `pathlib` modules allow you to create, remove, and navigate directories.

### **1.1 Creating Directories**
#### **Using `os.makedirs()`**
Creates nested directories if they don’t exist.

```python
import os

directory = "new_folder/sub_folder"
os.makedirs(directory, exist_ok=True)  # `exist_ok=True` prevents errors if it already exists

print(f"Directory '{directory}' created successfully.")
```

#### **Using `pathlib.Path.mkdir()`**
```python
from pathlib import Path

path = Path("new_folder/sub_folder")
path.mkdir(parents=True, exist_ok=True)  # Create nested directories if they don't exist

print(f"Directory '{path}' created successfully.")
```

---

### **1.2 Listing Files and Directories**
#### **Using `os.listdir()`**
```python
import os

directory = "."
files = os.listdir(directory)  # Lists all files and folders in the current directory

print("Files and Directories:", files)
```

#### **Using `pathlib.Path.iterdir()`**
```python
from pathlib import Path

path = Path(".")
files = [item.name for item in path.iterdir()]  # List all items in the directory

print("Files and Directories:", files)
```

---

### **1.3 Deleting Directories**
#### **Using `os.rmdir()` (Only Works on Empty Directories)**
```python
import os

directory = "empty_folder"
os.rmdir(directory)

print(f"Directory '{directory}' removed.")
```

#### **Using `shutil.rmtree()` (Removes Non-Empty Directories)**
```python
import shutil

directory = "non_empty_folder"
shutil.rmtree(directory)

print(f"Directory '{directory}' and its contents were deleted.")
```

#### **Using `pathlib.Path.rmdir()`**
```python
from pathlib import Path

path = Path("empty_folder")
path.rmdir()

print(f"Directory '{path}' removed.")
```

---

## **2. Managing Files** 📝

### **2.1 Renaming a File**
#### **Using `os.rename()`**
```python
import os

old_name = "old_file.txt"
new_name = "new_file.txt"

os.rename(old_name, new_name)
print(f"File renamed from '{old_name}' to '{new_name}'.")
```

#### **Using `pathlib.Path.rename()`**
```python
from pathlib import Path

file_path = Path("old_file.txt")
file_path.rename("new_file.txt")

print(f"File renamed to '{file_path}'.")
```

---

### **2.2 Copying Files**
#### **Using `shutil.copy()`**
```python
import shutil

source = "source.txt"
destination = "destination.txt"

shutil.copy(source, destination)
print(f"Copied '{source}' to '{destination}'.")
```

#### **Using `shutil.copy2()` (Preserves Metadata)**
```python
shutil.copy2(source, destination)
print(f"Copied '{source}' to '{destination}' with metadata preserved.")
```

---

### **2.3 Deleting a File**
#### **Using `os.remove()`**
```python
import os

file_name = "delete_me.txt"
os.remove(file_name)

print(f"File '{file_name}' deleted.")
```

#### **Using `pathlib.Path.unlink()`**
```python
from pathlib import Path

file_path = Path("delete_me.txt")
file_path.unlink()

print(f"File '{file_path}' deleted.")
```

---

## **3. File Metadata & Permissions** 🛠️

### **3.1 Checking File Metadata**
#### **Using `os.stat()`**
```python
import os
import time

file_name = "example.txt"
file_stats = os.stat(file_name)

print(f"Size: {file_stats.st_size} bytes")
print(f"Last Modified: {time.ctime(file_stats.st_mtime)}")
print(f"Created: {time.ctime(file_stats.st_ctime)}")
```

#### **Using `pathlib.Path.stat()`**
```python
from pathlib import Path

file_path = Path("example.txt")
file_stats = file_path.stat()

print(f"Size: {file_stats.st_size} bytes")
print(f"Last Modified: {time.ctime(file_stats.st_mtime)}")
print(f"Created: {time.ctime(file_stats.st_ctime)}")
```

---

### **3.2 Changing File Permissions**
#### **Using `os.chmod()`**
```python
import os
import stat

file_name = "example.txt"

# Making file readable and writable for the owner only
os.chmod(file_name, stat.S_IRUSR | stat.S_IWUSR)

print(f"Permissions changed for '{file_name}'.")
```

#### **Using `pathlib.Path.chmod()`**
```python
from pathlib import Path
import stat

file_path = Path("example.txt")

# Making file readable and writable for the owner only
file_path.chmod(stat.S_IRUSR | stat.S_IWUSR)

print(f"Permissions changed for '{file_path}'.")
```

---

## **4. Working with Temporary Files** 🏗️

Python’s `tempfile` module allows you to create temporary files and directories.

### **4.1 Creating a Temporary File**
```python
import tempfile

with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b"Temporary data")
    print(f"Temporary file created at: {temp_file.name}")
```

---

### **4.2 Creating a Temporary Directory**
```python
import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    print(f"Temporary directory created at: {temp_dir}")

# The directory is automatically deleted when the block exits.
```

---

## **5. Working with Large Files Efficiently** 📑

### **5.1 Reading a File Line by Line**
To handle large files efficiently, read them line by line instead of loading them into memory.

```python
with open("large_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # Process each line
```

---

### **5.2 Using Generators for Large Files**
```python
def read_large_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()

for line in read_large_file("large_file.txt"):
    print(line)
```

---

## **Best Practices for Advanced File Operations** ✅

✔ **Use `pathlib` for modern, object-oriented file handling.**  
✔ **Check if a file or directory exists before performing operations.**  
✔ **Handle exceptions (`try-except`) to avoid crashes.**  
✔ **Use `shutil` for efficient file/directory copying and moving.**  
✔ **Use `tempfile` for temporary file storage.**  
✔ **Read large files using generators or line-by-line reading.**  
✔ **Use `os.access()` to check permissions before modifying files.**  


