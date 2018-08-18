def takeInput():
    firstEqu = input( "Enter 1st equation: ")
    secondEqu = input( "Enter 2nd equation: ")
    return [ firstEqu, secondEqu ]

def extractCoef( equation ):
    str = equation.split( '+' )
    a = float( str[ 0 ].split( 'x' )[ 0 ] )
    b = float( str[ 1 ].split( 'y' )[ 0 ] )
    c = float( str[ 1 ].split( '=' )[ 1 ] )
    return [ a, b, c ]

def calculateDeterminant( coef1, coef2 ):
    determinant = coef1[ 0 ] * coef2[ 1 ] - coef2[ 0 ] * coef1[ 1 ]
    return determinant

def calculateX( det, coef1, coef2 ):
    dx = coef1[ 2 ] * coef2[ 1 ] - coef2[ 2 ] * coef1[ 1 ]
    return dx / det

def calculateY( det, coef1, coef2 ):
    dy = coef1[ 0 ] * coef2[ 2 ] - coef2[ 0 ] * coef1[ 2 ]
    return dy / det

def plotSolution( solX, solY, coef1, coef2 ):
    import matplotlib
    import matplotlib.pyplot as plt
    fig,ax = plt.subplots()
    x1 = list( range( -2 * 5, 2 * 5 + 1 ))
    y1 = []
    for x in x1:
        y1.append(( coef1[ 2 ] - coef1[ 0 ] * x ) / coef1[ 1 ] )
    ax.plot( x1, y1, color = "g", label = "Line 1" )
    x2 = list( range( -2 * 5, 2 * 5 + 1 ))
    y2 = []
    for x in x2:
        y2.append(( coef2[ 2 ] - coef2[ 0 ] * x ) / coef2[ 1 ] )
    ax.plot( x2, y2, color = "b", label = "Line 2" )
    plt.title( "Solving systems of equations" )
    solution = [ solX, solY ]
    circle = plt.Circle( solution, radius = 0.25 , color = 'r' )
    ax.add_artist( circle )
    ax.legend()
    plt.show()

def main():
    #equList = takeInput()
    equList = [ '1x + -1y = 0', '1x + 1y = 1' ]
    coef1 = extractCoef( equList[ 0 ])
    coef2 = extractCoef( equList[ 1 ])
    d = calculateDeterminant( coef1, coef2 )
    print( d )
    x = calculateX( d, coef1, coef2 )
    y = calculateY( d, coef1, coef2 )
    print( "Solution: X= ", x, "Y= ", y )
    plotSolution( x, y, coef1, coef2 )
    
main()
    