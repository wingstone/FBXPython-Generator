"""

 Copyright (C) 2001 - 2010 Autodesk, Inc. and/or its licensors.
 All Rights Reserved.

 The coded instructions, statements, computer programs, and/or related material 
 (collectively the "Data") in these files contain unpublished information 
 proprietary to Autodesk, Inc. and/or its licensors, which is protected by 
 Canada and United States of America federal copyright law and by international 
 treaties. 
 
 The Data may not be disclosed or distributed to third parties, in whole or in
 part, without the prior written consent of Autodesk, Inc. ("Autodesk").

 THE DATA IS PROVIDED "AS IS" AND WITHOUT WARRANTY.
 ALL WARRANTIES ARE EXPRESSLY EXCLUDED AND DISCLAIMED. AUTODESK MAKES NO
 WARRANTY OF ANY KIND WITH RESPECT TO THE DATA, EXPRESS, IMPLIED OR ARISING
 BY CUSTOM OR TRADE USAGE, AND DISCLAIMS ANY IMPLIED WARRANTIES OF TITLE, 
 NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE OR USE. 
 WITHOUT LIMITING THE FOREGOING, AUTODESK DOES NOT WARRANT THAT THE OPERATION
 OF THE DATA WILL BE UNINTERRUPTED OR ERROR FREE. 
 
 IN NO EVENT SHALL AUTODESK, ITS AFFILIATES, PARENT COMPANIES, LICENSORS
 OR SUPPLIERS ("AUTODESK GROUP") BE LIABLE FOR ANY LOSSES, DAMAGES OR EXPENSES
 OF ANY KIND (INCLUDING WITHOUT LIMITATION PUNITIVE OR MULTIPLE DAMAGES OR OTHER
 SPECIAL, DIRECT, INDIRECT, EXEMPLARY, INCIDENTAL, LOSS OF PROFITS, REVENUE
 OR DATA, COST OF COVER OR CONSEQUENTIAL LOSSES OR DAMAGES OF ANY KIND),
 HOWEVER CAUSED, AND REGARDLESS OF THE THEORY OF LIABILITY, WHETHER DERIVED
 FROM CONTRACT, TORT (INCLUDING, BUT NOT LIMITED TO, NEGLIGENCE), OR OTHERWISE,
 ARISING OUT OF OR RELATING TO THE DATA OR ITS USE OR ANY OTHER PERFORMANCE,
 WHETHER OR NOT AUTODESK HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH LOSS
 OR DAMAGE. 
 
"""

from DisplayModule.DisplayCommon import *
#from fbx import FbxCamera

def DisplayLodGroup(pNode):
    lDisplayLevels = [ "UseLOD", "Show", "Hide" ] 

    DisplayString("LodGroup Name: ", pNode.GetName())

    DisplayInt("    ", pNode.GetChildCount(), " Geometries")
    for i in range(pNode.GetChildCount()):
        lChildNode = pNode.GetChild(i)
        DisplayString("        ", lChildNode.GetName())

    lLodGroupAttr = pNode.GetNodeAttribute()
    DisplayBool("    MinMaxDistance Enabled: ", lLodGroupAttr.MinMaxDistance.Get())
    if lLodGroupAttr.MinMaxDistance.Get():
        DisplayDouble("        Min Distance: ", lLodGroupAttr.MinDistance.Get())
        DisplayDouble("        Max Distance: ", lLodGroupAttr.MaxDistance.Get())
    DisplayBool("    Is World Space: ", lLodGroupAttr.WorldSpace.Get())

    DisplayString("    Thresholds ")
    for i in range(lLodGroupAttr.GetNumThresholds()):
        if lLodGroupAttr.GetThreshold(i, lThreshVal):
            DisplayDouble("        ", lThreshVal.value())

    DisplayString("    DisplayLevels")
    for i in range(lLodGroupAttr.GetNumDisplayLevels()):
        res, lLevel = lLodGroupAttr.GetDisplayLevel(i)
        if res:
            DisplayString("        ", lDisplayLevels[lLevel])
