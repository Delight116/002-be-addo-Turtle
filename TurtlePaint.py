import cmd
import turtle as t
import pickle
import os
import math



class Figures(object):

    def __init__(self):
        self.width = 0
        self.height = 0
        self.sideA = 0
        self.sideB = 0
        self.sideC = 0
        self.radius = 0
        self.countSides = 0

    def draw(self, args):
        'draw figure'
        pass

    def drawFill(self, args):
        'draw fill figure'
        pass

class Triangle(Figures):
    def __init__(self):
        super(Triangle, self).__init__()

    def draw(self, args):
        args = args.split()
        if len(args) > 1:
            self.sideA, self.sideB, self.sideC = args
            self.sideA = int(self.sideA)
            self.sideB = int(self.sideB)
            self.sideC = int(self.sideC)
            degA = math.degrees(math.cos(((self.sideA*self.sideA)-(self.sideB*self.sideB)+(self.sideC*self.sideC))/ (2*self.sideA*self.sideC)))
            degB = math.degrees(math.cos(((self.sideB*self.sideB)-(self.sideA*self.sideA)+(self.sideC*self.sideC))/ (2*self.sideB*self.sideC)))
            degC = math.degrees(math.cos(((self.sideB*self.sideB)-(self.sideC*self.sideC)+(self.sideA*self.sideA))/ (2*self.sideB*self.sideA)))

            t.fd(int(self.sideA))
            t.left(math.floor(degA*2))

            t.fd(int(self.sideB))
            t.left(math.floor(degB*2))

            t.fd(int(self.sideC))
            t.left(math.floor(degC*2))
        else:
            args = int(args[0])
            for i in range(3):
                t.fd(int(args))
                t.left(120)

    def drawFill(self, args):
        t.begin_fill()
        args = args.split()
        if len(args) > 1:
            self.sideA, self.sideB, self.sideC = args
            self.sideA = int(self.sideA)
            self.sideB = int(self.sideB)
            self.sideC = int(self.sideC)
            degA = math.degrees(math.cos(
                ((self.sideA * self.sideA) - (self.sideB * self.sideB) + (self.sideC * self.sideC)) / (
                2 * self.sideA * self.sideC)))
            degB = math.degrees(math.cos(
                ((self.sideB * self.sideB) - (self.sideA * self.sideA) + (self.sideC * self.sideC)) / (
                2 * self.sideB * self.sideC)))
            degC = math.degrees(math.cos(
                ((self.sideB * self.sideB) - (self.sideC * self.sideC) + (self.sideA * self.sideA)) / (
                2 * self.sideB * self.sideA)))

            t.fd(int(self.sideA))
            t.left(math.floor(degA * 2))

            t.fd(int(self.sideB))
            t.left(math.floor(degB * 2))

            t.fd(int(self.sideC))
            t.left(math.floor(degC * 2))
        else:
            args = int(args[0])
            for i in range(3):
                t.fd(args)
                t.left(120)
        t.end_fill()

class Rectamgl(Figures):
    def __init__(self):
        super(Rectamgl, self).__init__()
    def draw(self, args):
        if len(args.split()) == 1:
            args = args.split()
            self.width = int(args[0])
            self.height = int(args[0])
        else:
            self.width, self.height = args.split()
            self.width = int(self.width)
            self.height = int(self.height)
        for i in range(2):
            t.fd(self.width)
            t.left(90)
            t.fd(self.height)
            t.left(90)

    def drawFill(self, args):
        if len(args.split()) == 1:
            args = args.split()
            self.width = int(args[0])
            self.height = int(args[0])
        else:
            self.width, self.height = args.split()
            self.width = int(self.width)
            self.height = int(self.height)
        t.begin_fill()
        for i in range(2):
            t.fd(self.width)
            t.left(90)
            t.fd(self.height)
            t.left(90)
        t.end_fill()

class Circle(Figures):
    def __init__(self):
        super(Circle, self).__init__()
    def draw(self, args):
        t.circle(*parse(args))
    def drawFill(self, args):
        t.begin_fill()
        t.circle(*parse(args))
        t.end_fill()

class PolyLine(Figures):
    def __init__(self):
        super(PolyLine, self).__init__()
    def draw(self, args):
        args = parse(args)
        sides = args[1]
        length = args[0]
        angle = 360.0 / sides

        for i in range(sides):
            t.forward(length)
            t.right(angle)
    def drawFill(self, args):
        args = parse(args)
        t.begin_fill()
        sides = args[1]
        length = args[0]
        angle = 360.0 / sides
        for i in range(sides):
            t.forward(length)
            t.right(angle)
        t.end_fill()

class Paint(cmd.Cmd):
    tr = Triangle()
    rc = Rectamgl()
    cl = Circle()
    pl = PolyLine()
    fileName = None
    dataFile = list()
    prompt = '- - > '
    dataLists = ['load', 'save', 'saveAndExit', 'exit', 'help','reset','position','heading','home']
    intro ='Hello in Try Paint! You can use simple brashes and figures!!!'

    def do_line(self, x):
        'Draw line, enter size of line 50'
        t.fd(int(x))
    def do_right(self,deg):
        'turn right on X degrees  50'
        t.right(int(deg))
    def do_left(self,deg):
        'turn left on X degrees  50'
        t.right(int(deg))
    def do_setpos(self, arg):
        'Move turtle to an absolute position without painting.  SETPOS 100 200'
        t.setpos(*parse(args))
    def do_goto(self, args):
        'Move turtle to an absolute position with changing orientation.  GOTO 100 200'
        t.goto(*parse(args))
    def do_home(self, args):
        'Return turtle to the home postion:  HOME'
        t.home()
    def do_circle(self, args):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        self.cl.draw(args)
    def do_circleFill(self, args):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        self.cl.drawFill(args)
    def do_position(self, args):
        'Print the current turle position:  POSITION'
        print('Current position is %d %d\n' % self.position())
    def do_heading(self, args):
        'Print the current turle heading in degrees:  HEADING'
        print('Current heading is %d\n' % (self.heading(),))
    def do_color(self, args):
        'Set the color:  COLOR BLUE'
        t.color(args.lower())
    def do_polyline(self,args):
        'Enter the number of long-line and coals 50 6'
        self.pl.draw(args)

    def do_polylineFill(self,args):
        'Enter the number of long-line and coals 50 6'
        self.pl.drawFill(args)

    def do_rect(self,args):
        self.rc.draw(args)

    def do_rectFill(self,args):
        self.rc.drawFill(args)
    def do_treangle(self,args):
        self.tr.draw(args)

    def do_treangleFill(self, args):
        'draw treangle'
        self.tr.drawFill(args)

    def do_fillColor(self,args):
        'Set fillcolor red,green ... '
        args = args.lower()
        t.fillcolor(args)

    def do_reset(self, args):
        'Clear the screen and return turtle to center:  RESET'
        t.reset()
    def precmd(self, line):
        if line == '':
            print('enter comand from the list: ')
            line = 'help'
        elif line in self.dataLists or line.split()[0] in self.dataLists:
            print('not write')
        else:
            self.dataFile.append(line)
        tree = line.split()
        if len(tree) == 1 and tree[0] not in self.dataLists:
            line = 'help ' + tree[0]

        return line

    def do_get(self):
        'file to writing'
        print(self.dataFile)

    def do_save(self, name):
        'save file'
        if name == '':
            namer = input('Enter file name! ')
            if namer == '':
                print('Okeee')
                self.do_save('trolalal')
            else:
                self.do_save(namer)
        else:
            if name+'.p' in os.listdir('Data'):
                quest = input('this name already exists!! overwrite? (y/n)')
                if quest == "y":
                    self.fileName = name + ".p"
                else:
                    newName = name + "_copy"
                    self.do_save(newName)
            else:
                self.fileName = name+".p"

        print('saving....')
        output = open('Data/'+self.fileName,'wb')
        pickle.dump(self.dataFile, output)
        self.cmdloop('saved!')
        output.close()

    def do_saveAndExit(self,name):
        'save and exit'
        self.do_save(name)
        raise SystemExit

    def do_load(self, name):
        "Load file, nead file name, like 'file.p'"
        if name == '':
            print('File names: ', os.listdir('Data'))
            print('s')
        else:
            inputs = open('Data/'+name,'rb')
            obj = pickle.load(inputs)

            for s in obj:
                self.dataFile.append(s)
                print('- - > '+s)
                self.onecmd(s+'\n')

            inputs.close()

    def do_exit(self, args):
        'Exit from paint'
        quest = input ('Are your sure to exit (y/n)? ')
        if quest == "y":
            quest = input ('Are you  save, before out (y/n)? ')
            if quest == "y":
                raise SystemExit
            elif quest == "n":
                self.cmdloop('now you can saved')
        else:
            self.dataFile = list()
            self.cmdloop()



def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
   Paint().cmdloop()
