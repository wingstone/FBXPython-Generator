import sys
import math
from DisplayModule.DisplayGlobalSettings  import *
from DisplayModule.DisplayHierarchy       import DisplayHierarchy
from DisplayModule.DisplayMarker          import DisplayMarker
from DisplayModule.DisplayMesh            import DisplayMesh
from DisplayModule.DisplayUserProperties  import DisplayUserProperties
from DisplayModule.DisplayPivotsAndLimits import DisplayPivotsAndLimits
from DisplayModule.DisplaySkeleton        import DisplaySkeleton
from DisplayModule.DisplayNurb            import DisplayNurb
from DisplayModule.DisplayPatch           import DisplayPatch
from DisplayModule.DisplayCamera          import DisplayCamera
from DisplayModule.DisplayLight           import DisplayLight
from DisplayModule.DisplayLodGroup        import DisplayLodGroup
from DisplayModule.DisplayPose            import DisplayPose
from DisplayModule.DisplayAnimation       import DisplayAnimation
from DisplayModule.DisplayGenericInfo     import DisplayGenericInfo

def DisplayContent(pScene):
    lNode = pScene.GetRootNode()

    if lNode:
        for i in range(lNode.GetChildCount()):
            DisplayNodeContent(lNode.GetChild(i))

def DisplayTarget(pNode):
    if pNode.GetTarget():
        DisplayString("    Target Name: ", pNode.GetTarget().GetName())

def ProcessMesh(pNode):
    lMesh = pNode.GetNodeAttribute ()
    DisplayString("Mesh Name: ", pNode.GetName())
    
    # lPolygonCount = lMesh.GetPolygonCount()
    # lControlPoints = lMesh.GetControlPoints() 
    # for i in range(lPolygonCount):
    #     lPolygonSize = lMesh.GetPolygonSize(i)

    #     for j in range(lPolygonSize):
    #         lControlPointIndex = lMesh.GetPolygonVertex(i, j)
    #         Display3DVector("            Coordinates: ", lControlPoints[lControlPointIndex])

def DisplayNodeContent(pNode):
    if pNode.GetNodeAttribute() == None:
        print("NULL Node Attribute\n")
    else:
        lAttributeType = (pNode.GetNodeAttribute().GetAttributeType())

        if lAttributeType == FbxNodeAttribute.eMesh:
            DisplayMesh(pNode)
        
    DisplayTarget(pNode)

    for i in range(pNode.GetChildCount()):
        DisplayNodeContent(pNode.GetChild(i))

if __name__ == "__main__":
    try:
        from FbxCommon import *
        from fbx import *
    except ImportError:
        print("Error: module FbxCommon and/or fbx failed to import.\n")
        sys.exit(1)

    # Prepare the FBX SDK.
    (lSdkManager, lScene) = InitializeSdkObjects()

    # The example can take a FBX file as an argument.
    if len(sys.argv) > 1:
        print("\n\nFile: %s\n" % sys.argv[1])
        lResult = LoadScene(lSdkManager, lScene, sys.argv[1])
    else :
        lResult = False
        print("\n\nUsage: ImportScene <FBX file name>\n")

    if not lResult:
        print("\n\nAn error occurred while loading the scene...")
    else :
        # todo process model
        DisplayContent(lScene)

    # Save the scene.
    # The example can take an output file name as an argument.
    if len(sys.argv) > 2:
        lResult = SaveScene(lSdkManager, lScene, sys.argv[2])
    # A default output file name is given otherwise.
    else:
        lResult = SaveScene(lSdkManager, lScene, sys.argv[1])

    if lResult == False:
        print("\n\nAn error occurred while saving the scene...\n")
        lSdkManager.Destroy()
        sys.exit(1)

    # Destroy all objects created by the FBX SDK.
    lSdkManager.Destroy()
   
    sys.exit(0)
