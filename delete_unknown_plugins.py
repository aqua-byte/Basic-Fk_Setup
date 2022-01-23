import maya.cmds as cmds
plugins=cmds.unknownPlugin(query=True,list=True)   #this will querry and list all the unknown plugins in the scene
if plugins:  #if plugins exists, it will run for loop ,ELSE it will print )
    for i in plugins:
     cmds.unknownPlugin(i,remove=True)
else:
    print('no plugins found')  
