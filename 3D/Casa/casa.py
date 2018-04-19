from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
#from PIL import Image
import sys
import png
#y altura do y - altura total/altura total;
#x textura = x/x total
# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'
 
# Number of the glut window.
window = 0
 
# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0
 
# texture = []
 
def LoadTextures():
    global texture
    texture = glGenTextures(2)
    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[0])
    #img = Image.open('atras.png')
    reader = png.Reader(filename='atras.png')
    w, h, pixels, metadata = reader.read_flat()

    #w, h = img.size[0], img.size[1]
    #print w, h
    #pixels = img.getdata()
    # pixels = [pixels[i * w:(i + 1) * w] for i in xrange(h)]
    #img_data = numpy.array(list(img.getdata()), numpy.uint8)
    if(metadata['alpha']):
		modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
	
    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[1])
    #img = Image.open('frente.png')
    reader = png.Reader(filename='frente.png')
    w, h, pixels, metadata = reader.read_flat()

    #w, h = img.size[0], img.size[1]
    #print w, h
    #pixels = img.getdata()
    # pixels = [pixels[i * w:(i + 1) * w] for i in xrange(h)]
    #img_data = numpy.array(list(img.getdata()), numpy.uint8)
    if(metadata['alpha']):
		modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################
 
def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
     
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
 
    glMatrixMode(GL_MODELVIEW)
 
def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1
 
    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
 
def DrawGLScene():
    global xrot, yrot, zrot, texture
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   
 
    glClearColor(0.5,0.5,0.5,1.0)            
     
    glTranslatef(0.0,0.0,-7.0)            
    #glTranslatef(1.5, 0.0, -7.0)
    #glRotatef(xrot,1.0,0.0,0.0)          
    #glRotatef(xrot,1.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    #glRotatef(zrot,0.0,0.0,1.0) 
     
    glBindTexture(GL_TEXTURE_2D, texture[1])
	#Desenho frente da casa
    glBegin(GL_QUADS)              
    glTexCoord2f(0.11, -0.12); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(0.49, -0.12);glVertex3f( 1.0, -1.0,  1.0) 
    glTexCoord2f(0.49, -0.6); glVertex3f( 1.0,  1.0,  1.0)   
    glTexCoord2f(0.11, -0.6);glVertex3f(-1.0,  1.0,  1.0)  
    glEnd()       	# Done Drawing The Cube
	
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glBegin(GL_QUADS)
	# Lateral da casa(Direita)
    glTexCoord2f(-0.09, -0.13); glVertex3f( 1.0, -1.0, -1.0)    
    glTexCoord2f(-0.09, -0.6); glVertex3f( 1.0,  1.0, -1.0)   
    glTexCoord2f(-0.49, -0.6); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(-0.49, -0.13); glVertex3f( 1.0, -1.0,  1.0)  
    glEnd()
	
    glBindTexture(GL_TEXTURE_2D, texture[1])
	#Telhado da casa(Frente)
    glBegin(GL_TRIANGLES)
    glTexCoord2f(0.3, -0.92); glVertex3f( 0.0, 2.0, 1.0) 
    glTexCoord2f(0.11, -0.6); glVertex3f(1.0,  1.0,  1.0)  	
    glTexCoord2f(0.49, -0.6); glVertex3f( -1.0, 1.0,  1.0) 
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture[0])
	#Telhado da casa(Atras)
    glBegin(GL_TRIANGLES)
    glTexCoord2f(0.3, -0.92); glVertex3f( 0.0, 2.0,  -1.0) 
    glTexCoord2f(0.5, -0.6); glVertex3f( -1.0, 1.0, -1.0) 
    glTexCoord2f(0.09, -0.6); glVertex3f(1.0,  1.0,  -1.0)  	
    glEnd()
    glBindTexture(GL_TEXTURE_2D, texture[0])
    #Atras da casa
    glBegin(GL_QUADS)
    glTexCoord2f(0.09, -0.13); glVertex3f(-1.0, -1.0, -1.0)    
    glTexCoord2f(0.09, -0.6); glVertex3f(-1.0,  1.0, -1.0)    
    glTexCoord2f(0.49, -0.6); glVertex3f( 1.0,  1.0, -1.0)    
    glTexCoord2f(0.49, -0.13); glVertex3f( 1.0, -1.0, -1.0)   
    glEnd() 
	
    glBindTexture(GL_TEXTURE_2D, texture[1])
	#Telhado(lados esquerdo)
    glBegin(GL_QUAD_STRIP) 
    glTexCoord2f(-0.11, -0.12); glVertex3f( 0.0, 2.0, 1.0) 
    glTexCoord2f(-0.49, -0.12); glVertex3f( -1.0, 1.0, 1.0)
    glTexCoord2f(-0.49, -0.6); glVertex3f( 0.0, 2.0, -1.0)
    glTexCoord2f(-0.11, -0.6); glVertex3f( -1.0, 1.0, -1.0)	
    glEnd()
	
	#Telhado(lados direito)
    glBegin(GL_QUAD_STRIP)
    glTexCoord2f(1.0, 0.0); glVertex3f( 0.0, 2.0, 1.0) 
    glTexCoord2f(0.0, 0.0); glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f( 0.0, 2.0, -1.0) 
    glTexCoord2f(0.0, 0.0); glVertex3f(1.0,  1.0,  -1.0)  	
    glEnd()
	# Lateral da casa(Esquerda)
    glBegin(GL_QUADS)
    glTexCoord2f(-0.11, -0.12); glVertex3f(-1.0, -1.0, -1.0)  
    glTexCoord2f(-0.49, -0.12); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(-0.49, -0.6); glVertex3f(-1.0,  1.0,  1.0)   
    glTexCoord2f(-0.11, -0.6); glVertex3f(-1.0,  1.0, -1.0)   
    glEnd()

	#Jardim/chao casa
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-5.0, -1.0,  5.0)  
    glTexCoord2f(1.0, 0.0); glVertex3f(5.0,  -1.0,   5.0)    
    glTexCoord2f(1.0, 1.0); glVertex3f(5.0, -1.0,  -5.0)   
    glTexCoord2f(0.0, 1.0); glVertex3f(-5.0, -1.0, -5.0)
    glEnd()
	
    xrot = xrot + 0.01                # X rotation
    yrot = yrot + 0.01                 # Y rotation
    zrot = zrot + 0.01                 # Z rotation
 
    glutSwapBuffers()
 
 
def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 0.5
        dy = 0
        dz = 0  
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 0.5
        dz = 0  
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 0.5
 
def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print "ESQUERDA"
        xrot -= dx                # X rotation
        yrot -= dy                 # Y rotation
        zrot -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        print "DIREITA"
        xrot += dx                # X rotation
        yrot += dy                 # Y rotation
        zrot += dz                     
    elif tecla == GLUT_KEY_UP:
        print "CIMA"
    elif tecla == GLUT_KEY_DOWN:
        print "BAIXO"
 
def main():
    global window
    glutInit(sys.argv)
 
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
     
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
     
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
     
    window = glutCreateWindow("Textura")
 
    glutDisplayFunc(DrawGLScene)
     
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
     
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
     
    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(keyPressed)
 
    glutSpecialFunc(teclaEspecialPressionada)
 
    # Initialize our window. 
    InitGL(640, 480)
 
    # Start Event Processing Engine    
    glutMainLoop()
 
# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()