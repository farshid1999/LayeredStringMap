# LayeredStringMap

## Overview
LayeredStringMap is a data structure designed to store and manage hierarchical string-based keys efficiently. It provides functionalities such as adding, removing, and searching for strings in a layered manner, similar to a trie.

## Features
- **Append**: Add a string to the structure.
- **Remove**: Delete a string if it exists.
- **Check Existence**: Verify whether a string is stored.
- **Find Index**: Retrieve the ASCII index representation of a string.
- **Prefix Search**: Find all strings that start with a given prefix.
- **Filter Search**: Search for strings based on a custom filter function.
- **Truncate**: Clear the entire structure.

## Installation
No external libraries are required. Simply include the `LayeredStringMap` class in your project.

## Usage
```python
# Create an instance
lsm = LayeredStringMap()

# Add strings
lsm.append("apple")
lsm.append("app")
lsm.append("banana")
lsm.append("apricot")
lsm.append("grape")

# Search for a prefix
print(lsm.prefix_search("ap"))  # Output: ['apple', 'app', 'apricot']

# Check if a word exists
print(lsm.is_exist("banana"))  # Output: True

# Remove a word
lsm.remove("banana")
print(lsm.is_exist("banana"))  # Output: False

# Filter search example: words containing 'a'
print(lsm.filter_search(lambda x: 'a' in x))
```

## License
This project is open-source and available under the MIT License.

