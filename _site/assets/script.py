import os

#data = "<div class=\"one-half\" style=\"text-align: center;\"> <img class=\"profile-img\" src=\"{{url}}\" alt=\"Card image cap\" style=\"max-width: 25%\"><br> <h4>{{name}}</h4> <hr><small>{{university}}<br>{{interest}}</small></div>"
data = "<div style=\"width:500px;height:100px;border:1px solid #000;\" class=\"one-half\" style=\"text-align: center;\"> <img class=\"profile-img\" src=\"{{url}}\" alt=\"Card image cap\" style=\"max-width: 25%\"><br> <h4>{{name}}</h4> <hr><small>{{university}}<br>{{interest}}</small></div>"


def findlink(string):
	for line in os.walk('../images/profile/'):
                for l in line[2]:
                	if string.lower() in l.lower():
				return l
	return 0

if __name__ == '__main__':
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
			temp = data.replace("{{url}}",str('/images/profile/'))
                        temp = temp.replace("{{name}}",str(' '.join(name)))
                        temp = temp.replace("{{university}}",str(k[1]))
                        temp = temp.replace("{{interest}}",'')
                        print temp

		count+=1
                if count%2==0:
                	print "<div><br><br><br></div>"

