
Struct TreeNode{
    int val = val;
    TreeNode left = None;
    TreeNode right = None;
}


void main(TreeNode root, TreeNode p, TreeNode q){
    if(root == None){
        return None;
    }
    path_p TreeNode <<vector>>;
    path_q TreeNode <<vector>>;

    void helper(TreeNode root, TreeNode node, TreeNode path){
        if(root == None){
            return;
        }
        path.append(root);
        if root == node{
            return True;
        }

        if (helper(root.left, node, path) || helper(root.right, node, path)){
            return True;
        }
        path.pop(root);
    }
    helper(root, p, path_p);
    helper(root, q, path_q);

    TreeNode res = TreeNode(None);
    int i = 0;
    int mini = math.min(length(path_p), length(path_q));
    while i < mini && path_p[i] == path_q[i]{
        res = path_p[i];
        ++i;
    }
    return res
}