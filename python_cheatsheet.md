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

---

## Open-Closed Principle (OCP)

The open-closed principle (OCP) for object-oriented design was originally introduced by Bertrand Meyer in 1988 and means that:

`Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.`

To understand what the open-closed principle is all about, consider the following Shape class:

```python
# shapes_ocp.py

from math import pi

class Shape:
def **init**(self, shape_type, \*\*kwargs):
self.shape_type = shape_type
if self.shape_type == "rectangle":
self.width = kwargs["width"]
self.height = kwargs["height"]
elif self.shape_type == "circle":
self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2
```

The initializer of Shape takes a shape_type argument that can be either "rectangle" or "circle". It also takes a specific set of keyword arguments using the \*\*kwargs syntax. If you set the shape type to "rectangle", then you should also pass the width and height keyword arguments so that you can construct a proper rectangle.

In contrast, if you set the shape type to "circle", then you must also pass a radius argument to construct a circle.

Note: This example may seem a bit extreme. Its intention is to clearly expose the core idea behind the open-closed principle.

Shape also has a .calculate_area() method that computes the area of the current shape according to its .shape_type:

```python
> > > from shapes_ocp import Shape

> > > rectangle = Shape("rectangle", width=10, height=5)
> > > rectangle.calculate_area()
> > > 50
> > > circle = Shape("circle", radius=5)
> > > circle.calculate_area()
> > > 78.53981633974483
```

The class works. You can create circles and rectangles, compute their area, and so on. However, the class looks pretty bad. Something seems wrong with it at first sight.

Imagine that you need to add a new shape, maybe a square. How would you do that? Well, the option here is to add another elif clause to .**init**() and to .calculate_area() so that you can address the requirements of a square shape.

Having to make these changes to create new shapes means that your class is open to modification. That violates the open-closed principle. How can you fix your class to make it open to extension but closed to modification? Here’s a possible solution:

```python
# shapes_ocp.py

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
def **init**(self, shape_type):
self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
def **init**(self, radius):
super().**init**("circle")
self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

class Rectangle(Shape):
def **init**(self, width, height):
super().**init**("rectangle")
self.width = width
self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
def **init**(self, side):
super().**init**("square")
self.side = side

    def calculate_area(self):
        return self.side**2

```

In this code, you completely refactored the Shape class, turning it into an abstract base class (ABC). This class provides the required interface (API) for any shape that you’d like to define. That interface consists of a .shape_type attribute and a .calculate_area() method that you must override in all the subclasses.

Note: The example above and some examples in the next sections use Python’s ABCs to provide what’s called interface inheritance. In this type of inheritance, subclasses inherit interfaces rather than functionality. In contrast, when classes inherit functionality, then you’re presented with implementation inheritance.

This update closes the class to modifications. Now you can add new shapes to your class design without the need to modify Shape. In every case, you’ll have to implement the required interface, which also makes your classes polymorphic.

---
