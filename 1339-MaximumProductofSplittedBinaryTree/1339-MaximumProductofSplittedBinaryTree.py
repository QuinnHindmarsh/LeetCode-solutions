        return root.val+total(root.left)+total(root.right)

    sum1=total(root)

    def traversal(root):
        nonlocal maximum
        if root==None:
            return 0

        ls=traversal(root.left)
        rs=traversal(root.right)

        sumz=ls+rs+root.val
        
        if (sum1-rs)*rs>maximum:
            maximum=(sum1-rs)*rs
        if (sum1-ls)*ls>maximum:
            maximum=(sum1-ls)*ls

        return sumz
        
    maximum=-99999
    traversal(root)
    return maximum%(10**9+7)