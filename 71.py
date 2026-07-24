class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for component in path.split("/"):
            if component == "" or component == ".":
                continue
            elif component == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(component)

        return "/" + "/".join(stack)