class LayeredStringMap:
    def __init__(self):
        # Initialize an empty dictionary to store the trie structure
        self.head = {}

    def hook(self, *args):
        """ Retrieves the value stored at the given key path. """
        current = self.head
        for i in args:
            if i not in current:
                return None
            current = current[i]
        return str(current.get("value", None))

    def is_exist(self, x):
        """ Checks if a given string exists in the trie. """
        current = self.head
        for c in x:
            if c not in current:
                return False
            current = current[c]
        return "value" in current

    def append(self, x):
        """ Inserts a string into the trie. """
        current = self.head
        for c in x:
            if c not in current:
                current[c] = {}
            current = current[c]
        current["value"] = x

    def remove(self, x):
        """ Removes a string from the trie if it exists. """
        current = self.head
        stack = []

        for c in x:
            if c not in current:
                return False  # String not found
            stack.append((current, c))
            current = current[c]

        if "value" not in current:
            return False  # The string is not registered as a value

        del current["value"]  # Delete the value

        while stack:
            parent, char = stack.pop()
            if not parent[char]:
                del parent[char]
            else:
                break

        return True

    def delete(self, *args):
        """ Deletes a nested key path from the trie. """
        current = self.head
        stack = []

        for i in args:
            if i not in current:
                return False
            stack.append((current, i))
            current = current[i]

        if "value" in current:
            del current["value"]

        while stack:
            parent, char = stack.pop()
            if not parent[char]:
                del parent[char]
            else:
                break

        return True

    def truncate(self):
        """ Clears the entire trie. """
        self.head.clear()

    def __str__(self):
        """ Returns all stored values as a string representation. """
        result = []

        def traverse(node, path=""):
            if "value" in node:
                result.append(node["value"])
            for c in node:
                if c != "value":
                    traverse(node[c], path + c)

        traverse(self.head)
        return str(result)

    def prefix_search(self, prefix):
        """ Returns all stored strings that start with the given prefix. """
        current = self.head
        for c in prefix:
            if c not in current:
                return []  # Prefix not found
            current = current[c]

        result = []

        def traverse(node, path):
            if "value" in node:
                result.append(node["value"])
            for c in node:
                if c != "value":
                    traverse(node[c], path + c)

        traverse(current, prefix)
        return result

    def filter_search(self, condition):
        """ Returns stored strings that match a given condition function. """
        result = []

        def traverse(node):
            if "value" in node and condition(node["value"]):
                result.append(node["value"])
            for c in node:
                if c != "value":
                    traverse(node[c])

        traverse(self.head)
        return result

