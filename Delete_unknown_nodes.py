import maya.cmds as cmds

unknown_nodes=cmds.ls(type='unknown')  #this will list all the unknown nodes in the scene
if unknown_nodes:   #if unknown nodes exists,it will run below lines from 5.If not else sttement will be run on line 14
    cmds.lockNode(unknown_nodes,lock=False)  #it will unlock the node
    cmds.delete(unknown_nodes) # it will delete the node after unlocking it
    a=cmds.ls(type='unknown')  #it will again list the unknown nodes
    if not a :   # if it doesn't exist now then it will print line 9 otherwise it will go to line 10
        print('All unknown nodes deleted')
    else:    
        print('Unable to delete all nodes')
    
    
else:
    print('no unknown nodes found')
