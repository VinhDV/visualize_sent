import re

pattern = '-?[^\s]*([^\s]*[\d]+[^\s]*)+[^\s]*'
repl = ' ### '

sents = open('zalopay_des.txt').read()
sents = re.sub(pattern=pattern,repl=repl,string=sents)
h = open('processed_zalo.txt', 'w')
h.write(sents)
h.close()
