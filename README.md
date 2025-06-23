# Python Coding Challenges

This repository contains a collection of Python coding challenges designed to cover a wide range of concepts, from fundamental data structures to advanced topics like asynchronous programming, web frameworks, and AI vectorization. Each challenge is self-contained in its own file and includes a problem statement, requirements, and an example solution.

---

## Challenge Categories

The challenges are organized into the following categories:

1.  [Core Python Concepts](#core-python-concepts)
2.  [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
3.  [Advanced Language Features & Modules](#advanced-language-features--modules)
4.  [Data Science, AI & Web](#data-science-ai--web)
5.  [Combined & Mathematical Challenges](#combined--mathematical-challenges)

---

### Core Python Concepts

Basic building blocks of the Python language.

-   **challenge_1_list.py**: Manipulating lists (CRUD operations).
-   **challenge_2_dictionary.py**: Working with key-value pairs in dictionaries.
-   **challenge_3_tuple.py**: Understanding the immutability and use cases of tuples.
-   **challenge_4_loops.py**: Using `for` and `while` loops for iteration.
-   **challenge_5_functions.py**: Defining and calling functions with parameters.
-   **challenge_6_recursion.py**: Solving problems with recursive function calls (e.g., factorial).
-   **challenge_7_shallow_copy.py**: Demonstrates how a shallow copy duplicates the outer object but shares inner object references.
-   **challenge_53_deep_copy.py**: Shows how `copy.deepcopy` creates fully independent copies of nested objects.
-   **challenge_32_lambda.py**: Creating small, anonymous functions.
-   **challenge_38_exception_handling.py**: Using `try...except` blocks to handle runtime errors gracefully.
-   **challenge_39_list_comprehensions.py**: A concise way to create lists.
-   **challenge_54_set_dict_comprehensions.py**: Concise syntax for creating sets and dictionaries.
-   **challenge_40_walrus_operator.py**: Using the `:=` operator to assign variables within expressions.
-   **challenge_41_enumerate.py**: Getting both the index and value during iteration.
-   **challenge_42_map_function.py**: Applying a function to every item in an iterable.
-   **challenge_43_filter_function.py**: Filtering elements from an iterable based on a condition.
-   **challenge_55_zip_function.py**: Iterating over multiple iterables in parallel.
-   **challenge_36_regular_expressions.py**: Finding patterns in strings using the `re` module.

### Object-Oriented Programming (OOP)

Principles of structuring code using classes and objects.

-   **challenge_8_objects.py**: The fundamental concept of an object as an instance of a class.
-   **challenge_9_methods.py**: Defining functions (methods) that belong to a class.
-   **challenge_10_inheritance.py**: Creating a subclass that inherits from a parent class.
-   **challenge_11_instance.py**: Understanding that each object instance is separate and has its own data.
-   **challenge_12_method_overriding.py**: A subclass providing a specific implementation of a method that is already defined in its superclass.
-   **challenge_13_composition.py**: Building complex objects by composing other objects ("has-a" relationship).
-   **challenge_14_aggregation.py**: A "has-a" relationship where the contained object can exist independently.
-   **challenge_15_arguments.py**: Using `*args` and `**kwargs` to handle a variable number of function arguments.
-   **challenge_16_constructors.py**: Using the `__init__` method to initialize an object's state.
-   **challenge_17_encapsulation.py**: Restricting direct access to an object's internal state (using "private" attributes).
-   **challenge_18_self.py**: The `self` parameter representing the instance of the class.
-   **challenge_19_super.py**: Calling methods from the parent class.
-   **challenge_22_instance_method.py**: Standard methods that operate on an instance of a class.
-   **challenge_23_static_method.py**: Methods that belong to a class but don't operate on an instance (`@staticmethod`).
-   **challenge_24_class_method.py**: Methods that operate on the class itself, not the instance (`@classmethod`).
-   **challenge_25_duck_typing.py**: The concept that an object's suitability is determined by its methods, not its type.
-   **challenge_26_abstract_class.py**: Defining base classes that cannot be instantiated and must be subclassed.
-   **challenge_27_destructors.py**: The `__del__` method, called when an object is destroyed.
-   **challenge_28_operator_overloading.py**: Defining how standard operators (`+`, `-`, etc.) work with custom objects.
-   **challenge_34_metaclasses.py**: Advanced topic on classes that create classes.
-   **challenge_37_properties.py**: Creating getter/setter methods that are accessed like attributes (`@property`).
-   **challenge_47_passing_objects.py**: How class instances can be passed to functions as arguments.

### Advanced Language Features & Modules

Deeper dives into Python's capabilities and its powerful standard library.

-   **challenge_20_wrapper.py**: A function that wraps another function to extend its behavior.
-   **challenge_21_decorators.py**: A syntactic sugar for applying wrappers to functions (`@decorator`).
-   **challenge_29_iterators.py**: Creating custom iterators with `__iter__` and `__next__`.
-   **challenge_30_generators.py**: A simpler way to create iterators using functions and the `yield` keyword.
-   **challenge_44_yield.py**: The core keyword for creating generators.
-   **challenge_31_assert.py**: Using the `assert` statement for debugging checks.
-   **challenge_33_multithreading.py**: Running tasks concurrently (not in parallel) using the `threading` module.
-   **challenge_61_multiprocessing.py**: Running tasks in true parallelism across multiple CPU cores.
-   **challenge_35_closures.py**: Nested functions that remember the state of their enclosing scope.
-   **challenge_45_constants.py**: Discusses how constants are conventionally implemented in Python.
-   **challenge_46_with_statement.py**: Using context managers for resource management (e.g., opening/closing files).
-   **challenge_48_argparse.py**: Creating command-line interfaces for scripts.
-   **challenge_49_unittest.py**: Writing tests for your code using Python's built-in testing framework.
-   **challenge_50_pytest.py**: Using the popular third-party `pytest` framework for testing.
-   **challenge_51_logger.py**: Recording application events, warnings, and errors with the `logging` module.
-   **challenge_56_datetime.py**: Working with dates and times.
-   **challenge_57_json.py**: Serializing Python objects to JSON and vice-versa.
-   **challenge_58_pathlib.py**: An object-oriented way to handle filesystem paths.
-   **challenge_59_collections_counter.py**: A specialized dictionary for counting hashable objects.
-   **challenge_60_asyncio.py**: Writing concurrent code using the `async`/`await` syntax.

### Data Science, AI & Web

Challenges focused on popular third-party libraries for data science, AI, and web development.

-   **challenge_52_vectorization.py**: Demonstrates the performance benefits of using `NumPy` for mathematical operations over loops.
-   **challenge_62_requests.py**: Making HTTP requests to web APIs.
-   **challenge_63_pandas.py**: Using the `pandas` library for 2D data manipulation with DataFrames.
-   **challenge_64_fastapi.py**: Building a simple web API with `FastAPI`.
-   **challenge_69_nn_forward_pass.py**: A vectorized simulation of a neural network's forward pass calculation using `NumPy`.
-   **challenge_70_llm_encoder.py**: Simulating a simplified LLM encoder block using self-attention.
-   **challenge_71_llm_decoder.py**: Simulating a simplified LLM decoder that generates text using masked self-attention.

### Combined & Mathematical Challenges

Problems that require combining multiple concepts to build a solution.

-   **challenge_65_log_analyzer.py**: Combines file I/O, string parsing, and `collections.Counter` to analyze a log file.
-   **challenge_66_persistent_api.py**: Combines `FastAPI`, `json`, and file I/O to create a web API with a persistent data store.
-   **challenge_67_oop_report_generator.py**: Combines OOP principles, `datetime`, and dictionaries to process data and generate a formatted report.
-   **challenge_68_sieve_of_eratosthenes.py**: A classic mathematical algorithm for finding prime numbers efficiently.

# C++ Coding Challenges

This section contains a collection of C++ coding challenges that cover core language features, object-oriented programming (OOP) principles, the Standard Template Library (STL), and modern C++ features.

---

### Core C++ Language

-   **challenge_1_variables.cpp**: Declaring, initializing, and printing fundamental data types.
-   **challenge_2_operators.cpp**: Using arithmetic, relational, and logical operators.
-   **challenge_3_control_flow.cpp**: Using `if/else` and `for` loops for logic and iteration.
-   **challenge_4_functions.cpp**: Defining and calling functions for code modularity.
-   **challenge_5_pointers_references.cpp**: Working with memory addresses via pointers and references.
-   **challenge_6_cstyle_arrays_strings.cpp**: Using C-style arrays and null-terminated strings.
-   **challenge_7_file_io.cpp**: Writing to and reading from files using `<fstream>`.

### Object-Oriented Programming (OOP) in C++

-   **challenge_8_classes_objects.cpp**: Defining classes and creating object instances.
-   **challenge_9_constructors_destructors.cpp**: Managing the object lifecycle with constructors and destructors (RAII).
-   **challenge_10_access_specifiers.cpp**: Encapsulating code using `public` and `private`.
-   **challenge_11_this_pointer.cpp**: Using the `this` pointer to disambiguate members and enable method chaining.
-   **challenge_12_inheritance.cpp**: Creating derived classes that inherit from a base class.
-   **challenge_13_polymorphism.cpp**: Using `virtual` functions to achieve polymorphic behavior.
-   **challenge_14_operator_overloading.cpp**: Customizing operators like `+` and `<<` for user-defined types.

### The Standard Template Library (STL)

-   **challenge_15_stl_string.cpp**: Manipulating text with the powerful `std::string` class.
-   **challenge_16_stl_vector.cpp**: Using `std::vector` as a dynamic, self-managing array.
-   **challenge_17_stl_map.cpp**: Storing and retrieving key-value pairs with `std::map`.
-   **challenge_18_stl_algorithms.cpp**: Using generic functions from `<algorithm>` like `std::sort` and `std::find`.

### Advanced & Modern C++

-   **challenge_19_exception_handling.cpp**: Managing errors with `try`, `catch`, and `throw`.
-   **challenge_20_smart_pointers.cpp**: Automating memory management with `std::unique_ptr`.
-   **challenge_21_lambda_expressions.cpp**: Writing inline, anonymous functions.
