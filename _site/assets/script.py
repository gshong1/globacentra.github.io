import os

#data = "<div class=\"one-half\" style=\"text-align: center;\"> <img class=\"profile-img\" src=\"{{url}}\" alt=\"Card image cap\" style=\"max-width: 25%\"><br> <h4>{{name}}</h4> <hr><small>{{university}}<br>{{interest}}</small></div>"
data = "<div class=\"one-half\" style=\"text-align: center;\"><img class=\"profile-img\" src=\"..{{url}}\" alt=\"{{name}}\" style=\"height: 150px;\"><h4>{{name}}</h4>{{university}}<br>{{interest}}\n</div>"
#data = "{::nomarkdown}<div class=\"one-half\">{:/nomarkdown}\
#{::nomarkdown}<img class=\"profile-img\" src=\"..{{url}}\" alt=\"Card image cap\" style=\"max-width: 25%\">{:/nomarkdown}\
### [{{name}} <i class=\"fa fa-link\"></i>](#)\
#{{university}}\
#{::nomarkdown}</div>{:/nomarkdown}"


for line in os.walk('../images/profile/'):
	lines = line[2]

def findlink(string):
	global lines
        for l in lines:
        	if string.lower() in l.lower():
			lines.pop(lines.index(l))
			return l
	return 0

if __name__ == '__main__':
#	print len(lines)
	f = open("researchers.csv")
	count = 0
	for line in f:
		flag = 0
		k = line.split('#')
		name = k[0].split(' ')
		for n in name:
			temp = findlink(n)
			if(temp):
				temp = data.replace("{{url}}",str('/images/profile/'+temp))
				temp = temp.replace("{{name}}",str(' '.join(name)))
				temp = temp.replace("{{university}}",str(k[1]))
				temp = temp.replace("{{interest}}",'')
				print temp
				flag = 1
				break
		if flag == 0:
			temp = data.replace("{{url}}",str('/images/profile/holder.jpg'))
                        temp = temp.replace("{{name}}",str(' '.join(name)))
#                        temp = temp.replace("21%","25%")
                        temp = temp.replace("{{university}}",str(k[1]))
                        temp = temp.replace("{{interest}}",'')
                        print temp

		count+=1
                if count%2==0:
                	print "<br><br><br>"

	print '\n\n\n\n'
#	print len(lines)
#	for line in lines:
#		print line
