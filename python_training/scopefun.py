def max(a,b):				#scopefun.py LEGB
	if a > b:
		return "a in global"
	return "b in global"
def funA(a,b):			#funA(10,20)
	def max(a,b):
		if a > b:
			return "a in funA"
		return "b in funA"
	def funB(a,b):
		def max(a,b):
			if a > b:
				return "a in funB"
			return "b in funB"
		def funC(a,b):
			def max(a,b):
				if a > b:
					return "a in funC"
				return "b in funC"
			print(max(a,b))			#max(10,20)
		funC(a,b)		#funC(10,20)
	funB(a,b)			#funB(10,20)

funA(20,10)
#scopefun.py
