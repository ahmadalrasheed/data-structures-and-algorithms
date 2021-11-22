from code_challenges.hashtable.hash_table import HashTable



def tree_intersection(tree1,tree2):
    """
    Function to return common values between two binary search trees

    arguments:
    input-> two trees
    output-> list of common values
    """
    my_object=HashTable()
    common_values=[]
    if not tree1.root or not tree2.root:
        raise Exception('the tree is empty')

    else:
        def walk(node):
            # Using Preorder logic
            my_object.add(str(node.data),node.data)
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)
        node1=tree1.root
        tree1_elements=walk(node1)

        def contain_value(node):
            # Using Preorder logic
            if my_object.contains(str(node.data)):
                common_values.append(node.data)
            if node.left:
                contain_value(node.left)
            if node.right:
                contain_value(node.right)
            return common_values

        node2=tree2.root
        result=contain_value(node2)

        return (result)











