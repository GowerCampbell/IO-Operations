## **What Are Advanced File Operations?**
Advanced file operations go beyond just reading and writing files. They include:
1. **Working with directories** (folders): Creating, listing, and deleting them.
2. **Managing files**: Renaming, copying, and deleting files.
3. **Handling file metadata**: Checking file size, creation/modification dates, and permissions.
4. **Working with temporary files**: Creating files and directories that are automatically deleted when no longer needed.
5. **Efficiently handling large files**: Reading and processing large files without running out of memory.

These operations are essential for tasks like organizing files, automating file management, and working with large datasets.

---

## **1. Working with Directories** 📂

### **What is a Directory?**
A directory (or folder) is a place where files and other directories are stored. For example, your "Documents" folder is a directory.

---

### **1.1 Creating Directories**
You can create directories (folders) using Python.

#### **Example: Creating a Directory**
```python
import os

# Create a directory called "my_folder"
os.makedirs("my_folder", exist_ok=True)
print("Directory 'my_folder' created!")
```

- `os.makedirs()` creates a directory. If the directory already exists, `exist_ok=True` prevents an error.
- If you want to create nested directories (e.g., `my_folder/sub_folder`), this works too!

---

### **1.2 Listing Files and Directories**
You can list all the files and folders inside a directory.

#### **Example: Listing Files**
```python
import os

# List all files and folders in the current directory
files = os.listdir(".")
print("Files and Directories:", files)
```

- `os.listdir(".")` lists everything in the current directory (`.` means the current folder).

---

### **1.3 Deleting Directories**
You can delete directories, but be careful! Deleting a directory removes it permanently.

#### **Example: Deleting a Directory**
```python
import os

# Delete an empty directory
os.rmdir("my_folder")
print("Directory 'my_folder' deleted!")
```

- `os.rmdir()` only works for **empty directories**. If the directory has files, use `shutil.rmtree()` instead.

---

## **2. Managing Files** 📝

### **2.1 Renaming a File**
You can rename a file using Python.

#### **Example: Renaming a File**
```python
import os

# Rename "old_file.txt" to "new_file.txt"
os.rename("old_file.txt", "new_file.txt")
print("File renamed!")
```

---

### **2.2 Copying Files**
You can copy a file from one location to another.

#### **Example: Copying a File**
```python
import shutil

# Copy "source.txt" to "destination.txt"
shutil.copy("source.txt", "destination.txt")
print("File copied!")
```

- `shutil.copy()` creates a copy of the file.

---

### **2.3 Deleting a File**
You can delete a file using Python.

#### **Example: Deleting a File**
```python
import os

# Delete "delete_me.txt"
os.remove("delete_me.txt")
print("File deleted!")
```

---

## **3. File Metadata & Permissions** 🛠️

### **What is File Metadata?**
Metadata is information about a file, such as:
- **Size**: How big the file is (in bytes).
- **Last Modified**: When the file was last changed.
- **Created**: When the file was created.

---

### **3.1 Checking File Metadata**
You can check a file’s metadata using Python.

#### **Example: Checking File Metadata**
```python
import os
import time

# Get metadata for "example.txt"
file_stats = os.stat("example.txt")

print("Size:", file_stats.st_size, "bytes")
print("Last Modified:", time.ctime(file_stats.st_mtime))
print("Created:", time.ctime(file_stats.st_ctime))
```

---

### **3.2 Changing File Permissions**
You can change who can read, write, or execute a file.

#### **Example: Changing File Permissions**
```python
import os
import stat

# Make "example.txt" readable and writable only by the owner
os.chmod("example.txt", stat.S_IRUSR | stat.S_IWUSR)
print("Permissions changed!")
```

---

## **4. Working with Temporary Files** 🏗️

### **What Are Temporary Files?**
Temporary files are files that are created for a short time and then deleted automatically. They are useful for storing data temporarily.

---

### **4.1 Creating a Temporary File**
You can create a temporary file using Python.

#### **Example: Creating a Temporary File**
```python
import tempfile

# Create a temporary file
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b"Temporary data")
    print("Temporary file created at:", temp_file.name)
```

- The file is automatically deleted when the program ends (unless `delete=False` is used).

---

### **4.2 Creating a Temporary Directory**
You can also create a temporary directory.

#### **Example: Creating a Temporary Directory**
```python
import tempfile

# Create a temporary directory
with tempfile.TemporaryDirectory() as temp_dir:
    print("Temporary directory created at:", temp_dir)
```

- The directory is automatically deleted when the program ends.

---

## **5. Working with Large Files Efficiently** 📑

### **Why Handle Large Files Differently?**
Large files can take up a lot of memory. Instead of loading the entire file into memory, you can process it line by line.

---

### **5.1 Reading a File Line by Line**
You can read a large file one line at a time.

#### **Example: Reading a Large File**
```python
# Open a large file and read it line by line
with open("large_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # Process each line
```

---

### **5.2 Using Generators for Large Files**
Generators allow you to process large files efficiently.

#### **Example: Using a Generator**
```python
def read_large_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()  # Yield one line at a time

# Process the file line by line
for line in read_large_file("large_file.txt"):
    print(line)
```

---

## **Best Practices for Advanced File Operations** ✅

1. **Use `pathlib`**: It’s a modern way to handle files and directories.
2. **Check if a file/directory exists**: Before performing operations, make sure the file or directory exists.
3. **Handle exceptions**: Use `try-except` to avoid crashes if something goes wrong.
4. **Use `shutil`**: For copying and moving files/directories.
5. **Use `tempfile`**: For temporary storage.
6. **Read large files efficiently**: Use line-by-line reading or generators.
7. **Check permissions**: Before modifying files, ensure you have the right permissions.

---

## **Summary**
Here’s a quick summary of what we covered:

| **Operation**              | **How to Do It**                                                                 |
|----------------------------|----------------------------------------------------------------------------------|
| Create a directory         | `os.makedirs("my_folder")`                                                      |
| List files in a directory  | `os.listdir(".")`                                                               |
| Delete a directory         | `os.rmdir("my_folder")` or `shutil.rmtree("my_folder")`                         |
| Rename a file              | `os.rename("old_file.txt", "new_file.txt")`                                     |
| Copy a file                | `shutil.copy("source.txt", "destination.txt")`                                  |
| Delete a file              | `os.remove("delete_me.txt")`                                                    |
| Check file metadata        | `os.stat("example.txt")`                                                        |
| Change file permissions    | `os.chmod("example.txt", stat.S_IRUSR | stat.S_IWUSR)`                          |
| Create a temporary file    | `tempfile.NamedTemporaryFile()`                                                 |
| Create a temporary directory | `tempfile.TemporaryDirectory()`                                                |
| Read a large file          | Use line-by-line reading or generators.                                         |


