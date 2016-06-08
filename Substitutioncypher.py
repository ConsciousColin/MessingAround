 """
 My solution to the python challenge 
 """
 
 alph =list('abcdefghijklmnopqrstuvwxyz')

 raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


tokens = []
for i in raw:
 	if i == "z":
 		tokens.append("b")
 	if i == "y":
 		tokens.append("a")
 	if i in alph and i != "y" and i != "z":
	 	tokens.append(alph[alph.index(i)+2])
	if i not in alph:
		tokens.append(i)

"".join(tokens)