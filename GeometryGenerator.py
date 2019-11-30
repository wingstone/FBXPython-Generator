"""

 
"""

import sys
import math

SAVE_FILE_NAME = "Example.Fbx"

def CreateScene(pSdkManager, pScene, pSampleFileName):
    #AddCube( pScene )
    AddSphere( pScene )
    return True

def AddSphere( pScene, center = ( 0, 0, 0 ), redius = 1, row = 5, colum = 5 ):
    ''' Adds a sphere mesh to the scene. '''

    rootNode = pScene.GetRootNode()

    sphereNode = FbxNode.Create( pScene, 'SphereNode' )
    rootNode.AddChild( sphereNode )

    sphereMesh = FbxMesh.Create( pScene, 'SphereMesh' )
    sphereNode.SetNodeAttribute( sphereMesh )

    # mesh
    if row < 2 or colum < 3:
        return False

    # control point
    sphereMesh.InitControlPoints( (row - 1)*colum + 2 )
    sphereMesh.SetControlPointAt(FbxVector4(0, redius, 0), 0)
    for i in range( 0, row - 1 ):
        for j in range( 0, colum ):
            phi = math.pi / row * (i+1)
            theta = j / colum*2*math.pi
            sphereMesh.SetControlPointAt( FbxVector4( redius*math.sin(phi)*math.cos(theta), redius*math.cos(phi), redius*math.sin(phi)*math.sin(theta) ), i*colum+ j+1 )
    sphereMesh.SetControlPointAt(FbxVector4(0, -redius, 0),  (row - 1)*colum + 1)

    # first row
    for i in range( 0, colum-1 ):
        sphereMesh.BeginPolygon( i )
        sphereMesh.AddPolygon(0)
        sphereMesh.AddPolygon(i+2)
        sphereMesh.AddPolygon(i+1)
        sphereMesh.EndPolygon()
    sphereMesh.BeginPolygon( colum-1 )
    sphereMesh.AddPolygon(0)
    sphereMesh.AddPolygon(1)
    sphereMesh.AddPolygon(colum)
    sphereMesh.EndPolygon()

    # middle row
    for i in range( 0, row-2 ):
        for j in range(0, colum-1):
            sphereMesh.BeginPolygon( i*colum + colum + j )
            sphereMesh.AddPolygon( i*colum + j+1 )
            sphereMesh.AddPolygon( i*colum + j+2 )
            sphereMesh.AddPolygon( (i+1)*colum + j+2 )
            sphereMesh.AddPolygon( (i+1)*colum + j+1 )
            sphereMesh.EndPolygon()
        sphereMesh.BeginPolygon( i*colum + 2*colum - 1 )
        sphereMesh.AddPolygon( (i+1)*colum )
        sphereMesh.AddPolygon( i*colum +1 )
        sphereMesh.AddPolygon( (i+1)*colum+1 )
        sphereMesh.AddPolygon( (i+2)*colum )
        sphereMesh.EndPolygon()

    # last row
    for i in range( 0, colum-1 ):
        sphereMesh.BeginPolygon( i + colum*(row-1) )
        sphereMesh.AddPolygon( i + colum*(row-2)+1 )
        sphereMesh.AddPolygon( i + colum*(row-2)+2 )
        sphereMesh.AddPolygon( (row - 1)*colum + 1 )
        sphereMesh.EndPolygon()
    sphereMesh.BeginPolygon( colum*2+2 )
    sphereMesh.AddPolygon( (row - 1)*colum )
    sphereMesh.AddPolygon( (row - 2)*colum+1 )
    sphereMesh.AddPolygon( (row - 1)*colum + 1 )
    sphereMesh.EndPolygon()


def AddCube( pScene, center = ( 0, 0, 0 ), length = 1):
    ''' Adds a cubic mesh to the scene. '''

    rootNode = pScene.GetRootNode()

    cubeNode = FbxNode.Create( pScene, 'CubeNode' )
    rootNode.AddChild( cubeNode )

    cubeMesh = FbxMesh.Create( pScene, 'CubeMesh' )
    cubeNode.SetNodeAttribute( cubeMesh )

    # 左手坐标系
    # 左乘cross
    halfLength = length / 2
    center = FbxVector4( center[0], center[1], center[2] )

 	# A set of vertices which we will use to create a cube in the scene.
    cubeVertices = [ FbxVector4( -1, -1, -1 ) * halfLength + center, # 0 - vertex index.
                     FbxVector4(  1, -1, -1 ) * halfLength + center, # 1
                     FbxVector4(  1,  1, -1 ) * halfLength + center, # 2
                     FbxVector4( -1,  1, -1 ) * halfLength + center, # 3
                     FbxVector4( -1, -1,  1 ) * halfLength + center, # 4
                     FbxVector4(  1, -1,  1 ) * halfLength + center, # 5
                     FbxVector4(  1,  1,  1 ) * halfLength + center, # 6
                     FbxVector4( -1,  1,  1 ) * halfLength + center] # 7

    # The polygons (faces) of the cube.
    polygonVertices = [ (  0,  1,  2,  3 ), # Face 1 - composed of the vertex index sequence: 0, 1, 2, and 3.
                        (  4,  5,  6,  7 ), # Face 2
                        (  8,  9, 10, 11 ), # Face 3
                        ( 12, 13, 14, 15 ), # Face 4
                        ( 16, 17, 18, 19 ), # Face 5
                        ( 20, 21, 22, 23 )] # Face 6

    cubeMesh.InitControlPoints( 24 )

    # Face 1
    cubeMesh.SetControlPointAt( cubeVertices[3], 0 )
    cubeMesh.SetControlPointAt( cubeVertices[2], 1 )
    cubeMesh.SetControlPointAt( cubeVertices[1], 2 )
    cubeMesh.SetControlPointAt( cubeVertices[0], 3 )
    # Face 2
    cubeMesh.SetControlPointAt( cubeVertices[4], 4 )
    cubeMesh.SetControlPointAt( cubeVertices[7], 5 )  
    cubeMesh.SetControlPointAt( cubeVertices[3], 6 )
    cubeMesh.SetControlPointAt( cubeVertices[0], 7 )
    # Face 3
    cubeMesh.SetControlPointAt( cubeVertices[0], 8 )
    cubeMesh.SetControlPointAt( cubeVertices[1], 9 )
    cubeMesh.SetControlPointAt( cubeVertices[5], 10 )
    cubeMesh.SetControlPointAt( cubeVertices[4], 11 )
    # Face 4
    cubeMesh.SetControlPointAt( cubeVertices[7], 12 )
    cubeMesh.SetControlPointAt( cubeVertices[6], 13 )
    cubeMesh.SetControlPointAt( cubeVertices[2], 14 )
    cubeMesh.SetControlPointAt( cubeVertices[3], 15 )
    # Face 5
    cubeMesh.SetControlPointAt( cubeVertices[6], 16 )
    cubeMesh.SetControlPointAt( cubeVertices[5], 17 )
    cubeMesh.SetControlPointAt( cubeVertices[1], 18 )
    cubeMesh.SetControlPointAt( cubeVertices[2], 19 )
    # Face 6
    cubeMesh.SetControlPointAt( cubeVertices[4], 20 )
    cubeMesh.SetControlPointAt( cubeVertices[5], 21 )
    cubeMesh.SetControlPointAt( cubeVertices[6], 22 )
    cubeMesh.SetControlPointAt( cubeVertices[7], 23 )

    for i in range( 0, len( polygonVertices ) ):

        cubeMesh.BeginPolygon( i )

        for j in range( 0, len( polygonVertices[i] ) ):

            cubeMesh.AddPolygon( polygonVertices[i][j] )

        cubeMesh.EndPolygon()

#########
#
# main function
# copy from python sdk
#
#########

if __name__ == "__main__":
    try:
        import FbxCommon
        from fbx import *
    except ImportError:
        print("Error: module FbxCommon and/or fbx failed to import.\n")
        print("Copy the files located in the compatible sub-folder lib/python<version> into your python interpreter site-packages folder.")
        import platform
        if platform.system() == 'Windows' or platform.system() == 'Microsoft':
            print('For example: copy ..\\..\\lib\\Python27_x64\\* C:\\Python27\\Lib\\site-packages')
        elif platform.system() == 'Linux':
            print('For example: cp ../../lib/Python27_x64/* /usr/local/lib/python2.7/site-packages')
        elif platform.system() == 'Darwin':
            print('For example: cp ../../lib/Python27_x64/* /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages')
        sys.exit(1)

    # Prepare the FBX SDK.
    (lSdkManager, lScene) = FbxCommon.InitializeSdkObjects()
    
    # The example can take an output file name as an argument.
    lSampleFileName = ""
    if len(sys.argv) > 1:
        lSampleFileName = sys.argv[1]
    # A default output file name is given otherwise.
    else:
        lSampleFileName = SAVE_FILE_NAME

    # Create the scene.
    lResult = CreateScene(lSdkManager, lScene, lSampleFileName)

    if lResult == False:
        print("\n\nAn error occurred while creating the scene...\n")
        lSdkManager.Destroy()
        sys.exit(1)

    # Save the scene.
    lResult = FbxCommon.SaveScene(lSdkManager, lScene, lSampleFileName)

    if lResult == False:
        print("\n\nAn error occurred while saving the scene...\n")
        lSdkManager.Destroy()
        sys.exit(1)

    # Destroy all objects created by the FBX SDK.
    lSdkManager.Destroy()
   
    sys.exit(0)
