from binary_search_trees import *

def is_bst_satisfied(self):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        
        val = node.data

        if val <= lower or val >= higher:
            return False
        
        if not self.helper(node.right, val, upper):
            return False
        if not self.helper(node.left, lower, upper):
            return False
        return True
    
    return self.helper(self.root)