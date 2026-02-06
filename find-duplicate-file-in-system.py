class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_map = defaultdict(list)

        for s in paths:
            parts = s.split()
            directory = parts[0]

            for file_info in parts[1:]:
                file_name, content = file_info.split('(')
                content = content[:-1]
                full_path = directory + '/' + file_name

                path_map[content].append(full_path)
            
        results = []
        for files in path_map.values():
            if len(files) > 1:
                results.append(files)

        return results
