/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> order = new ArrayList<>();

        traverse(root, order);
        return order;
    }

    public void traverse(TreeNode node, List<Integer> order){
            if (node == null) return;

            if (node.left != null){
                traverse(node.left, order);
            }
            order.add(node.val);

            if (node.right != null){
                traverse(node.right, order);
            }
            
    }
    
}