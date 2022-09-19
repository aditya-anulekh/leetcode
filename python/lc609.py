class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        contents = {}
        for path in paths:
            path = path.split(" ")
            directory = path[0]
            for p in path[1:]:
                fname, file_content = p.split('(')
                file_content = file_content[:-1]
                if contents.get(file_content):
                    contents[file_content].append(directory + '/' + fname)
                else:
                    contents[file_content] = [directory + '/' + fname]
        return_list = [value for value in contents.values() if len(value)>1]
        return return_list



if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))