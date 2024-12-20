from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('alogrithm'))
template = env.get_template('1.jinja2')

seq1 = ["D128", "D129", "D130", 'D131']
seq2 = ["/mnt/test"]*4
with open("va.cfg", "w") as f:
    f.write(template.render(seq1=seq1, seq2=seq2))