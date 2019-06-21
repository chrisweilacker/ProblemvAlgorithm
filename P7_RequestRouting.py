# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        currentNode = self.root

        for folder in path:
            if folder != '':
                if folder not in currentNode.nodes:
                    currentNode.insert(folder)
                currentNode = currentNode.nodes[folder]

        currentNode.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        # A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
        currentNode = self.root

        for folder in path:
            if folder != '':
                if folder in currentNode.nodes:
                    currentNode = currentNode.nodes[folder]
                else:
                    return None
        
        return currentNode.handler

class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.nodes = {}
        self.handler = handler

    def insert(self, folder, handler=None):
        # Insert the node as before
        if folder not in self.nodes:
            self.nodes[folder] = RouteTrieNode(handler)
        else:
            self.nodes[folder].handler = handler
        # The Router class will wrap the Trie and handle


class Router:
    def __init__(self, handler, notFoundHandler):
        # Create a new RouteTrie for holding our routes
        self.root = RouteTrie(handler)
        self.nFHandler = notFoundHandler
        # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, path, handler = None):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        newPathList = self.split_path(path)
        self.root.insert(newPathList, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        newPathList = self.split_path(path)
        returnHandler = self.root.find(newPathList)
        if returnHandler == None:
            return self.nFHandler
        else:
            return returnHandler

    def split_path(self, path = ''):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.strip().split('/')

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
