from create_suduko import create_sudoku
from flask import Flask,render_template,request

def wrong_answer(a):
    s = '<!DOCTYPE html>\n<html>\n<head><title>Sudoku Solution</title>\n<style>\ntable, th, td {\n  border: 1px solid black;\n  border-collapse: collapse;\n  text-align: center;\n  vertical-align: middle;  \n}\ninput {\n        color: #000000;\n        padding: 0;\n        border: 0;\n        text-align: center;\n        width: 48px;\n        height: 48px;\n        font-size: 24px;\n        background-color: #FFFFFF;\n        outline: none;\n      }\n    body{\n        border-collapse: collapse;\n  		text-align: center;\n    	background-image: url("/static/image1.jpg");\n    }\n</style></head>\n<body><center>\n<h2><p style="color:white;">Sorry!! You Lost<br>\nThis is one of the solution given below</h2>\n<table style="width:5%;height:50%;margin-top:0.2%">\n<tr>'
    for i in range(9):
        for j in range(9):
            if a[i][j] != 0:
                s += f'<td bgcolor="#99bbff"><input id="{i}{j}"  type="text" value="{a[i][j]}" disabled></td>\n'
                #s += f'<td bgcolor="grey" style="width:20%">{a[i][j]}</td>\n'
            else:
                s += f'<td bgcolor="black"><input type="text" maxlength="1" size="1" name="{i}{j}"> </td>\n'
        s += '</tr>\n'
    s += '</table>\n <form action="/"><button type="submit" style="margin-top:1%">Try again?</button></form>   </center>\n<p style="color:white;">@UDHAYA</p>\n</body>\n</html>\n'
    return s

def check(l):
    n=['1','2','3','4','5','6','7','8','9']
    u=[[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            if l[i][j] not in n:
                return False
            u[(i//3)+(j//3)].append(l[i][j])
    k=list(zip(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]))
    for i in range(9):
        if(len(set(l[i]))!=9 or len(set(k[i]))!=9 or len(set(u[i]))!=9):
            return False
    return True


app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def create_grid():
    global board
    global result
    global s
    a = create_sudoku()
    board = a[0][:]
    result = a[1]
    s='<!DOCTYPE html>\n<html>\n<head><title>Sudoku</title>\n<style>\ntable, th, td {\n  border: 1px solid black;\n  border-collapse: collapse;\n  text-align: center;\n  vertical-align: middle;  \n}\ninput {\n        color: #000000;\n        padding: 0;\n        border: 0;\n        text-align: center;\n        width: 48px;\n        height: 48px;\n        font-size: 24px;\n        background-color: #FFFFFF;\n        outline: none;\n      }\n    body{\n        border-collapse: collapse;\n  		text-align: center;\n    	background-image: url("/static/image.jpg");\n    }\n</style></head>\n<body><center><form action="/result" method="POST">\n\n<h2>Enter only numbers from 1 to 9</h2>\n<table style="width:5%;height:50%;margin-top:0.2%">\n<tr>'
    for i in range(9):
        for j in range(9):
            if board[i][j]!=0:
                s+=f'<td bgcolor="grey" style="width:0.5%">{board[i][j]}</td>\n'
            else:
                s+=f'<td bgcolor="black"><input type="text" maxlength="1" size="1" name="{i}{j}"> </td>\n'
        s+='</tr>\n'
    s+='</table>\n    <button type="submit" style="margin-top:2%">Submit</button>\n</form>\n</center>\n<form action="/"><button type="submit" style="margin-top:1%">Refresh</button></form>\n<p>@UDHAYA</p>\n</body>\n</html>\n'

    return s
@app.route('/result',methods=['POST'])
def getdata():
    global board
    tr=board[:]
    global result
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                tr[i][j]=request.form[f"{i}{j}"]
            else:
                tr[i][j]=str(tr[i][j])
            if tr[i][j]=='':
                tr[i][j]='0'
    if(not check(tr)):
        return wrong_answer(result)
    else:
        return render_template('victory.html')
if __name__ == '__main__':
    app.run(debug = True)
