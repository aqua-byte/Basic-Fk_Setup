##########################################################################################################################################
################################################# CTRL_ZERO_OUT ##########################################################################
##########################################################################################################################################

#Select the Controllers and run the script,it will zero out all the value on the controller(translation,rotation)
#OR
#select nothing and run the script(it will zerout all the ctrls which are ending with *ctrl.


#change the prefix on line 21 accordingly like '*Ctrl' '*Ctl'.
#You can set this as Hotkey as 0 or something very useful to zeroout t s r on ctrls. 




selected_object=cmds.ls(selection=True)

if len(selected_object)==0:
    obj_ending_with_Ctrl=cmds.ls('*Ctrl',an=True)     #an=absolute name

    for i in obj_ending_with_Ctrl:
        try:
            cmds.setAttr(i+'.translateX',0)
        except:
            pass
        try:
            cmds.setAttr(i+'.translateY',0)
        except:
            pass
        
        try:
            cmds.setAttr(i+'.translateZ',0)
        except:
            pass
        try:
            cmds.setAttr(i+'.rotateX',0)
        except:
            pass
        
        try:
            cmds.setAttr(i+'.rotateY',0)
        except:
            pass
        try:
            cmds.setAttr(i+'.rotateZ',0)
        except:
            pass
            
            
        def sczero():
            obj_ending_with_Ctrl=cmds.ls('*Ctrl',an=True)     #when there is no selection 
            
            for i in selected_object:
                
                try:
                    cmds.setAttr(i+'.scaleX',1)
                    
                except:
                    pass
                try:
                    cmds.setAttr(i+'.scaleY',1)
                except:
                    pass
                
                try:
                    cmds.setAttr(i+'.scaleZ',1)
                except:
                    pass    
        sczero()
  

else:
    


    for i in selected_object:
           
        try:
            cmds.setAttr(i+'.translateX',0)
        except:
            pass
        try:
            cmds.setAttr(i+'.translateY',0)
        except:
            pass
        
        try:
            cmds.setAttr(i+'.translateZ',0)
        except:
            pass
        try:
            cmds.setAttr(i+'.rotateX',0)
        except:
            pass
        
        try:
            cmds.setAttr(i+'.rotateY',0)
        except:
            pass
        try:
            cmds.setAttr(i+'.rotateZ',0)
        except:
            pass
            
            
        def scsel():
            
            selected_object=cmds.ls(selection=True)             #when there is selection 
        
            
            for z in selected_object:
                try:
                    cmds.setAttr(i+'.scaleX',1)
                except:
                    pass
                try:
                    cmds.setAttr(i+'.scaleY',1)
                except:
                    pass
                
                try:
                    cmds.setAttr(i+'.scaleZ',1)
                except:
                    pass 
        scsel()
