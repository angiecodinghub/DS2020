import argparse

class BSTree_Node():
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.value)

class BSTree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        # TODO
        now = self.root
        if self.root == None:
            self.root = BSTree_Node(key)
        else:
            while now:
                if key == now.value:
                    return 
                if key > now.value and now.right_child:
                    now = now.right_child
                elif key < now.value and now.left_child:
                    now = now.left_child       
                else:
                    break               
            if key > now.value:
                now.right_child = BSTree_Node(key)
            else:
                now.left_child = BSTree_Node(key)
        
    def delete(self, key):
        # TODO
        now = self.root
        previous = self.root
        found = False
        while not found and now:
            if key > now.value:
                if now.right_child:
                    previous = now
                    now = now.right_child
                else: 
                    break
            elif key < now.value:
                if now.left_child:
                    previous = now
                    now = now.left_child
                else:
                    break
            elif key == now.value:
                found = True
            elif not now.right_child and not now.left_child:
                break
        if found:
            if not now.right_child and not now.left_child: # is leaf
                if now == previous: #### root to be deleted
                    self.root = None
                elif now is previous.right_child:
                    previous.right_child = None
                else:
                    previous.left_child = None
            elif now.right_child and not now.left_child: # one child r
                if now == previous:
                    self.root = now.right_child
                elif now is previous.right_child:
                    previous.right_child = now.right_child
                else:
                    previous.left_child = now.right_child
            elif now.left_child and not now.right_child: # one child l
                if now == previous:
                    self.root = now.left_child
                elif now is previous.right_child:
                    previous.right_child = now.left_child
                else:
                    previous.left_child = now.left_child
            else: # two children
                right_tree = now.right_child
                if not right_tree.left_child:
                    now.value = right_tree.value
                    now.right_child = right_tree.right_child
                else:
                    while right_tree.left_child:
                        previous = right_tree
                        right_tree = right_tree.left_child      
                    if right_tree.right_child: # one right child
                        now.value = right_tree.value
                        previous.left_child = right_tree.right_child
                    else: # no child
                        now.value = right_tree.value
                        previous.left_child = None
   
    def inorder_helper(self, output):
        if self.root:
            left_tree = BSTree()
            left_tree.root = self.root.left_child
            left_tree.inorder_helper(output)
            output.write(str(self.root) + " ")
            right_tree = BSTree()
            right_tree.root = self.root.right_child
            right_tree.inorder_helper(output)   

    def inorder(self, output):  # output: file name
        # TODO
        self.inorder_helper(output)
        output.write('\n')
        
    def preorder_helper(self, output):
        # TODO
        if self.root:
            output.write(str(self.root) + " ")
            left_tree = BSTree()
            left_tree.root = self.root.left_child
            left_tree.preorder_helper(output)
            right_tree = BSTree()
            right_tree.root = self.root.right_child
            right_tree.preorder_helper(output)
    
    def preorder(self, output):
        self.preorder_helper(output)
        output.write('\n')
            
def main(input_path, output_path):
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    bstree = BSTree()
    output = open(output_path, 'w')
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            if line.lower() == 'inorder':
                bstree.inorder(output)
            elif line.lower() == 'preorder':
                bstree.preorder(output)
            else:
                operation = line.split(' ')[0]
                key = int(line.split(' ')[1])
                if operation.lower() == 'insert':
                    bstree.insert(key)
                elif operation.lower() == 'delete':
                    bstree.delete(key)
                else:
                    raise NotImplementedError
    output.close()


if __name__ == '__main__':
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='./input')
    parser.add_argument('--output', default='./output')
    args = parser.parse_args()

    main(args.input, args.output)

