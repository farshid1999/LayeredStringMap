# LayeredStringMap

## Overview
LayeredStringMap is a data structure designed to store and manage hierarchical string-based keys efficiently. It provides functionalities such as adding, removing, and searching for strings in a layered manner, similar to a trie.

Applications and Use Cases
1. Fast Searching in Text Databases (Text Indexing)

How it works with a dictionary?
Dictionaries still work excellently for storing and quickly searching data. In search systems like Autocomplete or Spell Checkers, because only the necessary paths (keys) are stored, search speed improves and memory usage is reduced.

Use Cases:
This structure can still be effectively used for search engines, word suggestion systems, and spell checking.

2. Data Compression

How it works with a dictionary?
Using a dictionary, only the essential and optimized parts of the data are stored. In data compression, if the data has a lot of repetition, the dictionary structure can store it in a compressed form with minimal memory usage.

Use Cases:
This structure can be used in compression systems like gzip or bzip2 and in NoSQL databases that require compressed storage.

3. Key-Value Stores

How it works with a dictionary?
Just like dictionaries are used in traditional Key-Value Stores like Redis, they can be used for quick data storage and retrieval. Operations like search and insert will be faster, and memory usage will be lower.

Use Cases:
This structure is still useful in caching systems and NoSQL databases for fast and efficient data storage.

4. Log Analysis and Text Processing

How it works with a dictionary?
Dictionaries allow fast and efficient storage and search for information (such as IP addresses or specific patterns). This is particularly useful for log analysis and network data processing because searches will be faster and less costly.

Use Cases:
This can be effectively used in firewalls, Intrusion Detection Systems (IDS), and security log analysis.

5. Pattern Matching and String Processing

How it works with a dictionary?
Using a dictionary, pattern searching in large texts (such as DNA sequences) and fast string processing can be performed. This compressed and optimized structure will perform pattern matching faster than other methods.

Use Cases:
Useful in DNA sequencing algorithms, pattern recognition in texts, and anomaly detection systems.

Conclusion
 Using a dictionary leads to optimized memory usage while maintaining all core applications.
 The listed use cases (fast searching, data compression, key-value stores, log analysis, pattern matching) are still achievable with this structure.
 This structure is now even more efficient in text processing, fast storage, and searching applications, especially in caching systems, search engines, and data analysis.

So yes, switching to a dictionary does not interfere with the applications and actually improves their efficiency!

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

