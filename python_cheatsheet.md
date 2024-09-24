Single-Responsibility Principle (SRP)

The single-responsibility principle (SRP) comes from Robert C. Martin, more commonly known by his nickname Uncle Bob, who’s a well-respected figure in the software engineering world and one of the original signatories of the Agile Manifesto. In fact, he coined the term SOLID.

The single-responsibility principle states that:

`A class should have only one reason to change.`

This means that a class should have only one responsibility, as expressed through its methods. If a class takes care of more than one task, then you should separate those tasks into separate classes.

Note: You’ll find the SOLID principles worded in various ways out there. In this tutorial, you’ll refer to them following the wording that Uncle Bob uses in his book Agile Software Development: Principles, Patterns, and Practices. So, all the direct quotes come from this book.

If you want to read alternate wordings in a quick roundup of these and related principles, then check out Uncle Bob’s The Principles of OOD.

This principle is closely related to the concept of separation of concerns, which suggests that you should split your programs into different sections. Each section must address a separate concern.

To illustrate the single-responsibility principle and how it can help you improve your object-oriented design, say that you have the following FileManager class:

```python
# file_manager_srp.py

from pathlib import Path
from zipfile import ZipFile

class FileManager:
def **init**(self, filename):
self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
```

In this example, your FileManager class has two different responsibilities. It uses the .read() and .write() methods to manage the file. It also deals with ZIP archives by providing the .compress() and .decompress() methods.

This class violates the single-responsibility principle because it has two reasons for changing its internal implementation. To fix this issue and make your design more robust, you can split the class into two smaller, more focused classes, each with its own specific concern:

```python
# file_manager_srp.py

from pathlib import Path
from zipfile import ZipFile

class FileManager:
def **init**(self, filename):
self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
def **init**(self, filename):
self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
```

Now you have two smaller classes, each having only a single responsibility. FileManager takes care of managing a file, while ZipFileManager handles the compression and decompression of a file using the ZIP format. These two classes are smaller, so they’re more manageable. They’re also easier to reason about, test, and debug.

The concept of responsibility in this context may be pretty subjective. Having a single responsibility doesn’t necessarily mean having a single method. Responsibility isn’t directly tied to the number of methods but to the core task that your class is responsible for, depending on your idea of what the class represents in your code. However, that subjectivity shouldn’t stop you from striving to use the SRP.
