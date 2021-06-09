class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        start = (list(map(lambda x: x[0], paths)))
        for path in paths:
            if path[1] not in start: return path[1]
        
        # dic = {}
        # for i in range(len(paths)):
        #     dic[paths[i][0]] = paths[i][1]
        # city = paths[0][0]
        # while True:
        #     if city in dic.keys(): city = dic[city]
        #     else: return city

        