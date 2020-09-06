import maya.cmds as cmds

    
def set_attribute(obj, action=None):
    """action must be one of t, r, s. It is callers responsibility to
    validate the input."""
    cmds.setAttr(obj+'.{}x'.format(action),lock=True)
    cmds.setAttr(obj+'.{}y'.format(action),lock=True)
    cmds.setAttr(obj+'.{}z'.format(action),lock=True)

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
                    set_attribute(sel[i], 't')
                    print 'Connected Translation'
        
        
                            
                            
            elif c=='r':
                for i in sel:
                    set_attribute(sel[i], 'r')
                    print 'Connected Rotation'
                    
                    
                    
            elif c=='s':
                for i in sel:
                    set_attribute(sel[i], 's')
                    print 'Connected Scale'  
                    
            elif c=='a':
                for i in sel:
                    set_attribute(sel[i], 't')
                    set_attribute(sel[i], 'r')
                    set_attribute(sel[i], 's')
                    print 'Connected Scale,Rotation,Translation' 
        else:
            print('No Object Selected')                           
                    
                                
    else:
        if result=='Cancel':
            print 'Nothing Locked'
    
    
lock()
