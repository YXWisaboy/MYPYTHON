#-*- coding:utf-8 –*-
__author__ = 'Dodd'
import unit
import FP_Grow_tree
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
class tree:
	frequent=[]
	confident=[]
	def __init__(self,headnode,headtable,support,a):
		self.a=a
		self.headnode=headnode
		self.headtable=headtable
		self.support=support
		#print('ji:')
		#print(a)
		#tree.printTree(self.headnode)
		#tree.printheadtable(self.headtable)


       
	def printfrequent(self):
		File = open("hello1.txt", "w")     
		y=sorted(tree.frequent,key=lambda x:x[1],reverse=True)
		for x in y:
			#if hasNumbers(str(x[0])):	
			print(x)
			File.write(str(x) + "\n") 
			pass
			'''
			print(x)
			File.write(str(x) + "\n") 
			pass
			'''
		print(len(y))
		File.write(str(len(y)) + "\n") 
		File.close()
		
	def printconfident(self,con):
		for i in tree.frequent:
			a=i[0].split(',')
			alen=len(a)
			for j in tree.frequent:
				flag=1
				b=j[0].split(',')
				blen=len(b)
				if blen>alen:
					str1=i[0]
					str2=[]
					for x in a:
						if x not in b:
							flag=0
					if flag==1:
						for x2 in a: 
							b.remove(x2)
						str2=",".join(str(d) for d in b)
						str2=str1+'-->>'+str2
						num=float(j[1])/float(i[1])
						tree.confident.append((str2,float(j[1]),num))
		File = open("hello2.txt", "w")
		y=sorted(tree.confident,key=lambda x:x[1],reverse=True)
		count=0
		for x in y:
			if x[2]>=con:
				#if hasNumbers(str(x[0])):
				count+=1
				print(x)
				File.write(str(x) + "\n") 
				'''
				count+=1
				print(x)
				File.write(str(x) + "\n") 
				'''
			pass
		print(count)
		File.write(str(count) + "\n") 
		File.close()
	def FP_growth(self,headnode,headtable):
		a=self.a
		if tree.checkTreeOneWay(headnode):
			add=unit.generateCombination(headtable,a,self.support)
			if len(add)>0:
				tree.frequent+=add
			#print('frequent')
			#print('1',tree.frequent)
			pass
		else:
			for item in headtable:
				#datas为条件模式基
				datas=unit.generateSubset(headtable,item,self.a,tree.frequent)
				if datas:
					#print('2',item)
					if item:
						x=a[:]
						x.append(item)
						f=FP_Grow_tree.FP_Grow_tree(datas,x,self.support)
						#print('----------------ddddd-')
						#print(item,f.f.pretable)
						for jix in f.f.pretable:
							xx=a[:]
							xx.append(item)
							xx.append(jix[0])
							tree.frequent.append((",".join(str(i) for i in xx),jix[1]))
							pass
				pass
			pass
		pass
	def checkTreeOneWay(nodex):
		nodesx=nodex
		#print(nodesx)
		while nodesx:
			#print(nodesx)
			if len(nodesx.child)>1:
				return False
			if len(nodesx.child)>0:
				nodesx=nodesx.child[0]
			if len(nodesx.child)==0:
				break
			#nodesx=nodesx.child[0]
		return True
	def printTree(node):
		if len(node.child)!=0:
			print(node.name+str(node.count)+'p   '+node.parent.name if node.parent else 'not')
			for nodes in node.child:
				tree.printTree(nodes)
				pass
		else:
			print(node.name+str(node.count)+'p   '+node.parent.name if node.parent else 'not')
		print('--------------')
	def printheadtable(headtable):
		print(headtable)
		for x in headtable:
			print(headtable[x])
			y=headtable[x]
			i=0
			print(x)
			while y.next:
				y=y.next
				print(y)
				i+=1
				pass
			print(i)
			pass