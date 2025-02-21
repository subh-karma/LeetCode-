class FindElements(object):
    
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.groot=TreeNode()
        self.sets=set()
        
        if root is not None and root.val==-1:
            root.val=0   
            self.sets.add(root.val) 

        self.solve(root)
        self.groot=root



    def solve(self, node):
        """
        :type node: Optional[TreeNode]
        """
        if node is None:
            return
        
        if node.left is not None:
            node.left.val=2*node.val+1;   
            self.sets.add(node.left.val); 
        
        if node.right is not None:
            node.right.val=2*node.val+2;   
            self.sets.add(node.right.val); 
        
        self.solve(node.left)
        self.solve(node.right)        



    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target in self.sets:
            return True
        
        return False
