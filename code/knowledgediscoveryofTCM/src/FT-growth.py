    
    
class treeNode:  
    def __init__(self,nameValue,numOccur,parentNode):  
        self.name = nameValue #值  
        self.count = numOccur #计数  
        self.nodeLink = None #横向链  
        self.parent = parentNode #父亲节点  
        self.children = {}   #儿子节点  
    def inc(self,numOccur):  
        self.count += numOccur  
    def disp(self,ind = 1):   #输出显示  
        print( * ind,self.name,' ',self.count)
        for child in self.children.values():  
            child.disp(ind + 1)  
    #dataSet是记录,minSup是最小支持度  
def createTree(dataSet,minSup=1):  
    #对每个元素进行计数  
    headerTable = {}  
    for trans in dataSet   
        for item in trans:  
            headerTable[item] = headerTable.get(item,0) + dataSet[trans]  
  
#删除项集大小为1的非频繁项集,根据apriori原则,包含该非频繁项集的项集都不可能是频繁项集  
    for k in headerTable.keys():  
        if headerTable[k] < minSup:  
            del(headerTable[k])  
    freqItemSet = set(headerTable.keys())  
    if len(freqItemSet) == 0: return None,None  
    for k in headerTable:  
        headereTable[k] = [headerTable[k],None]  
    #创建根节点  
    retTree = treeNode('Null Set',1,None)  
    #得到删除非频繁k=1的项的 项集,并以字典树的形式插入树里。  
    for tranSet, count in dataSet.items():  
        localID = {}  
        for item in tranSet:  
            if item in freqItemSet:  
                localD[item] = headerTable[item][0]  
        if len(localD) > 0:  
            orderedItems = [v[0] for v in sorted(localD.items(),key=lambda p: p[1],reverse = True)]     #按照单个项集的频率进行排序  
             updateTree(orderedItems,retTree,headerTable,count)  
    return retTree,headerTable  
    #dataSet是记录,minSup是最小支持度 
def updateHeader(nodeToTest,targetNone):  
    while(nodeToTest.nodeLink != None):  
        nodeToTest = nodeToTest.nodeLink  
    nodeToTest.nodeLink = targetNone   
def loadSimpDat():  
    simpDat = [['r','z','h','j','p'],  
               ['z','y','x','w','v','u','t','s'],  
               ['z'],  
               ['r','x','n','o','s'],  
               ['y','r','x','z','q','t','p'],  
               ['y','z','x','e','q','s','t','m']]  
    return simpDat  
def createInitSet(dataSet):  
    retDict = {}  
    for trans in dataSet:  
        retDict[frozenset(trans)] = 1  
    return retDict  