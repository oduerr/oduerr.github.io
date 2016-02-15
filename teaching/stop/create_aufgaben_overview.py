import os.path, time

header = '<!DOCTYPE html>' + '<html lang="de">' + '<head>' +  '<meta charset="utf-8">' + '<title>WaSt3</title></head> <body>'
text = '<h4>StoP Uebungsblaetter und Handouts im FS 2016</h4>'
foot = '</body></html>'


def create_cell(dir, file_name):
    str = '<td>'
    if os.path.isfile(dir + "/" + file_name):
        str += '<a href=' + dir + "/" + file_name + ">" + file_name + "</a>"
    else:
        str += '-'
    str += '</td>'
    return str

if __name__ == '__main__':
    f = open('aufgaben.html', 'w')
    f.write(header)
    f.write(text)
    f.write('Last update ' + time.asctime())
    f.write('</br>')
    f.write('<table border="1" bordercolor="#888" cellspacing="0" >\n')
    f.write('<tr><th>Woche</th><th>Praktikum</th><th>Praktikum (lsg)</th><td>Handout</td><td>Slides</td></tr>')
    for i in range(14):
        f.write('<tr>')
        dir_name = 'woche{0}'.format(i+1)
        print dir_name
        f.write('<td>' + dir_name + '</td>')
        f.write(create_cell(dir_name, 'ab{0}_nolsg.pdf'.format(i+1)))
        f.write(create_cell(dir_name, 'ab{0}_lsg.pdf'.format(i+1)))
        f.write(create_cell(dir_name, 'handout{0}.pdf'.format(i+1)))
	f.write(create_cell(dir_name, 'slides{0}.pdf'.format(i+1)))
        f.write('</tr>')
    f.write(foot)
    f.close()