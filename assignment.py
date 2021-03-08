#!python3
# Volume Calculator
# Feel free to rename your variables
import math
import sys
def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Liam
    # Modified: 
    # title
    print('██╗░░░██╗░█████╗░██╗░░░░░██╗░░░██╗███╗░░░███╗███████╗')
    print('██║░░░██║██╔══██╗██║░░░░░██║░░░██║████╗░████║██╔════╝')
    print('╚██╗░██╔╝██║░░██║██║░░░░░██║░░░██║██╔████╔██║█████╗░░')
    print('░╚████╔╝░██║░░██║██║░░░░░██║░░░██║██║╚██╔╝██║██╔══╝░░')
    print('░░╚██╔╝░░╚█████╔╝███████╗╚██████╔╝██║░╚═╝░██║███████╗')
    print('░░░╚═╝░░░░╚════╝░╚══════╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝')
    
    print('░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░')
    print('██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗')
    print('██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝')
    print('██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗')
    print('╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║')
    print('░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝')
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Liam
    # Modified:
    while True:
        print('This program will calculate the volume of the chosen shape')
        print('1. Choose your shape')
        print('2. Enter measurements of shape')
        print('3. Program will calculate volume')
        print('\nContinue?')
        answer = input('Yes or No: ').strip()
        if answer == 'No' or answer == 'no' or answer == 'n':
            sys.exit()
        elif answer == 'Yes' or answer == "yes" or answer == 'y':
            break
    return None

def getParams():
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    print('\nShapes: Cylinder, Cube, Rectangular Prism, Triangular Prism, Cone, Pyramid, Sphere, Pentagonal Prism, Hexagonal Prism, Tetrahedron, Pentagonal Pyramid, Ellipsoid, Octahedron')

    shape = input('Enter a shape: ').strip()
    if shape == 'Cylinder':
        return [1,'Enter Radius: ','Enter Height: ']
    if shape == 'Cube':
        return [2,'Enter Length: ']
    if shape == 'Rectangular Prism':
        return [3,'Enter Length: ','Enter Height: ','Enter Width: ']
    if shape == 'Triangular Prism':
        return [4,'Enter Base Length: ','Enter Height: ','Enter Base Height: ']
    if shape == 'Cone':
        return [5,'Enter Radius: ','Enter Height: ']
    if shape == 'Pyramid':
        return [6,'Enter Base Length: ','Enter Base Width: ','Enter Height: ']
    if shape == 'Sphere':
        return [7,'Enter Radius: ']
    if shape == 'Pentagonal Prism':
        return [8,'Enter Base Length: ','Enter Height: ']
    if shape == 'Hexagonal Prism':
        return [9,'Enter Base Length: ','Enter Height: ']
    if shape == 'Tetrahedron':
        return [10, 'Enter length of Edge: ']
    if shape =='Pentagonal Pyramid':
        return [11,'Enter Base Length: ','Enter Height: ']
    if shape == 'Ellipsoid':
        return [12,'Enter semi-axe A: ','Enter semi-axe B: ', 'Enter semi-axe C: ']
    if shape == 'Octahedron':
        return [13,'Enter length of Edge: ']
    else:
        return [0,'Invalid Shape']

def getInputs(q):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements = [0]
    if  q[0]==1:
        measurements[0]=1
        for x in range (2):
            measurements.append(float(input(q[x+1])))
    elif q[0]==2:
        measurements[0]=2
        for x in range (1):
            measurements.append(float(input(q[1])))
    elif q[0]==3:
        measurements[0]=3
        for x in range (3):
            measurements.append(float(input(q[x+1])))
    elif q[0]==4:
        measurements[0]=4
        for x in range (3):
            measurements.append(float(input(q[x+1])))
    elif q[0]==5:
        measurements[0]=5
        for x in range (2):
            measurements.append(float(input(q[x+1])))
    elif q[0]==6:
        measurements[0]=6
        for x in range (3):
            measurements.append(float(input(q[x+1])))
    elif q[0]==7:
        measurements[0]=7
        for x in range (1):
            measurements.append(float(input(q[1])))
    elif q[0]==8:
        measurements[0]=8
        for x in range (2):
            measurements.append(float(input(q[x+1])))
    elif q[0]==9:
        measurements[0]=9
        for x in range (2):
            measurements.append(float(input(q[x+1])))
    elif q[0]==10:
        measurements[0]=10
        for x in range (1):
            measurements.append(float(input(q[1])))
    elif q[0]==11:
        measurements[0]=11
        for x in range (2):
            measurements.append(float(input(q[x+1])))
    elif q[0]==12:
        measurements[0]=12
        for x in range (3):
            measurements.append(float(input(q[x+1])))
    elif q[0]==13:
        measurements[0]=13
        for x in range (1):
            measurements.append(float(input(q[1])))
    elif q[0]==0:
        print(q[1])
        measurements[0]= 'Invalid'

    return measurements

def calc(x):
    #Cylinder
    if x[0]==1:
        return math.pi*(x[1]**2)*x[2]
    #Cube
    elif x[0]==2:
        return x[1]**3
   #Rectangular Prism
    elif x[0]==3:
        return x[1]* x[2]* x[3]
    #Triangular Prism
    elif x[0]==4:
        return (1/3)*x[1]*x[3]*x[2]*(1/2)
    #Cone
    elif x[0]==5:
        return (x[2]/3)*math.pi*math.pow(x[1],2)
    #Pyramid
    elif x[0]==6:
        return (x[1]*x[2]*x[3])/3
    #Sphere
    elif x[0]==7:
        return (4/3)*math.pi*math.pow(x[1],3)
    #Pentagonal Prism
    elif x[0]==8:
        return (1/4)*math.sqrt(5*(5+2*math.sqrt(5)))*math.pow(x[1],2)*x[2]
    #Hexagonal Prism
    elif x[0]==9:
        return 3*math.sqrt(3)*math.pow(x[1],2)* x[2]/2
    #Tetrahedron
    elif x[0]==10:
        return (x[1]**3)/(6*math.sqrt(2))
    #Pentagonal Pyramid
    elif x[0]==11:
        return (5/12)*math.tan(0.942478)*x[2]*math.pow(x[1],2)
    #Ellipsoid
    elif x[0]==12:
        return (4/3)*math.pi*x[1]*x[2]*x[3]
    #Octahedron
    elif x[0]==13:
        return (x[1]**3)/(3*math.sqrt(2))
    elif x[0]=='Invalid':
        return None
    

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    instructions()
    while True:
        info = calc(getInputs(getParams()))
        if info == None:
            pass
        else:
            print("Volume: ", round(info,2))
            quit = input("Quit? ") 
            if quit == "Yes" or quit == "yes" or quit == 'y':
                break
            else:
                pass
main()
