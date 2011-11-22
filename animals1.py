import random
import time

class Animal:
	def crawl(self):
		if self.dirctn == 'N' and self.lis[1]< 9:
			self.lis[1] += 1
                        print "new position %s%s%s" %(self.name,self.lis,self.dirctn)
		
		elif self.dirctn == 'S' and self.lis[1]> 0:
			self.lis[1] -= 1
			print "new position %s%s%s" %(self.name,self.lis,self.dirctn)
		
		elif self.dirctn == 'E' and self.lis[0]< 9:
			self.lis[0] += 1
			print "new position %s%s%s" %(self.name,self.lis,self.dirctn)
		
		elif self.dirctn == 'W' and self.lis[0]> 0:
			self.lis[0] -= 1
			print "new position %s%s%s" %(self.name,self.lis,self.dirctn)
		else:
			self.dirctn=self.turn()

	def jump(self):
		if self.dirctn == 'N' and self.lis[1]< 8:
                        self.lis[1] += 2
                        print "new position %s%s%s" %(self.name,self.lis,self.dirctn)
                
		elif self.dirctn == 'S' and self.lis[1]> 1:
                        self.lis[1] -= 2
                        print "new position %s%s%s" %(self.name,self.lis,self.dirctn)
                
		elif self.dirctn == 'E' and self.lis[0]< 8:
                        self.lis[0] += 2
                        print "new position %s%s%s" %(self.name,self.lis,self.dirctn)
                
		elif self.dirctn == 'W' and self.lis[0]> 1:
                        self.lis[0] -= 2
                        print "new position %s%s%s" %(self.name,self.lis,self.dirctn)
                
		else:
                        self.dirctn = self.turn()


	def eat(self,objlist,obj):
		
		print "%s get eaten" %(obj.name)
		
		
			
			
		

	def turn(self):
		if self.dirctn == 'N':
			seq = ['E','W','S']
			return random.choice(seq)
		elif self.dirctn == 'S':
			seq = ['N','E','W']
			return random.choice(seq)
		elif self.dirctn == 'E':
                        seq = ['N','S','W']
                        return random.choice(seq)
		else: 
                        seq = ['N','E','S']
                        return random.choice(seq)


class Worm(Animal):
	def __init__(self,name,lis,dirctn):
		self.name = name
		self.lis = lis
		self.dirctn = dirctn
		print "Worm Created:%s%s%s"%(self.name,self.lis,self.dirctn)
	
	def move(self):
		Animal.crawl(self)
	
class Ghopper(Animal):
	def __init__(self,name,lis,dirctn):
		self.name = name
		self.lis = lis
		self.dirctn = dirctn
		print "Grass Hopper Created:%s%s%s"%(self.name,self.lis,self.dirctn)

	def move(self):
		Animal.jump(self)

	def eat(self,objlist,obj):
		Animal.eat(self,objlist,obj)


class Frog(Animal):
	def __init__(self,name,lis,dirctn):
		self.name = name
		self.lis = lis
		self.dirctn = dirctn
		print "Frog Created:%s%s%s"%(self.name,self.lis,self.dirctn)

	def move(self):
		Animal.jump(self)

	def eat(self,objlist,obj):
		Animal.eat(self,objlist,obj)


class Snake(Animal):
        def __init__(self,name,lis,dirctn):
                self.name = name
                self.lis = lis
                self.dirctn = dirctn
                print "Snake Created:%s%s%s"%(self.name,self.lis,self.dirctn)

        def move(self):
                Animal.crawl(self)

        def eat(self,objlist,obj):
                Animal.eat(self,objlist,obj)


class Bfrog(Frog):
        def __init__(self,name,lis,dirctn):
                self.name = name
                self.lis=lis
                self.dirctn=dirctn
                print "Bull Frog Created:%s%s%s"%(self.name,self.lis,self.dirctn)

        def move(self):
                Frog.jump(self)

        def eat(self,objlist,obj):
                Frog.eat(self,objlist,obj)


def main():
	w1 = Worm('W1',[1,1],'N')
	g1 = Ghopper('G1',[2,1],'E')
	f1 = Frog('F1',[2,3],'S')
	s1 = Snake('S1',[5,2],'W')
	bf1 = Bfrog('BF1',[3,3],'N')
	objlist = [w1,g1,f1,s1,bf1]
	while(len(objlist)>1):
		print "**********************************"	
		poslist = []
		try:
			rmv_obja=None
			rmv_obja1=None
			rmv_objb=None
			rmv_objb1=None
			rmv_objc=None
			rmv_objc1=None
			rmv_objd=None
			rmv_objd1=None
			time.sleep(1)
			for obj in range(0,len(objlist)):
				objlist[obj].move()
				if len(poslist) == 0:
					poslist.extend([objlist[obj],objlist[obj].lis])
				
				else:
					poslist.extend([objlist[obj],objlist[obj].lis])
					for i in range(1,len(poslist)-2,2):
						if poslist[i] == objlist[obj].lis:
							cname1 = poslist[i-1].__class__.__name__
							cname2 = objlist[obj].__class__.__name__
							if cname1 == "Ghopper" and cname2 == "Worm":
								poslist[i-1].eat(objlist,objlist[obj])
								rmv_obja=objlist[obj]
								poslist.remove(objlist[obj].lis)
								poslist.remove(objlist[obj])
								break
							
							elif cname1 == "Worm" and cname2 == "Ghopper":
								objlist[obj].eat(objlist,poslist[i-1])
								rmv_obja1=poslist[i-1]
								poslist.remove(poslist[i-1])
								poslist.remove(poslist[i-1])
								break
							
							elif cname1 == "Frog" and cname2 == "Ghopper":
								poslist[i-1].eat(objlist,objlist[obj])
								rmv_objb=objlist[obj]
								poslist.remove(objlist[obj].lis)
								poslist.remove(objlist[obj])
								break
							
							elif cname1 == "Ghopper" and cname2 == "Frog":
								objlist[obj].eat(objlist,poslist[i-1])
								rmv_objb1=poslist[i-1]
								poslist.remove(poslist[i-1])
								poslist.remove(poslist[i-1])
								break
							
							elif cname1 == "Snake" and (cname2 == "Ghopper" or cname2 == "Frog"):
								poslist[i-1].eat(objlist,objlist[obj])
								rmv_objc=objlist[obj]
								poslist.remove(objlist[obj].lis)
								poslist.remove(objlist[obj])
								break
							
							elif (cname1 == "Ghopper" or cname1 == "Frog") and cname2 == "Snake":
								objlist[obj].eat(objlist,poslist[i-1])
								rmv_objc1=poslist[i-1]
								poslist.remove(poslist[i-1])
								poslist.remove(poslist[i-1])
								break
							
							elif cname1 == "Bfrog" and (cname2 == "Frog" or cname2 == "Snake"):
								poslist[i-1].eat(objlist,objlist[obj])
								rmv_objd=objlist[obj]
								poslist.remove(objlist[obj].lis)
								poslist.remove(objlist[obj])
								break
							
							elif (cname1 == "Frog" or cname2 == "Snake") and cname2 == "Bfrog":
								objlist[obj].eat(objlist,poslist[i-1])
								rmv_objd1=poslist[i-1]
								poslist.remove(poslist[i-1])
								poslist.remove(poslist[i-1])
								break
							elif cname1==cname2:
								pass
			if rmv_obja:
				objlist.remove(rmv_obja)
			if rmv_obja1:
				objlist.remove(rmv_obja1)
			if rmv_objb:
				objlist.remove(rmv_objb)
			if rmv_objb1:
				objlist.remove(rmv_objb1)
			if rmv_objc:
				objlist.remove(rmv_objc)
			if rmv_objc1:
				objlist.remove(rmv_objc1)
			if rmv_objd:
				objlist.remove(rmv_objd)
			if rmv_objd1:
				objlist.remove(rmv_objd1)
		except IndexError,NameError:
			continue	

print "Game over"
main()
