########################################################################################################################################
##################################################### LOCK #############################################################################
########################################################################################################################################

import maya.cmds as cmds

def lock():
    

    result = cmds.promptDialog(
                    title='Lock',
                    message='Enter the attribute:'
                            't for trans,r for rot,s for scale,a for all', 
                    button=['OK', 'Cancel'],
                    defaultButton='OK',
                    cancelButton='Cancel',
                    dismissString='Cancel')
    
    if result == 'OK':
        text = cmds.promptDialog(query=True, text=True)
        sel=cmds.ls(selection=True)
        sel_size=len(sel)
        if sel_size>0:
            c=str(text)
             
            if c=='t':
                for i in sel:
                    cmds.setAttr((i+'.tx'),lock=True)
                    cmds.setAttr((i+'.ty'),lock=True)
                    cmds.setAttr((i+'.tz'),lock=True)
                    print 'Connected Translation'
        
        
                            
                            
            elif c=='r':
                sel=cmds.ls(selection=True)
                for i in sel:
                    cmds.setAttr((i+'.rx'),lock=True)
                    cmds.setAttr((i+'.ry'),lock=True)
                    cmds.setAttr((i+'.rz'),lock=True)
                    print 'Connected Rotation'
                    
                    
                    
            elif c=='s':
                sel=cmds.ls(selection=True)
                for i in sel:
                    cmds.setAttr((i+'.sx'),lock=True)
                    cmds.setAttr((i+'.sy'),lock=True)
                    cmds.setAttr((i+'.sz'),lock=True)
                    print 'Connected Scale'  
                    
            elif c=='a':
                sel=cmds.ls(selection=True)
                for i in sel:
                    cmds.setAttr((i+'.sx'),lock=True)
                    cmds.setAttr((i+'.sy'),lock=True)
                    cmds.setAttr((i+'.sz'),lock=True)
                    cmds.setAttr((i+'.rx'),lock=True)
                    cmds.setAttr((i+'.ry'),lock=True)
                    cmds.setAttr((i+'.rz'),lock=True)
                    cmds.setAttr((i+'.tx'),lock=True)
                    cmds.setAttr((i+'.ty'),lock=True)
                    cmds.setAttr((i+'.tz'),lock=True)
                    print 'Connected Scale,Rotation,Translation' 
        else:
            print('No Object Selected')                           
                    
                                
    else:
        if result=='Cancel':
            print 'Nothing Locked'
    
    
lock()    
    
    
           
    
