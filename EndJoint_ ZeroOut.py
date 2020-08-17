###############################################################################################################
###################################   EndJoint_Orient_ZeroOut   ###############################################
###############################################################################################################
#Author:Himanshi Ahuja
#Email:himansheeahuja@gmail.com

#Orient X,Y,Z will be zeroed out of evey end joint in the hierarchy.
#You only have to selet the root joint.
#Make sure all your end joints the hierarchy have 'end' word in the joint name.




Selected_joints = cmds.listRelatives(allDescendents=True, type='joint')


empty_list=[]
for i in Selected_joints:
    if 'end'in i.lower():
        empty_list.append(i)
        cmds.setAttr(i+'.jointOrientX',0)
        cmds.setAttr(i+'.jointOrientY',0)
        cmds.setAttr(i+'.jointOrientZ',0)
else:
    print'No End Joint found'

print empty_list
