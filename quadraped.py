

import maya.cmds as cmds

''' place locators to define rig shape '''
def bluecon(s):
    cmds.setAttr(s+'.overrideEnabled',1)
    cmds.setAttr(s+'.overrideColor',15)
def yellowcon(s):
    cmds.setAttr(s+'.overrideEnabled',1)
    cmds.setAttr(s+'.overrideColor',17)
def redcon(s):
    cmds.setAttr(s+'.overrideEnabled',1)
    cmds.setAttr(s+'.overrideColor',13)
def lockTranslate(s):
    cmds.setAttr(s+'.tx',k=False,l=True)
    cmds.setAttr(s+'.ty',k=False,l=True)
    cmds.setAttr(s+'.tz',k=False,l=True)
def lockScale(s):
    cmds.setAttr(s+'.sx',k=False,l=True)
    cmds.setAttr(s+'.sy',k=False,l=True)
    cmds.setAttr(s+'.sz',k=False,l=True)
def lockRotate(s):
    cmds.setAttr(s+'.rx',k=False,l=True)
    cmds.setAttr(s+'.ry',k=False,l=True)
    cmds.setAttr(s+'.rz',k=False,l=True)

hindToe=cmds.spaceLocator(n='l_hindToe_LOC')
cmds.setAttr(hindToe[0]+'.translateX',12)
cmds.setAttr(hindToe[0]+'.translateZ',-20)
bluecon(hindToe[0])
hindAnkle=cmds.spaceLocator(n='l_hindAnkle_LOC')
cmds.setAttr(hindAnkle[0]+'.translateX',12)
cmds.setAttr(hindAnkle[0]+'.translateY',5)
cmds.setAttr(hindAnkle[0]+'.translateZ',-23)
bluecon(hindAnkle[0])
hindKnee=cmds.spaceLocator(n='l_hindKnee_LOC')
cmds.setAttr(hindKnee[0]+'.translateX',12)
cmds.setAttr(hindKnee[0]+'.translateY',25)
cmds.setAttr(hindKnee[0]+'.translateZ',-28)
bluecon(hindKnee[0])
hindUpperKnee=cmds.spaceLocator(n='l_hindUpperKnee_LOC')
cmds.setAttr(hindUpperKnee[0]+'.translateX',12)
cmds.setAttr(hindUpperKnee[0]+'.translateY',36)
cmds.setAttr(hindUpperKnee[0]+'.translateZ',-19)
bluecon(hindUpperKnee[0])
hindFemur=cmds.spaceLocator(n='l_hindFemur_LOC')
cmds.setAttr(hindFemur[0]+'.translateX',12)
cmds.setAttr(hindFemur[0]+'.translateY',50)
cmds.setAttr(hindFemur[0]+'.translateZ',-25)
bluecon(hindFemur[0])
hindPelvis=cmds.spaceLocator(n='l_hindPelvis_LOC')
cmds.setAttr(hindPelvis[0]+'.translateY',54)
cmds.setAttr(hindPelvis[0]+'.translateZ',-24)
yellowcon(hindPelvis[0])

hindLocGrp=cmds.group(hindToe,hindAnkle,hindKnee,hindUpperKnee,hindFemur,hindPelvis,n='hindPlacement_GRP')

''' front leg locator placement '''
frontToe=cmds.spaceLocator(n='l_frontToe_LOC')
cmds.setAttr(frontToe[0]+'.translateX',12)
cmds.setAttr(frontToe[0]+'.translateZ',24)
bluecon(frontToe[0])
frontAnkle=cmds.spaceLocator(n='l_frontAnkle_LOC')
cmds.setAttr(frontAnkle[0]+'.translateX',12)
cmds.setAttr(frontAnkle[0]+'.translateY',5)
cmds.setAttr(frontAnkle[0]+'.translateZ',21)
bluecon(frontAnkle[0])
frontKnee=cmds.spaceLocator(n='l_frontKnee_LOC')
cmds.setAttr(frontKnee[0]+'.translateX',12)
cmds.setAttr(frontKnee[0]+'.translateY',25)
cmds.setAttr(frontKnee[0]+'.translateZ',24)
bluecon(frontKnee[0])
frontUpperKnee=cmds.spaceLocator(n='l_frontUpperKnee_LOC')
cmds.setAttr(frontUpperKnee[0]+'.translateX',12)
cmds.setAttr(frontUpperKnee[0]+'.translateY',36)
cmds.setAttr(frontUpperKnee[0]+'.translateZ',18)
bluecon(frontUpperKnee[0])
frontFemur=cmds.spaceLocator(n='l_frontFemur_LOC')
cmds.setAttr(frontFemur[0]+'.translateX',12)
cmds.setAttr(frontFemur[0]+'.translateY',44)
cmds.setAttr(frontFemur[0]+'.translateZ',25)
bluecon(frontFemur[0])
frontPelvis=cmds.spaceLocator(n='l_frontPelvis_LOC')
cmds.setAttr(frontPelvis[0]+'.translateY',54)
cmds.setAttr(frontPelvis[0]+'.translateZ',20)
yellowcon(frontPelvis[0])
frontLocGrp=cmds.group(frontToe,frontAnkle,frontKnee,frontUpperKnee,frontFemur,frontPelvis,n='frontPlacement_GRP')
''' neck loc placement '''
neckRoot=cmds.spaceLocator(n='neckRoot_LOC')
cmds.setAttr(neckRoot[0]+'.translateY',48)
cmds.setAttr(neckRoot[0]+'.translateZ',30)
yellowcon(neckRoot[0])
neckEnd=cmds.spaceLocator(n='neckEnd_LOC')
cmds.setAttr(neckEnd[0]+'.translateY',58)
cmds.setAttr(neckEnd[0]+'.translateZ',50)
yellowcon(neckEnd[0])
neckLocGrp=cmds.group(neckRoot,neckEnd,n='neckPlacement_GRP')
''' tail '''
tail1=cmds.spaceLocator(n='tailRoot_LOC')
cmds.setAttr(tail1[0]+'.translateY',54)
cmds.setAttr(tail1[0]+'.translateZ',-32)
yellowcon(tail1[0])
tail2=cmds.spaceLocator(n='tailEnd_LOC')
cmds.setAttr(tail2[0]+'.translateY',54)
cmds.setAttr(tail2[0]+'.translateZ',-62)
yellowcon(tail2[0])
tailLocGrp=cmds.group(tail1,tail2,n='tailPlacement_GRP')
''' finalize placement loc module '''
mainLocGrp=cmds.group(tailLocGrp,neckLocGrp,frontLocGrp,hindLocGrp,n='mainPlacementLoc_GRP')



''' build rig '''
''' build rig '''
''' worldController '''
world=cmds.curve(d=1,p=[(-5.472546,0, 1.778139),(-5.472546,0,-1.778137),(-4.655226,0,-3.382219),(-3.38222,0,-4.655226),(-1.778138,0,-5.472547),(1.778139,0,-5.472547),(3.382222,0,-4.655227),(4.655229,0,-3.38222),(5.47255,0,-1.778138),(5.472546,0,1.778139),(4.655226,0,3.382221),(3.38222,0,4.655227),(1.778138,0,5.472547),(-1.778137,0,5.472547),(-3.382219,0,4.655227),(-4.655226,0,3.382221),(-5.472546,0,1.778139)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],n='c_World_CTRL')
subworld=cmds.curve(d=1,p=[(-5.472546,0, 1.778139),(-5.472546,0,-1.778137),(-4.655226,0,-3.382219),(-3.38222,0,-4.655226),(-1.778138,0,-5.472547),(1.778139,0,-5.472547),(3.382222,0,-4.655227),(4.655229,0,-3.38222),(5.47255,0,-1.778138),(5.472546,0,1.778139),(4.655226,0,3.382221),(3.38222,0,4.655227),(1.778138,0,5.472547),(-1.778137,0,5.472547),(-3.382219,0,4.655227),(-4.655226,0,3.382221),(-5.472546,0,1.778139)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],n='c_SubWorld_CTRL')
cmds.scale(.7,.7,.7,subworld+'.cv[0:16]')
forward=cmds.curve(d=1, p=[(1.778138,0,5.472547),(6.55294e-07,0,8.059775),(-1.778137,0,5.472547)], k=(0,1,2),n='worldForward')
backward=cmds.curve(d=1, p=[(-1.778138,0,-5.472547),(8.61953e-07,0,-6.934346),(1.778139,0,-5.472547)], k=(0,1,2),n='worldBackward')
worldleft=cmds.curve(d=1, p=[(5.47255,0,-1.778138),(6.934345,0,1.43659e-06),(5.472546,0,1.778139)], k=(0,1,2),n='worldRight')
worldright=cmds.curve(d=1, p=[(-5.472546,0,-1.778137),(-6.934345,0,1.43659e-06),(-5.472546,0,1.778139)],k=(0,1,2),n='worldLeft')
mainshape=cmds.listRelatives(world,s=True)
cmds.rename(mainshape,'worldShape')
forwardshape=cmds.listRelatives(forward,s=True)
forwardshape=cmds.rename(forwardshape,'worldForwardShape')
backwardshape=cmds.listRelatives(backward,s=True)
backwardshape=cmds.rename(backwardshape,'worldBackwardShape')
worldleftshape=cmds.listRelatives(worldleft,s=True)
worldleftshape=cmds.rename(worldleftshape,'worldLeftShape')
worldrightshape=cmds.listRelatives(worldright,s=True)
worldrightshape=cmds.rename(worldrightshape,'worldRightShape')
subshape=cmds.listRelatives(subworld,s=True)
subshape=cmds.rename(subshape,'subWorldShape')
cmds.parent(forwardshape,world,s=True,r=True)
cmds.parent(worldleftshape,world,s=True,r=True)
cmds.parent(worldrightshape,world,s=True,r=True)
cmds.parent(backwardshape,world,s=True,r=True)
cmds.delete(forward,backward,worldleft,worldright)
cmds.parent(subworld,world)
yellowcon(world)
bluecon(worldleftshape)
redcon(worldrightshape)

''' create legs module '''
''' create legs module '''
''' hind legs '''
# joints
hindPelvisJnt=cmds.joint(n='c_hindPelvis_JNT')
yellowcon(hindPelvisJnt)
constr=cmds.pointConstraint(hindPelvis,hindPelvisJnt)
cmds.delete(constr)
cmds.select(d=True)
L_hindToeJnt=cmds.joint(n='l_hindToe_JNT')
constr=cmds.pointConstraint(hindToe,L_hindToeJnt)
cmds.delete(constr)
cmds.select(d=True)
L_hindAnkleJnt=cmds.joint(n='l_hindAnkle_JNT')
constr=cmds.pointConstraint(hindAnkle,L_hindAnkleJnt)
cmds.delete(constr)
cmds.select(d=True)
L_hindKneeJnt=cmds.joint(n='l_KneeAnkle_JNT')
constr=cmds.pointConstraint(hindKnee,L_hindKneeJnt)
cmds.delete(constr)
cmds.select(d=True)
L_hindUpperKneeJnt=cmds.joint(n='l_hindUpperKnee_JNT')
constr=cmds.pointConstraint(hindUpperKnee,L_hindUpperKneeJnt)
cmds.delete(constr)
cmds.select(d=True)
L_hindFemurJnt=cmds.joint(n='l_hindFemur_JNT')
constr=cmds.pointConstraint(hindFemur,L_hindFemurJnt)
cmds.delete(constr)
cmds.select(d=True)

# mirror to other side...
R_hindToeJnt=cmds.duplicate(L_hindToeJnt,n='r_hindToe_JNT')
xPos=cmds.getAttr(L_hindToeJnt+'.tx')
cmds.setAttr(R_hindToeJnt[0]+'.tx',-xPos)
R_hindAnkleJnt=cmds.duplicate(L_hindAnkleJnt,n='r_hindAnkle_JNT')
xPos=cmds.getAttr(L_hindAnkleJnt+'.tx')
cmds.setAttr(R_hindAnkleJnt[0]+'.tx',-xPos)
R_hindKneeJnt=cmds.duplicate(L_hindKneeJnt,n='r_hindKnee_JNT')
xPos=cmds.getAttr(L_hindKneeJnt+'.tx')
cmds.setAttr(R_hindKneeJnt[0]+'.tx',-xPos)
R_hindUpperKneeJnt=cmds.duplicate(L_hindUpperKneeJnt,n='r_hindUpperKnee_JNT')
xPos=cmds.getAttr(L_hindUpperKneeJnt+'.tx')
cmds.setAttr(R_hindUpperKneeJnt[0]+'.tx',-xPos)
R_hindFemurJnt=cmds.duplicate(L_hindFemurJnt,n='r_hindFemur_JNT')
xPos=cmds.getAttr(L_hindFemurJnt+'.tx')
cmds.setAttr(R_hindFemurJnt[0]+'.tx',-xPos)

# end joints for mayaSkinning...
L_hindToeEndJnt=cmds.joint(n='l_hindToeEnd_JNT')
constr=cmds.pointConstraint(hindToe,L_hindToeEndJnt)
cmds.delete(constr)
cmds.parent(L_hindToeEndJnt,L_hindToeJnt)
cmds.setAttr(L_hindToeEndJnt+'.tz',.04)
cmds.setAttr(L_hindToeEndJnt+'.visibility',0)
cmds.select(d=True)
R_hindToeEndJnt=cmds.joint(n='r_hindToeEnd_JNT')
cmds.parent(R_hindToeEndJnt,R_hindToeJnt,r=True)
cmds.setAttr(R_hindToeEndJnt+'.tz',.04)
cmds.setAttr(R_hindToeEndJnt+'.visibility',0)
cmds.select(d=True)

# parent hind leg joints...
cmds.parent(L_hindToeJnt,L_hindAnkleJnt)
cmds.parent(L_hindAnkleJnt,L_hindKneeJnt)
cmds.parent(L_hindKneeJnt,L_hindUpperKneeJnt)
cmds.parent(L_hindUpperKneeJnt,L_hindFemurJnt)
cmds.parent(L_hindFemurJnt,hindPelvisJnt)
cmds.parent(R_hindToeJnt,R_hindAnkleJnt)
cmds.parent(R_hindAnkleJnt,R_hindKneeJnt)
cmds.parent(R_hindKneeJnt,R_hindUpperKneeJnt)
cmds.parent(R_hindUpperKneeJnt,R_hindFemurJnt)
cmds.parent(R_hindFemurJnt,hindPelvisJnt)

# orient joints
cmds.select(L_hindFemurJnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_hindFemurJnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)

''' IK hind legs '''
L_hindToeJntIk=cmds.joint(n='l_hindToeIK_JNT')
constr=cmds.pointConstraint(hindToe,L_hindToeJntIk)
cmds.delete(constr)
cmds.select(d=True)
L_hindAnkleJntIk=cmds.joint(n='l_hindAnkleIK_JNT')
constr=cmds.pointConstraint(hindAnkle,L_hindAnkleJntIk)
cmds.delete(constr)
cmds.select(d=True)
L_hindKneeJntIk=cmds.joint(n='l_KneeAnkleIK_JNT')
constr=cmds.pointConstraint(hindKnee,L_hindKneeJntIk)
cmds.delete(constr)
cmds.select(d=True)
L_hindUpperKneeJntIk=cmds.joint(n='l_hindUpperKneeIK_JNT')
constr=cmds.pointConstraint(hindUpperKnee,L_hindUpperKneeJntIk)
cmds.delete(constr)
cmds.select(d=True)
L_hindFemurJntIk=cmds.joint(n='l_hindFemurIK_JNT')
constr=cmds.pointConstraint(hindFemur,L_hindFemurJntIk)
cmds.delete(constr)
cmds.select(d=True)

# mirror to other side...
R_hindToeJntIk=cmds.duplicate(L_hindToeJntIk,n='r_hindToeIK_JNT')
R_hindToeJntIk=R_hindToeJntIk[0]
xPos=cmds.getAttr(L_hindToeJntIk+'.tx')
cmds.setAttr(R_hindToeJntIk+'.tx',-xPos)
R_hindAnkleJntIk=cmds.duplicate(L_hindAnkleJntIk,n='r_hindAnkleIK_JNT')
R_hindAnkleJntIk=R_hindAnkleJntIk[0]
xPos=cmds.getAttr(L_hindAnkleJntIk+'.tx')
cmds.setAttr(R_hindAnkleJntIk+'.tx',-xPos)
R_hindKneeJntIk=cmds.duplicate(L_hindKneeJntIk,n='r_hindKneeIK_JNT')
R_hindKneeJntIk=R_hindKneeJntIk[0]
xPos=cmds.getAttr(L_hindKneeJntIk+'.tx')
cmds.setAttr(R_hindKneeJntIk+'.tx',-xPos)
R_hindUpperKneeJntIk=cmds.duplicate(L_hindUpperKneeJntIk,n='r_hindUpperKneeIK_JNT')
R_hindUpperKneeJntIk=R_hindUpperKneeJntIk[0]
xPos=cmds.getAttr(L_hindUpperKneeJntIk+'.tx')
cmds.setAttr(R_hindUpperKneeJntIk+'.tx',-xPos)
R_hindFemurJntIk=cmds.duplicate(L_hindFemurJntIk,n='r_hindFemurIK_JNT')
R_hindFemurJntIk=R_hindFemurJntIk[0]
xPos=cmds.getAttr(L_hindFemurJntIk+'.tx')
cmds.setAttr(R_hindFemurJntIk+'.tx',-xPos)

# parent hind leg joints...
cmds.parent(L_hindToeJntIk,L_hindAnkleJntIk)
cmds.parent(L_hindAnkleJntIk,L_hindKneeJntIk)
cmds.parent(L_hindKneeJntIk,L_hindUpperKneeJntIk)
cmds.parent(L_hindUpperKneeJntIk,L_hindFemurJntIk)
cmds.parent(L_hindFemurJntIk,hindPelvisJnt)
cmds.parent(R_hindToeJntIk,R_hindAnkleJntIk)
cmds.parent(R_hindAnkleJntIk,R_hindKneeJntIk)
cmds.parent(R_hindKneeJntIk,R_hindUpperKneeJntIk)
cmds.parent(R_hindUpperKneeJntIk,R_hindFemurJntIk)
cmds.parent(R_hindFemurJntIk,hindPelvisJnt)

# orient joints
cmds.select(L_hindFemurJntIk)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_hindFemurJntIk)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)

''' Fk hind legs '''
L_hindToeJntFk=cmds.joint(n='l_hindToeFk_JNT')
constr=cmds.pointConstraint(hindToe,L_hindToeJntFk)
cmds.delete(constr)
cmds.select(d=True)
L_hindAnkleJntFk=cmds.joint(n='l_hindAnkleFk_JNT')
constr=cmds.pointConstraint(hindAnkle,L_hindAnkleJntFk)
cmds.delete(constr)
cmds.select(d=True)
L_hindKneeJntFk=cmds.joint(n='l_KneeAnkleFk_JNT')
constr=cmds.pointConstraint(hindKnee,L_hindKneeJntFk)
cmds.delete(constr)
cmds.select(d=True)
L_hindUpperKneeJntFk=cmds.joint(n='l_hindUpperKneeFk_JNT')
constr=cmds.pointConstraint(hindUpperKnee,L_hindUpperKneeJntFk)
cmds.delete(constr)
cmds.select(d=True)
L_hindFemurJntFk=cmds.joint(n='l_hindFemurFk_JNT')
constr=cmds.pointConstraint(hindFemur,L_hindFemurJntFk)
cmds.delete(constr)
cmds.select(d=True)

# mirror to other side...
R_hindToeJntFk=cmds.duplicate(L_hindToeJntFk,n='r_hindToeFk_JNT')
xPos=cmds.getAttr(L_hindToeJntFk+'.tx')
R_hindToeJntFk=R_hindToeJntFk[0]
cmds.setAttr(R_hindToeJntFk+'.tx',-xPos)
R_hindAnkleJntFk=cmds.duplicate(L_hindAnkleJntFk,n='r_hindAnkleFk_JNT')
xPos=cmds.getAttr(L_hindAnkleJntFk+'.tx')
R_hindAnkleJntFk=R_hindAnkleJntFk[0]
cmds.setAttr(R_hindAnkleJntFk+'.tx',-xPos)
R_hindKneeJntFk=cmds.duplicate(L_hindKneeJntFk,n='r_hindKneeFk_JNT')
xPos=cmds.getAttr(L_hindKneeJntFk+'.tx')
R_hindKneeJntFk=R_hindKneeJntFk[0]
cmds.setAttr(R_hindKneeJntFk+'.tx',-xPos)
R_hindUpperKneeJntFk=cmds.duplicate(L_hindUpperKneeJntFk,n='r_hindUpperKneeFk_JNT')
xPos=cmds.getAttr(L_hindUpperKneeJntFk+'.tx')
R_hindUpperKneeJntFk=R_hindUpperKneeJntFk[0]
cmds.setAttr(R_hindUpperKneeJntFk+'.tx',-xPos)
R_hindFemurJntFk=cmds.duplicate(L_hindFemurJntFk,n='r_hindFemurFk_JNT')
xPos=cmds.getAttr(L_hindFemurJntFk+'.tx')
R_hindFemurJntFk=R_hindFemurJntFk[0]
cmds.setAttr(R_hindFemurJntFk+'.tx',-xPos)

# parent hind leg joints...
cmds.parent(L_hindToeJntFk,L_hindAnkleJntFk)
cmds.parent(L_hindAnkleJntFk,L_hindKneeJntFk)
cmds.parent(L_hindKneeJntFk,L_hindUpperKneeJntFk)
cmds.parent(L_hindUpperKneeJntFk,L_hindFemurJntFk)
cmds.parent(L_hindFemurJntFk,hindPelvisJnt)

cmds.parent(R_hindToeJntFk,R_hindAnkleJntFk)
cmds.parent(R_hindAnkleJntFk,R_hindKneeJntFk)
cmds.parent(R_hindKneeJntFk,R_hindUpperKneeJntFk)
cmds.parent(R_hindUpperKneeJntFk,R_hindFemurJntFk)
cmds.parent(R_hindFemurJntFk,hindPelvisJnt)

# orient joints
cmds.select(L_hindFemurJntFk)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_hindFemurJntFk)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)

''' front legs '''
# joints
frontPelvisJnt=cmds.joint(n='c_frontPelvis_JNT')
yellowcon(frontPelvisJnt)
constr=cmds.pointConstraint(frontPelvis,frontPelvisJnt)
cmds.delete(constr)
cmds.select(d=True)
L_frontToeJnt=cmds.joint(n='l_frontToe_JNT')
constr=cmds.pointConstraint(frontToe,L_frontToeJnt)
cmds.delete(constr)
cmds.select(d=True)
L_frontAnkleJnt=cmds.joint(n='l_frontAnkle_JNT')
constr=cmds.pointConstraint(frontAnkle,L_frontAnkleJnt)
cmds.delete(constr)
cmds.select(d=True)
L_frontKneeJnt=cmds.joint(n='l_frontKneeAnkle_JNT')
constr=cmds.pointConstraint(frontKnee,L_frontKneeJnt)
cmds.delete(constr)
cmds.select(d=True)
L_frontUpperKneeJnt=cmds.joint(n='l_frontUpperKnee_JNT')
constr=cmds.pointConstraint(frontUpperKnee,L_frontUpperKneeJnt)
cmds.delete(constr)
cmds.select(d=True)
L_frontFemurJnt=cmds.joint(n='l_frontFemur_JNT')
constr=cmds.pointConstraint(frontFemur,L_frontFemurJnt)
cmds.delete(constr)
cmds.select(d=True)

# mirror to other side...
R_frontToeJnt=cmds.duplicate(L_frontToeJnt,n='r_frontToe_JNT')
xPos=cmds.getAttr(L_frontToeJnt+'.tx')
R_frontToeJnt=R_frontToeJnt[0]
cmds.setAttr(R_frontToeJnt+'.tx',-xPos)
R_frontAnkleJnt=cmds.duplicate(L_frontAnkleJnt,n='r_frontAnkle_JNT')
xPos=cmds.getAttr(L_frontAnkleJnt+'.tx')
R_frontAnkleJnt=R_frontAnkleJnt[0]
cmds.setAttr(R_frontAnkleJnt+'.tx',-xPos)
R_frontKneeJnt=cmds.duplicate(L_frontKneeJnt,n='r_frontKnee_JNT')
xPos=cmds.getAttr(L_frontKneeJnt+'.tx')
R_frontKneeJnt=R_frontKneeJnt[0]
cmds.setAttr(R_frontKneeJnt+'.tx',-xPos)
R_frontUpperKneeJnt=cmds.duplicate(L_frontUpperKneeJnt,n='r_frontUpperKnee_JNT')
xPos=cmds.getAttr(L_frontUpperKneeJnt+'.tx')
R_frontUpperKneeJnt=R_frontUpperKneeJnt[0]
cmds.setAttr(R_frontUpperKneeJnt+'.tx',-xPos)
R_frontFemurJnt=cmds.duplicate(L_frontFemurJnt,n='r_frontFemur_JNT')
xPos=cmds.getAttr(L_frontFemurJnt+'.tx')
R_frontFemurJnt=R_frontFemurJnt[0]
cmds.setAttr(R_frontFemurJnt+'.tx',-xPos)

# end joints for mayaSkinning...
L_frontToeEndJnt=cmds.joint(n='l_frontToeEnd_JNT')
constr=cmds.pointConstraint(frontToe,L_frontToeEndJnt)
cmds.delete(constr)
cmds.parent(L_frontToeEndJnt,L_frontToeJnt)
cmds.setAttr(L_frontToeEndJnt+'.tz',.04)
cmds.setAttr(L_frontToeEndJnt+'.visibility',0)
cmds.select(d=True)
R_frontToeEndJnt=cmds.joint(n='r_frontToeEnd_JNT')
cmds.parent(R_frontToeEndJnt,R_frontToeJnt,r=True)
cmds.setAttr(R_frontToeEndJnt+'.tz',.04)
cmds.setAttr(R_frontToeEndJnt+'.visibility',0)
cmds.select(d=True)

# parent front leg joints...
cmds.parent(L_frontToeJnt,L_frontAnkleJnt)
cmds.parent(L_frontAnkleJnt,L_frontKneeJnt)
cmds.parent(L_frontKneeJnt,L_frontUpperKneeJnt)
cmds.parent(L_frontUpperKneeJnt,L_frontFemurJnt)
cmds.parent(L_frontFemurJnt,frontPelvisJnt)
cmds.parent(R_frontToeJnt,R_frontAnkleJnt)
cmds.parent(R_frontAnkleJnt,R_frontKneeJnt)
cmds.parent(R_frontKneeJnt,R_frontUpperKneeJnt)
cmds.parent(R_frontUpperKneeJnt,R_frontFemurJnt)
cmds.parent(R_frontFemurJnt,frontPelvisJnt)

# orient joints
cmds.select(L_frontFemurJnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_frontFemurJnt)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)

''' IK front legs '''
L_frontToeJntIk=cmds.joint(n='l_frontToeIK_JNT')
constr=cmds.pointConstraint(frontToe,L_frontToeJntIk)
cmds.delete(constr)
cmds.select(d=True)
L_frontAnkleJntIk=cmds.joint(n='l_frontAnkleIK_JNT')
constr=cmds.pointConstraint(frontAnkle,L_frontAnkleJntIk)
cmds.delete(constr)
cmds.select(d=True)
L_frontKneeJntIk=cmds.joint(n='l_frontKneeAnkleIK_JNT')
constr=cmds.pointConstraint(frontKnee,L_frontKneeJntIk)
cmds.delete(constr)
cmds.select(d=True)
L_frontUpperKneeJntIk=cmds.joint(n='l_frontUpperKneeIK_JNT')
constr=cmds.pointConstraint(frontUpperKnee,L_frontUpperKneeJntIk)
cmds.delete(constr)
cmds.select(d=True)
L_frontFemurJntIk=cmds.joint(n='l_frontFemurIK_JNT')
constr=cmds.pointConstraint(frontFemur,L_frontFemurJntIk)
cmds.delete(constr)
cmds.select(d=True)

# mirror to other side...
R_frontToeJntIk=cmds.duplicate(L_frontToeJntIk,n='r_frontToeIK_JNT')
xPos=cmds.getAttr(L_frontToeJntIk+'.tx')
R_frontToeJntIk=R_frontToeJntIk[0]
cmds.setAttr(R_frontToeJntIk+'.tx',-xPos)
R_frontAnkleJntIk=cmds.duplicate(L_frontAnkleJntIk,n='r_frontAnkleIK_JNT')
xPos=cmds.getAttr(L_frontAnkleJntIk+'.tx')
R_frontAnkleJntIk=R_frontAnkleJntIk[0]
cmds.setAttr(R_frontAnkleJntIk+'.tx',-xPos)
R_frontKneeJntIk=cmds.duplicate(L_frontKneeJntIk,n='r_frontKneeIK_JNT')
xPos=cmds.getAttr(L_frontKneeJntIk+'.tx')
R_frontKneeJntIk=R_frontKneeJntIk[0]
cmds.setAttr(R_frontKneeJntIk+'.tx',-xPos)
R_frontUpperKneeJntIk=cmds.duplicate(L_frontUpperKneeJntIk,n='r_frontUpperKneeIK_JNT')
xPos=cmds.getAttr(L_frontUpperKneeJntIk+'.tx')
R_frontUpperKneeJntIk=R_frontUpperKneeJntIk[0]
cmds.setAttr(R_frontUpperKneeJntIk+'.tx',-xPos)
R_frontFemurJntIk=cmds.duplicate(L_frontFemurJntIk,n='r_frontFemurIK_JNT')
xPos=cmds.getAttr(L_frontFemurJntIk+'.tx')
R_frontFemurJntIk=R_frontFemurJntIk[0]
cmds.setAttr(R_frontFemurJntIk+'.tx',-xPos)

# parent front leg joints...
cmds.parent(L_frontToeJntIk,L_frontAnkleJntIk)
cmds.parent(L_frontAnkleJntIk,L_frontKneeJntIk)
cmds.parent(L_frontKneeJntIk,L_frontUpperKneeJntIk)
cmds.parent(L_frontUpperKneeJntIk,L_frontFemurJntIk)
cmds.parent(L_frontFemurJntIk,frontPelvisJnt)
cmds.parent(R_frontToeJntIk,R_frontAnkleJntIk)
cmds.parent(R_frontAnkleJntIk,R_frontKneeJntIk)
cmds.parent(R_frontKneeJntIk,R_frontUpperKneeJntIk)
cmds.parent(R_frontUpperKneeJntIk,R_frontFemurJntIk)
cmds.parent(R_frontFemurJntIk,frontPelvisJnt)
cmds.parent(frontPelvisJnt,subworld)

# orient joints
cmds.select(L_frontFemurJntIk)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_frontFemurJntIk)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)

''' Fk front legs '''
L_frontToeJntFk=cmds.joint(n='l_frontToeFk_JNT')
constr=cmds.pointConstraint(frontToe,L_frontToeJntFk)
cmds.delete(constr)
cmds.select(d=True)
L_frontAnkleJntFk=cmds.joint(n='l_frontAnkleFk_JNT')
constr=cmds.pointConstraint(frontAnkle,L_frontAnkleJntFk)
cmds.delete(constr)
cmds.select(d=True)
L_frontKneeJntFk=cmds.joint(n='l_frontKneeAnkleFk_JNT')
constr=cmds.pointConstraint(frontKnee,L_frontKneeJntFk)
cmds.delete(constr)
cmds.select(d=True)
L_frontUpperKneeJntFk=cmds.joint(n='l_frontUpperKneeFk_JNT')
constr=cmds.pointConstraint(frontUpperKnee,L_frontUpperKneeJntFk)
cmds.delete(constr)
cmds.select(d=True)
L_frontFemurJntFk=cmds.joint(n='l_frontFemurFk_JNT')
constr=cmds.pointConstraint(frontFemur,L_frontFemurJntFk)
cmds.delete(constr)
cmds.select(d=True)

# mirror to other side...
R_frontToeJntFk=cmds.duplicate(L_frontToeJntFk,n='r_frontToeFk_JNT')
xPos=cmds.getAttr(L_frontToeJntFk+'.tx')
R_frontToeJntFk=R_frontToeJntFk[0]
cmds.setAttr(R_frontToeJntFk+'.tx',-xPos)
R_frontAnkleJntFk=cmds.duplicate(L_frontAnkleJntFk,n='r_frontAnkleFk_JNT')
xPos=cmds.getAttr(L_frontAnkleJntFk+'.tx')
R_frontAnkleJntFk=R_frontAnkleJntFk[0]
cmds.setAttr(R_frontAnkleJntFk+'.tx',-xPos)
R_frontKneeJntFk=cmds.duplicate(L_frontKneeJntFk,n='r_frontKneeFk_JNT')
xPos=cmds.getAttr(L_frontKneeJntFk+'.tx')
R_frontKneeJntFk=R_frontKneeJntFk[0]
cmds.setAttr(R_frontKneeJntFk+'.tx',-xPos)
R_frontUpperKneeJntFk=cmds.duplicate(L_frontUpperKneeJntFk,n='r_frontUpperKneeFk_JNT')
xPos=cmds.getAttr(L_frontUpperKneeJntFk+'.tx')
R_frontUpperKneeJntFk=R_frontUpperKneeJntFk[0]
cmds.setAttr(R_frontUpperKneeJntFk+'.tx',-xPos)
R_frontFemurJntFk=cmds.duplicate(L_frontFemurJntFk,n='r_frontFemurFk_JNT')
xPos=cmds.getAttr(L_frontFemurJntFk+'.tx')
R_frontFemurJntFk=R_frontFemurJntFk[0]
cmds.setAttr(R_frontFemurJntFk+'.tx',-xPos)

# parent front leg joints...
cmds.parent(L_frontToeJntFk,L_frontAnkleJntFk)
cmds.parent(L_frontAnkleJntFk,L_frontKneeJntFk)
cmds.parent(L_frontKneeJntFk,L_frontUpperKneeJntFk)
cmds.parent(L_frontUpperKneeJntFk,L_frontFemurJntFk)
cmds.parent(L_frontFemurJntFk,frontPelvisJnt)
cmds.parent(R_frontToeJntFk,R_frontAnkleJntFk)
cmds.parent(R_frontAnkleJntFk,R_frontKneeJntFk)
cmds.parent(R_frontKneeJntFk,R_frontUpperKneeJntFk)
cmds.parent(R_frontUpperKneeJntFk,R_frontFemurJntFk)
cmds.parent(R_frontFemurJntFk,frontPelvisJnt)

# orient joints...
cmds.select(L_frontFemurJntFk)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(R_frontFemurJntFk)
cmds.joint(e=True,zso=True, oj='xyz',secondaryAxisOrient='yup',ch=True)
cmds.select(d=True)

''' IK leg system '''
''' IK leg system '''
''' L hind leg IK'''
# IK controller...
L_Ik=cmds.ikHandle(sol='ikRPsolver',n='l_hindLeg_IK',sj=L_hindFemurJntIk,ee=L_hindAnkleJntIk )
L_hindIkCtl=cmds.curve(d=1,p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)],k=[0,1,2,3,4],n='l_footIK_CTRL')
# get distance to get controller with decent scale...
dist=cmds.createNode('distanceDimShape',n='delete_me_I_am_in_pain')
legStart=cmds.xform(L_hindToeJntIk,q=True,ws=True,rp=True)
legEnd=cmds.xform(L_frontToeJntIk,q=True,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(legStart))
cmds.setAttr(dist+'.startPoint',*(legEnd))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist,p=True))
distance=distance/8
cmds.setAttr(L_hindIkCtl+'.sx',distance)
cmds.setAttr(L_hindIkCtl+'.sy',distance)
cmds.setAttr(L_hindIkCtl+'.sz',distance)
cmds.makeIdentity(L_hindIkCtl,apply=True,t=1,r=1,s=1,n=0)
lockScale(L_hindIkCtl)
L_hindIkCtlGrp=cmds.group(L_hindIkCtl,n='l_footIKCtrl_GRP')
bluecon(L_hindIkCtlGrp)
constr=cmds.pointConstraint(L_hindToeJnt,L_hindIkCtlGrp)
cmds.delete(constr)
cmds.parent(L_Ik[0],L_hindIkCtl)
cmds.setAttr(L_Ik[0]+'.visibility',0)
# aim constraint makes the upper hind femur joint follow by some but lets the leg fold up like it should...
cmds.aimConstraint(L_hindIkCtl,L_hindFemurJntIk,n='l_femur_aim_towards_footCtrl',mo=True,wu=[0,0,0])
L_IkToe=cmds.ikHandle(sol='ikRPsolver',n='l_hindToe_IK', sj=L_hindAnkleJntIk,ee=L_hindToeJntIk)
cmds.parent(L_IkToe[0],L_hindIkCtl)
cmds.setAttr(L_IkToe[0]+'.visibility',0)

''' r hind leg IK'''
# IK controller...
R_Ik=cmds.ikHandle(sol='ikRPsolver',n='r_hindLeg_IK',sj=R_hindFemurJntIk,ee=R_hindAnkleJntIk )
R_hindIkCtl=cmds.curve(d=1,p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)],k=[0,1,2,3,4],n='r_footIK_CTRL')
cmds.setAttr(R_hindIkCtl+'.sx',distance)
cmds.setAttr(R_hindIkCtl+'.sy',distance)
cmds.setAttr(R_hindIkCtl+'.sz',distance)
cmds.makeIdentity(R_hindIkCtl,apply=True,t=1,r=1,s=1,n=0)
lockScale(R_hindIkCtl)
R_hindIkCtlGrp=cmds.group(R_hindIkCtl,n='r_footIKCtrl_GRP')
redcon(R_hindIkCtlGrp)
constr=cmds.pointConstraint(R_hindToeJnt,R_hindIkCtlGrp)
cmds.delete(constr)
cmds.parent(R_Ik[0],R_hindIkCtl)
cmds.setAttr(R_Ik[0]+'.visibility',0)
# aim constraint makes the upper hind femur joint follow by some but lets the leg fold up like it should...
cmds.aimConstraint(R_hindIkCtl,R_hindFemurJntIk,n='r_femur_aim_towards_footCtrl',mo=True,wu=[0,0,0])
R_IkToe=cmds.ikHandle(sol='ikRPsolver',n='r_hindToe_IK', sj=R_hindAnkleJntIk,ee=R_hindToeJntIk)
cmds.parent(R_IkToe[0],R_hindIkCtl)
cmds.setAttr(R_IkToe[0]+'.visibility',0)

''' l front leg IK'''
L_FIk=cmds.ikHandle(sol='ikRPsolver',n='l_frontLeg_IK',sj=L_frontFemurJntIk,ee=L_frontAnkleJntIk )
L_frontIkCtl=cmds.curve(d=1,p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)],k=[0,1,2,3,4],n='l_frontIK_CTRL')
cmds.setAttr(L_frontIkCtl+'.sx',distance)
cmds.setAttr(L_frontIkCtl+'.sy',distance)
cmds.setAttr(L_frontIkCtl+'.sz',distance)
cmds.makeIdentity(L_frontIkCtl,apply=True,t=1,r=1,s=1,n=0)
lockScale(L_frontIkCtl)
L_frontIkCtlGrp=cmds.group(L_frontIkCtl,n='l_frontFootIKCtrl_GRP')
bluecon(L_frontIkCtlGrp)
constr=cmds.pointConstraint(L_frontToeJnt,L_frontIkCtlGrp)
cmds.delete(constr)
cmds.parent(L_FIk[0],L_frontIkCtl)
cmds.setAttr(L_FIk[0]+'.visibility',0)
L_FToeIk=cmds.ikHandle(sol='ikRPsolver',n='l_frontToe_IK',sj=L_frontAnkleJntIk,ee=L_frontToeJntIk)
cmds.parent(L_FToeIk[0],L_frontIkCtl)

''' l ik front leg rotation ctrl '''
L_frontLegTranslate=cmds.circle(nr=(1,0,0), c=(0,0,0), n='l_frontLegTranslate_CTRL')
L_frontLegTranslateGrp=cmds.group(L_frontLegTranslate, n='l_frontLegTranslateCtrl_GRP')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontLegTranslateGrp,apply=True, t=1,r=1,s=1,n=0)
constr=cmds.pointConstraint(L_frontFemurJntIk,L_frontLegTranslateGrp)
cmds.delete(constr)
bluecon(L_frontLegTranslate[0])
lockRotate(L_frontLegTranslate[0])


''' r front leg IK'''
R_FIk=cmds.ikHandle(sol='ikRPsolver',n='r_frontLeg_IK',sj=R_frontFemurJntIk,ee=R_frontAnkleJntIk )
R_frontIkCtl=cmds.curve(d=1,p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)],k=[0,1,2,3,4],n='r_frontIK_CTRL')
cmds.setAttr(R_frontIkCtl+'.sx',distance)
cmds.setAttr(R_frontIkCtl+'.sy',distance)
cmds.setAttr(R_frontIkCtl+'.sz',distance)
cmds.makeIdentity(R_frontIkCtl,apply=True,t=1,r=1,s=1,n=0)
lockScale(R_frontIkCtl)
R_frontIkCtlGrp=cmds.group(R_frontIkCtl,n='r_frontFootIKCtrl_GRP')
redcon(R_frontIkCtlGrp)
constr=cmds.pointConstraint(R_frontToeJnt,R_frontIkCtlGrp)
cmds.delete(constr)
cmds.parent(R_FIk[0],R_frontIkCtl)
cmds.setAttr(R_FIk[0]+'.visibility',0)
R_FToeIk=cmds.ikHandle(sol='ikRPsolver',n='r_frontToe_IK',sj=R_frontAnkleJntIk,ee=R_frontToeJntIk)
cmds.parent(R_FToeIk[0],R_frontIkCtl)


''' r ik front leg rotation ctrl '''
R_frontLegTranslate=cmds.circle(nr=(1,0,0), c=(0,0,0), n='r_frontLegTranslate_CTRL')
R_frontLegTranslateGrp=cmds.group(R_frontLegTranslate, n='r_frontLegTranslateCtrl_GRP')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontLegTranslateGrp,apply=True, t=1,r=1,s=1,n=0)
constr=cmds.pointConstraint(R_frontFemurJntIk,R_frontLegTranslateGrp)
cmds.delete(constr)
redcon(R_frontLegTranslate[0])
lockRotate(R_frontLegTranslate[0])

''' create IK polevector '''
# l hind IK
L_hindPole=cmds.curve(d=1, p=[(-1.03923,0,0.6),(1.03923,0,0.6),(0,0,-1.2),(-1.03923,0,0.6)], k=[0,1,2,3],n='l_hindPoleVector_CTRL')
cmds.scale(distance/2,distance/2,distance/2)    
cmds.makeIdentity(L_hindPole,apply=True,t=1,r=1,s=1,n=0)
L_hindPoleGrp=cmds.group(L_hindPole,n='L_hindPoleVectorCtrl_GRP')
constr=cmds.parentConstraint(hindKnee,L_hindPoleGrp)
cmds.delete(constr)
addDist=cmds.getAttr(L_hindPoleGrp+'.tz')
cmds.setAttr(L_hindPoleGrp+'.tz',addDist*2)
bluecon(L_hindPole)
cmds.poleVectorConstraint(L_hindPole,L_Ik[0])
cmds.setAttr(L_Ik[0]+'.twist',180)
# r hind IK
R_hindPole=cmds.curve(d=1, p=[(-1.03923,0,0.6),(1.03923,0,0.6),(0,0,-1.2),(-1.03923,0,0.6)], k=[0,1,2,3],n='r_hindPoleVector_CTRL')
cmds.scale(distance/2,distance/2,distance/2)    
cmds.makeIdentity(R_hindPole,apply=True,t=1,r=1,s=1,n=0)
R_hindPoleGrp=cmds.group(R_hindPole,n='R_hindPoleVectorCtrl_GRP')
constr=cmds.parentConstraint(hindKnee,R_hindPoleGrp)
cmds.delete(constr)
cmds.setAttr(R_hindPoleGrp+'.tz',addDist*2)
redcon(R_hindPole)
revDist=cmds.getAttr(R_hindPoleGrp+'.tx')
cmds.setAttr(R_hindPoleGrp+'.tx',-revDist)
cmds.poleVectorConstraint(R_hindPole,R_Ik[0])
cmds.setAttr(R_Ik[0]+'.twist',180)
# l front IK
L_frontPole=cmds.curve(d=1, p=[(-1.03923,0,0.6),(1.03923,0,0.6),(0,0,-1.2),(-1.03923,0,0.6)], k=[0,1,2,3],n='l_frontPoleVector_CTRL')
cmds.scale(distance/2,distance/2,distance/2)    
cmds.makeIdentity(L_frontPole,apply=True,t=1,r=1,s=1,n=0)
lockScale(L_frontPole)
L_frontPoleGrp=cmds.group(L_frontPole,n='L_frontPoleVecorCtrl_GRP')
constr=cmds.parentConstraint(frontKnee,L_frontPoleGrp)
cmds.delete(constr)
addDist=cmds.getAttr(L_frontPoleGrp+'.tz')
cmds.setAttr(L_frontPoleGrp+'.tz', distance*2)
bluecon(L_frontPole)
cmds.poleVectorConstraint(L_frontPole,L_FIk[0])

# r front IK
R_frontPole=cmds.curve(d=1, p=[(-1.03923,0,0.6),(1.03923,0,0.6),(0,0,-1.2),(-1.03923,0,0.6)], k=[0,1,2,3],n='r_frontPoleVector_CTRL')
cmds.scale(distance/2,distance/2,distance/2)    
cmds.makeIdentity(R_frontPole,apply=True,t=1,r=1,s=1,n=0)
lockScale(R_frontPole)
R_frontPoleGrp=cmds.group(R_frontPole,n='R_frontPoleVecorCtrl_GRP')
constr=cmds.parentConstraint(frontKnee,R_frontPoleGrp)
cmds.delete(constr)
addDist=cmds.getAttr(R_frontPoleGrp+'.tz')
cmds.setAttr(R_frontPoleGrp+'.tz', distance*2)
revDist=cmds.getAttr(R_frontPoleGrp+'.tx')
cmds.setAttr(R_frontPoleGrp+'.tx',-revDist)
redcon(R_frontPole)
cmds.poleVectorConstraint(R_frontPole,R_FIk[0])

# group IK...
poleVectorGrp=cmds.group(L_frontPoleGrp,R_frontPoleGrp,L_hindPoleGrp,R_hindPoleGrp,n='c_poleVector_GRP')
IkCtlGrp=cmds.group(poleVectorGrp,R_frontLegTranslateGrp,L_frontLegTranslateGrp,R_frontIkCtlGrp,L_frontIkCtlGrp,R_hindIkCtlGrp,L_hindIkCtlGrp, n='c_IkCtrl_GRP')

''' fk leg setup '''
''' fk leg setup '''
# l fk hind leg...
L_hindLegFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_hindLegFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_hindLegFkCtl,apply=True, t=1, r=1, s=1, n=0)
L_hindLegFkCtlGrp=cmds.group(L_hindLegFkCtl,n='l_hindLegFkCtrl GRP')
constr=cmds.pointConstraint(L_hindFemurJntFk,L_hindLegFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_hindLegFkCtlGrp,L_hindFemurJntFk,mo=True)
lockScale(L_hindLegFkCtl[0])

L_hindUpperKneeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_hindUpperKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_hindUpperKneeFkCtl,apply=True, t=1, r=1, s=1, n=0)
L_hindUpperKneeFkCtlGrp=cmds.group(L_hindUpperKneeFkCtl,n='l_hindUpperKneeFKCtrl GRP')
constr=cmds.pointConstraint(L_hindUpperKneeJntFk,L_hindUpperKneeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_hindUpperKneeFkCtl,L_hindUpperKneeJntFk,mo=True)
lockScale(L_hindUpperKneeFkCtl[0])

L_hindKneeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_hindKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_hindKneeFkCtl,apply=True, t=1, r=1, s=1, n=0)
L_hindKneeFkCtlGrp=cmds.group(L_hindKneeFkCtl,n='l_hindKneeFKCtrl GRP')
constr=cmds.pointConstraint(L_hindKneeJntFk,L_hindKneeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_hindKneeFkCtl,L_hindKneeJntFk,mo=True)
lockScale(L_hindKneeFkCtl[0])

L_hindAnkleFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_hindAnkleFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_hindAnkleFkCtl,apply=True, t=1, r=1, s=1, n=0)
L_hindAnkleFkCtlGrp=cmds.group(L_hindAnkleFkCtl,n='l_hindAnkleFKCtrl GRP')
constr=cmds.pointConstraint(L_hindAnkleJntFk,L_hindAnkleFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_hindAnkleFkCtl,L_hindAnkleJntFk,mo=True)
lockScale(L_hindAnkleFkCtl[0])

L_hindToeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_hindToeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_hindToeFkCtl,apply=True, t=1, r=1, s=1, n=0)
L_hindToeFkCtlGrp=cmds.group(L_hindToeFkCtl,n='l_hindToeFKCtrl_GRP')
constr=cmds.pointConstraint(L_hindToeJntFk,L_hindToeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_hindToeFkCtl,L_hindToeJntFk,mo=True)
lockScale(L_hindToeFkCtl[0])
# parent fk...
cmds.parent(L_hindToeFkCtlGrp,L_hindAnkleFkCtl[0])
cmds.parent(L_hindAnkleFkCtlGrp,L_hindKneeFkCtl[0])
cmds.parent(L_hindKneeFkCtlGrp,L_hindUpperKneeFkCtl[0])
cmds.parent(L_hindUpperKneeFkCtlGrp,L_hindLegFkCtl[0])
bluecon(L_hindLegFkCtl[0])
cmds.parentConstraint(hindPelvisJnt,L_hindLegFkCtlGrp,mo=True)

# r fk hind leg...
R_hindLegFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_hindLegFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindLegFkCtl,apply=True, t=1, r=1, s=1, n=0)
R_hindLegFkCtlGrp=cmds.group(R_hindLegFkCtl,n='r_hindLegFkCtrl GRP')
constr=cmds.pointConstraint(R_hindFemurJntFk,R_hindLegFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_hindLegFkCtlGrp,R_hindFemurJntFk,mo=True)
lockScale(R_hindLegFkCtl[0])

R_hindUpperKneeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_hindUpperKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindUpperKneeFkCtl,apply=True, t=1, r=1, s=1, n=0)
R_hindUpperKneeFkCtlGrp=cmds.group(R_hindUpperKneeFkCtl,n='r_hindUpperKneeFKCtrl GRP')
constr=cmds.pointConstraint(R_hindUpperKneeJntFk,R_hindUpperKneeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_hindUpperKneeFkCtl,R_hindUpperKneeJntFk,mo=True)
lockScale(R_hindUpperKneeFkCtl[0])

R_hindKneeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_hindKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindKneeFkCtl,apply=True, t=1, r=1, s=1, n=0)
R_hindKneeFkCtlGrp=cmds.group(R_hindKneeFkCtl,n='r_hindKneeFKCtrl GRP')
constr=cmds.pointConstraint(R_hindKneeJntFk,R_hindKneeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_hindKneeFkCtl,R_hindKneeJntFk,mo=True)
lockScale(R_hindKneeFkCtl[0])

R_hindAnkleFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_hindAnkleFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindAnkleFkCtl,apply=True, t=1, r=1, s=1, n=0)
R_hindAnkleFkCtlGrp=cmds.group(R_hindAnkleFkCtl,n='r_hindAnkleFKCtrl GRP')
constr=cmds.pointConstraint(R_hindAnkleJntFk,R_hindAnkleFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_hindAnkleFkCtl,R_hindAnkleJntFk,mo=True)
lockScale(R_hindAnkleFkCtl[0])

R_hindToeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='R_hindToeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_hindToeFkCtl,apply=True, t=1, r=1, s=1, n=0)
R_hindToeFkCtlGrp=cmds.group(R_hindToeFkCtl,n='r_hindToeFKCtrR_GRP')
constr=cmds.pointConstraint(R_hindToeJntFk,R_hindToeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_hindToeFkCtl,R_hindToeJntFk,mo=True)
lockScale(R_hindToeFkCtl[0])

# parent fk...
cmds.parent(R_hindToeFkCtlGrp,R_hindAnkleFkCtl[0])
cmds.parent(R_hindAnkleFkCtlGrp,R_hindKneeFkCtl[0])
cmds.parent(R_hindKneeFkCtlGrp,R_hindUpperKneeFkCtl[0])
cmds.parent(R_hindUpperKneeFkCtlGrp,R_hindLegFkCtl[0])
redcon(R_hindLegFkCtl[0])
cmds.parentConstraint(hindPelvisJnt,R_hindLegFkCtlGrp,mo=True)

# l fk front leg...
L_frontLegFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_frontLegFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontLegFkCtl,apply=True, t=1, r=1, s=1, n=0)
L_frontLegFkCtlGrp=cmds.group(L_frontLegFkCtl,n='l_frontLegFkCtrl GRP')
constr=cmds.pointConstraint(L_frontFemurJntFk,L_frontLegFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_frontLegFkCtlGrp,L_frontFemurJntFk,mo=True)
lockScale(L_frontLegFkCtl[0])

L_frontUpperKneeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_frontUpperKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontUpperKneeFkCtl,apply=True, t=1, r=1, s=1, n=0)
L_frontUpperKneeFkCtlGrp=cmds.group(L_frontUpperKneeFkCtl,n='l_frontUpperKneeFKCtrl GRP')
constr=cmds.pointConstraint(L_frontUpperKneeJntFk,L_frontUpperKneeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_frontUpperKneeFkCtl,L_frontUpperKneeJntFk,mo=True)
lockScale(L_frontUpperKneeFkCtl[0])

L_frontKneeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_frontKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontKneeFkCtl,apply=True, t=1, r=1, s=1, n=0)
L_frontKneeFkCtlGrp=cmds.group(L_frontKneeFkCtl,n='l_frontKneeFKCtrl GRP')
constr=cmds.pointConstraint(L_frontKneeJntFk,L_frontKneeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_frontKneeFkCtl,L_frontKneeJntFk,mo=True)
lockScale(L_frontKneeFkCtl[0])

L_frontAnkleFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_frontAnkleFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontAnkleFkCtl,apply=True, t=1, r=1, s=1, n=0)
L_frontAnkleFkCtlGrp=cmds.group(L_frontAnkleFkCtl,n='l_frontAnkleFKCtrl GRP')
constr=cmds.pointConstraint(L_frontAnkleJntFk,L_frontAnkleFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_frontAnkleFkCtl,L_frontAnkleJntFk,mo=True)
lockScale(L_frontAnkleFkCtl[0])

L_frontToeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='l_frontToeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(L_frontToeFkCtl,apply=True, t=1, r=1, s=1, n=0)
L_frontToeFkCtlGrp=cmds.group(L_frontToeFkCtl,n='l_frontToeFKCtrl_GRP')
constr=cmds.pointConstraint(L_frontToeJntFk,L_frontToeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(L_frontToeFkCtl,L_frontToeJntFk,mo=True)
lockScale(L_frontToeFkCtl[0])
# parent fk...
cmds.parent(L_frontToeFkCtlGrp,L_frontAnkleFkCtl[0])
cmds.parent(L_frontAnkleFkCtlGrp,L_frontKneeFkCtl[0])
cmds.parent(L_frontKneeFkCtlGrp,L_frontUpperKneeFkCtl[0])
cmds.parent(L_frontUpperKneeFkCtlGrp,L_frontLegFkCtl[0])
bluecon(L_frontLegFkCtl[0])
cmds.parentConstraint(frontPelvisJnt,L_frontLegFkCtlGrp,mo=True)

# r fk front leg...
R_frontLegFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_frontLegFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontLegFkCtl,apply=True, t=1, r=1, s=1, n=0)
R_frontLegFkCtlGrp=cmds.group(R_frontLegFkCtl,n='r_frontLegFkCtrl GRP')
constr=cmds.pointConstraint(R_frontFemurJntFk,R_frontLegFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_frontLegFkCtlGrp,R_frontFemurJntFk,mo=True)
lockScale(R_frontLegFkCtl[0])

R_frontUpperKneeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_frontUpperKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontUpperKneeFkCtl,apply=True, t=1, r=1, s=1, n=0)
R_frontUpperKneeFkCtlGrp=cmds.group(R_frontUpperKneeFkCtl,n='r_frontUpperKneeFKCtrl GRP')
constr=cmds.pointConstraint(R_frontUpperKneeJntFk,R_frontUpperKneeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_frontUpperKneeFkCtl,R_frontUpperKneeJntFk,mo=True)
lockScale(R_frontUpperKneeFkCtl[0])

R_frontKneeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_frontKneeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontKneeFkCtl,apply=True, t=1, r=1, s=1, n=0)
R_frontKneeFkCtlGrp=cmds.group(R_frontKneeFkCtl,n='r_frontKneeFKCtrl GRP')
constr=cmds.pointConstraint(R_frontKneeJntFk,R_frontKneeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_frontKneeFkCtl,R_frontKneeJntFk,mo=True)
lockScale(R_frontKneeFkCtl[0])

R_frontAnkleFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='r_frontAnkleFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontAnkleFkCtl,apply=True, t=1, r=1, s=1, n=0)
R_frontAnkleFkCtlGrp=cmds.group(R_frontAnkleFkCtl,n='r_frontAnkleFKCtrl GRP')
constr=cmds.pointConstraint(R_frontAnkleJntFk,R_frontAnkleFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_frontAnkleFkCtl,R_frontAnkleJntFk,mo=True)
lockScale(R_frontAnkleFkCtl[0])

R_frontToeFkCtl=cmds.circle( nr=(0, 1, 0), c=(0, 0, 0),n='R_frontToeFK_CTRL')
cmds.scale(distance,distance,distance)
cmds.makeIdentity(R_frontToeFkCtl,apply=True, t=1, r=1, s=1, n=0)
R_frontToeFkCtlGrp=cmds.group(R_frontToeFkCtl,n='r_frontToeFKCtrR_GRP')
constr=cmds.pointConstraint(R_frontToeJntFk,R_frontToeFkCtlGrp)
cmds.delete(constr)
constr=cmds.parentConstraint(R_frontToeFkCtl,R_frontToeJntFk,mo=True)
lockScale(R_frontToeFkCtl[0])

# parent fk...
cmds.parent(R_frontToeFkCtlGrp,R_frontAnkleFkCtl[0])
cmds.parent(R_frontAnkleFkCtlGrp,R_frontKneeFkCtl[0])
cmds.parent(R_frontKneeFkCtlGrp,R_frontUpperKneeFkCtl[0])
cmds.parent(R_frontUpperKneeFkCtlGrp,R_frontLegFkCtl[0])
redcon(R_frontLegFkCtl[0])
cmds.parentConstraint(frontPelvisJnt,R_frontLegFkCtlGrp,mo=True)

# group fk controllers...
FkCtlGrp=cmds.group(L_hindLegFkCtlGrp,R_hindLegFkCtlGrp,L_frontLegFkCtlGrp,R_frontLegFkCtlGrp, n='c_FKCtrl_GRP')

''' IK FK switch '''
# l hind leg switch...
L_hindSwitch=cmds.curve(d=3, p=[(0.474561,0,-1.241626),(0.171579,0,-1.214307),(-0.434384,0,-1.159672),(-1.124061,0,-0.419971),(-1.169741,0,0.305922),(-0.792507,0,1.018176),(-0.0412486,0,1.262687),(0.915809,0,1.006098),(1.258635,0,0.364883),(1.032378,0,-0.461231),(0.352527,0,-0.810017),(-0.451954,0,-0.43765),(-0.634527,0,0.208919),(-0.0751226,0,0.696326),(0.292338,0,0.414161),(0.476068,0,0.273078)],k=[0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,13],n='l_hindSwitch_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0)
lockScale(L_hindSwitch)
lockTranslate(L_hindSwitch)
lockRotate(L_hindSwitch)
L_hindSwitchGrp=cmds.group(L_hindSwitch, n='l_hindSwitchCtrl_GRP')
constr=cmds.pointConstraint(L_hindAnkleJnt, L_hindSwitchGrp)
cmds.delete(constr)
dist=cmds.getAttr(L_hindSwitchGrp+'.tz')
cmds.setAttr(L_hindSwitchGrp+'.tz',dist-distance)
constr=cmds.pointConstraint(L_hindAnkleJnt,L_hindSwitchGrp,mo=True)
bluecon(L_hindSwitch)
cmds.addAttr(L_hindSwitch,longName='Leg_functions',at='enum',en=('____'),k=True)
cmds.setAttr(L_hindSwitch+'.Leg_functions',l=True)
cmds.addAttr(L_hindSwitch,longName='IK_FK',at='float', min=0, max=1, k=True)
# r hind leg switch...
R_hindSwitch=cmds.curve(d=3, p=[(0.474561,0,-1.241626),(0.171579,0,-1.214307),(-0.434384,0,-1.159672),(-1.124061,0,-0.419971),(-1.169741,0,0.305922),(-0.792507,0,1.018176),(-0.0412486,0,1.262687),(0.915809,0,1.006098),(1.258635,0,0.364883),(1.032378,0,-0.461231),(0.352527,0,-0.810017),(-0.451954,0,-0.43765),(-0.634527,0,0.208919),(-0.0751226,0,0.696326),(0.292338,0,0.414161),(0.476068,0,0.273078)],k=[0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,13],n='r_hindSwitch_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0)
lockScale(R_hindSwitch)
lockTranslate(R_hindSwitch)
lockRotate(R_hindSwitch)
R_hindSwitchGrp=cmds.group(R_hindSwitch, n='r_hindSwitchCtrl_GRP')
constr=cmds.pointConstraint(R_hindAnkleJnt, R_hindSwitchGrp)
cmds.delete(constr)
cmds.setAttr(R_hindSwitchGrp+'.tz',dist-distance)
constr=cmds.pointConstraint(R_hindAnkleJnt,R_hindSwitchGrp,mo=True)
redcon(R_hindSwitch)
cmds.addAttr(R_hindSwitch,longName='Leg_functions',at='enum',en=('____'),k=True)
cmds.setAttr(R_hindSwitch+'.Leg_functions',l=True)
cmds.addAttr(R_hindSwitch,longName='IK_FK',at='float', min=0, max=1, k=True)

# visibiliti of controllers...
cmds.connectAttr(L_hindSwitch+'.IK_FK',L_hindLegFkCtlGrp+'.visibility')
cmds.connectAttr(R_hindSwitch+'.IK_FK',R_hindLegFkCtlGrp+'.visibility')
IkFkHindRev=cmds.createNode('reverse', n='IK_FK_hindLeg_REV')
cmds.connectAttr(L_hindSwitch+'.IK_FK', IkFkHindRev+'.ix')
cmds.connectAttr(R_hindSwitch+'.IK_FK', IkFkHindRev+'.iy')
cmds.connectAttr(IkFkHindRev+'.ox', L_hindIkCtlGrp+'.visibility')
cmds.connectAttr(IkFkHindRev+'.oy', R_hindIkCtlGrp+'.visibility')
cmds.connectAttr(IkFkHindRev+'.ox', L_hindPoleGrp+'.visibility')
cmds.connectAttr(IkFkHindRev+'.oy', R_hindPoleGrp+'.visibility')

# l front leg switch...
L_frontSwitch=cmds.curve(d=3, p=[(0.474561,0,-1.241626),(0.171579,0,-1.214307),(-0.434384,0,-1.159672),(-1.124061,0,-0.419971),(-1.169741,0,0.305922),(-0.792507,0,1.018176),(-0.0412486,0,1.262687),(0.915809,0,1.006098),(1.258635,0,0.364883),(1.032378,0,-0.461231),(0.352527,0,-0.810017),(-0.451954,0,-0.43765),(-0.634527,0,0.208919),(-0.0751226,0,0.696326),(0.292338,0,0.414161),(0.476068,0,0.273078)],k=[0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,13],n='l_frontSwitch_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0)
lockScale(L_frontSwitch)
lockTranslate(L_frontSwitch)
lockRotate(L_frontSwitch)
L_frontSwitchGrp=cmds.group(L_frontSwitch, n='l_frontSwitchCtrl_GRP')
constr=cmds.pointConstraint(L_frontAnkleJnt, L_frontSwitchGrp)
cmds.delete(constr)
dist=cmds.getAttr(L_frontSwitchGrp+'.tz')
cmds.setAttr(L_frontSwitchGrp+'.tz',dist-distance)
constr=cmds.pointConstraint(L_frontAnkleJnt,L_frontSwitchGrp,mo=True)
bluecon(L_frontSwitch)
cmds.addAttr(L_frontSwitch,longName='Leg_functions',at='enum',en=('____'),k=True)
cmds.setAttr(L_frontSwitch+'.Leg_functions',l=True)
cmds.addAttr(L_frontSwitch,longName='IK_FK',at='float', min=0, max=1, k=True)
# r front leg switch...
R_frontSwitch=cmds.curve(d=3, p=[(0.474561,0,-1.241626),(0.171579,0,-1.214307),(-0.434384,0,-1.159672),(-1.124061,0,-0.419971),(-1.169741,0,0.305922),(-0.792507,0,1.018176),(-0.0412486,0,1.262687),(0.915809,0,1.006098),(1.258635,0,0.364883),(1.032378,0,-0.461231),(0.352527,0,-0.810017),(-0.451954,0,-0.43765),(-0.634527,0,0.208919),(-0.0751226,0,0.696326),(0.292338,0,0.414161),(0.476068,0,0.273078)],k=[0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,13,13],n='r_frontSwitch_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(apply=True, t=1,r=1,s=1,n=0)
lockScale(R_frontSwitch)
lockTranslate(R_frontSwitch)
lockRotate(R_frontSwitch)
R_frontSwitchGrp=cmds.group(R_frontSwitch, n='r_frontSwitchCtrl_GRP')
constr=cmds.pointConstraint(R_frontAnkleJnt, R_frontSwitchGrp)
cmds.delete(constr)
cmds.setAttr(R_frontSwitchGrp+'.tz',dist-distance)
constr=cmds.pointConstraint(R_frontAnkleJnt,R_frontSwitchGrp,mo=True)
redcon(R_frontSwitch)
cmds.addAttr(R_frontSwitch,longName='Leg_functions',at='enum',en=('____'),k=True)
cmds.setAttr(R_frontSwitch+'.Leg_functions',l=True)
cmds.addAttr(R_frontSwitch,longName='IK_FK',at='float', min=0, max=1, k=True)

# visibiliti of controllers...
cmds.connectAttr(L_frontSwitch+'.IK_FK',L_frontLegFkCtlGrp+'.visibility')
cmds.connectAttr(R_frontSwitch+'.IK_FK',R_frontLegFkCtlGrp+'.visibility')
IkFkfrontRev=cmds.createNode('reverse', n='IK_FK_frontLeg_REV')
cmds.connectAttr(L_frontSwitch+'.IK_FK', IkFkfrontRev+'.ix')
cmds.connectAttr(R_frontSwitch+'.IK_FK', IkFkfrontRev+'.iy')
cmds.connectAttr(IkFkfrontRev+'.ox', L_frontIkCtlGrp+'.visibility')
cmds.connectAttr(IkFkfrontRev+'.oy', R_frontIkCtlGrp+'.visibility')
cmds.connectAttr(IkFkfrontRev+'.ox', L_frontPoleGrp+'.visibility')
cmds.connectAttr(IkFkfrontRev+'.oy', R_frontPoleGrp+'.visibility')
cmds.connectAttr(IkFkfrontRev+'.ox', L_frontLegTranslateGrp+'.visibility')
cmds.connectAttr(IkFkfrontRev+'.oy', R_frontLegTranslateGrp+'.visibility')

# group IK FK switch system...
legSwitchGrp=cmds.group(L_frontSwitchGrp,R_frontSwitchGrp,L_hindSwitchGrp,R_hindSwitchGrp, n='c_legSwitchCtrl_GRP')
legCtlGrp=cmds.group(IkCtlGrp,FkCtlGrp, n='c_legCtrl_GRP')

# blend IK FK joint influence...
def blendJoints(ikJoints,fkJoints,skinJoints,master):
    count=0
    for e in skinJoints:
        #order is IK - FK - Main
        blendr1=cmds.shadingNode('blendColors',asUtility=True, n='L_IKFK_Switch_rotate_1')
        cmds.connectAttr(ikJoints[count]+'.rx',blendr1+'.color1R')
        cmds.connectAttr(ikJoints[count]+'.ry',blendr1+'.color1G')
        cmds.connectAttr(ikJoints[count]+'.rz',blendr1+'.color1B')
        cmds.connectAttr(fkJoints[count]+'.rx',blendr1+'.color2R')
        cmds.connectAttr(fkJoints[count]+'.ry',blendr1+'.color2G')
        cmds.connectAttr(fkJoints[count]+'.rz',blendr1+'.color2B')
        cmds.connectAttr(blendr1+'.output.outputR',skinJoints[count]+'.rx')
        cmds.connectAttr(blendr1+'.output.outputG',skinJoints[count]+'.ry')
        cmds.connectAttr(blendr1+'.output.outputB',skinJoints[count]+'.rz')
        cmds.connectAttr(master,blendr1+'.blender')
        count+=1

skinJoints=[L_hindToeJnt,L_hindAnkleJnt,L_hindKneeJnt,L_hindUpperKneeJnt,L_hindFemurJnt]
ikJoints=[L_hindToeJntIk,L_hindAnkleJntIk,L_hindKneeJntIk,L_hindUpperKneeJntIk,L_hindFemurJntIk]
fkJoints=[L_hindToeJntFk,L_hindAnkleJntFk,L_hindKneeJntFk,L_hindUpperKneeJntFk,L_hindFemurJntFk]
master=IkFkHindRev+'.ox'
blendJoints(ikJoints,fkJoints,skinJoints,master)

skinJoints=[R_hindToeJnt[0],R_hindAnkleJnt[0],R_hindKneeJnt[0],R_hindUpperKneeJnt[0],R_hindFemurJnt[0]]
ikJoints=[R_hindToeJntIk,R_hindAnkleJntIk,R_hindKneeJntIk,R_hindUpperKneeJntIk,R_hindFemurJntIk]
fkJoints=[R_hindToeJntFk,R_hindAnkleJntFk,R_hindKneeJntFk,R_hindUpperKneeJntFk,R_hindFemurJntFk]
master=IkFkHindRev+'.oy'
blendJoints(ikJoints,fkJoints,skinJoints,master)

skinJoints=[L_frontToeJnt,L_frontAnkleJnt,L_frontKneeJnt,L_frontUpperKneeJnt,L_frontFemurJnt]
ikJoints=[L_frontToeJntIk,L_frontAnkleJntIk,L_frontKneeJntIk,L_frontUpperKneeJntIk,L_frontFemurJntIk]
fkJoints=[L_frontToeJntFk,L_frontAnkleJntFk,L_frontKneeJntFk,L_frontUpperKneeJntFk,L_frontFemurJntFk]
master=IkFkfrontRev+'.ox'
blendJoints(ikJoints,fkJoints,skinJoints,master)

skinJoints=[R_frontToeJnt,R_frontAnkleJnt,R_frontKneeJnt,R_frontUpperKneeJnt,R_frontFemurJnt]
ikJoints=[R_frontToeJntIk,R_frontAnkleJntIk,R_frontKneeJntIk,R_frontUpperKneeJntIk,R_frontFemurJntIk]
fkJoints=[R_frontToeJntFk,R_frontAnkleJntFk,R_frontKneeJntFk,R_frontUpperKneeJntFk,R_frontFemurJntFk]
master=IkFkfrontRev+'.oy'
blendJoints(ikJoints,fkJoints,skinJoints,master)


# front femur must be connected to translations...
def blendJointsTranslate(ikJoints,fkJoints,skinJoints,master):
    count=0
    for e in skinJoints:
        blendr1=cmds.shadingNode('blendColors',asUtility=True,n='L_IKFK_switch_translate_1')
        cmds.connectAttr(ikJoints[count]+'.tx',blendr1+'.color1R')
        cmds.connectAttr(ikJoints[count]+'.ty',blendr1+'.color1G')
        cmds.connectAttr(ikJoints[count]+'.tz',blendr1+'.color1B')
        cmds.connectAttr(fkJoints[count]+'.tx',blendr1+'.color2R')
        cmds.connectAttr(fkJoints[count]+'.ty',blendr1+'.color2G')
        cmds.connectAttr(fkJoints[count]+'.tz',blendr1+'.color2B')
        cmds.connectAttr(blendr1+'.output.outputR',skinJoints[count]+'.tx')
        cmds.connectAttr(blendr1+'.output.outputG',skinJoints[count]+'.ty')
        cmds.connectAttr(blendr1+'.output.outputB',skinJoints[count]+'.tz')
        cmds.connectAttr(master,blendr1+'.blender')
        count+=1    

skinJoints=[L_frontFemurJnt]
ikJoints=[L_frontFemurJntIk]
fkJoints=[L_frontFemurJntFk]
master=IkFkfrontRev+'.ox'
blendJointsTranslate(ikJoints,fkJoints,skinJoints,master)
skinJoints=[R_frontFemurJnt]
ikJoints=[R_frontFemurJntIk]
fkJoints=[R_frontFemurJntFk]
blendJointsTranslate(ikJoints,fkJoints,skinJoints,master)

# set it...
skinJntSet=cmds.sets(L_hindToeJnt,R_hindToeJnt,L_hindAnkleJnt,R_hindAnkleJnt,L_hindKneeJnt,R_hindKneeJnt,L_hindUpperKneeJnt,R_hindUpperKneeJnt,L_hindFemurJnt,R_hindFemurJnt,L_frontToeJnt,R_frontToeJnt,L_frontAnkleJnt,R_frontAnkleJnt,L_frontKneeJnt,R_frontKneeJnt,L_frontFemurJnt,R_frontFemurJnt, n='LegSkinJnt_SET')

''' create tail/spine module '''
''' create tail/spine module '''
# meassure the distance between joints and get tail root placement...
dist=cmds.createNode('distanceDimShape', n='delete_me_my_boy')
tailStart=cmds.xform(tail1,q=True,ws=True,rp=True)
tailEnd=cmds.xform(tail2,q=True,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(tailEnd))
cmds.setAttr(dist+'.startPoint',*(tailStart))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist, p=True))
# joints in chain...
initialAmmountOfJoints=5
#
ammountOfJoints=initialAmmountOfJoints-1
cmds.select(d=True)
tailRootJnt=cmds.joint(n='c_tail5_JNT')
while ammountOfJoints > 0:
    tailJnt=cmds.joint(n='c_tail'+str(ammountOfJoints)+'_JNT')
    ammountOfJoints-=1
cmds.select(tailRootJnt, hi=True)
tailJointChain=cmds.ls(sl=True)
# calculate translation distance between each joint...
ammountOfJoints=initialAmmountOfJoints-1
distancePerJoint=distance/ammountOfJoints
for e in tailJointChain:
    cmds.setAttr(e+'.tz',-distancePerJoint)
cmds.setAttr(tailRootJnt+'.tz',0)
cmds.rename(tailJointChain[-1],tailJointChain[-1]+'End')
constr=cmds.pointConstraint(tail1,tailJointChain[0])

# rotate joint to aim for the end of the chain...
tempcon=cmds.aimConstraint(tail2,tailRootJnt, aimVector=(0,0,-1))
rotation=cmds.getAttr(tailRootJnt+'.rx')
cmds.delete(tempcon)
cmds.parent(tailJointChain[1],w=True)
cmds.setAttr(tailRootJnt+'.rx',0)
cmds.setAttr(tailRootJnt+'.ry',0)
cmds.setAttr(tailRootJnt+'.rz',0)
cmds.parent(tailJointChain[1],tailRootJnt)
cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True)

# create IK solver...
IkTailHandle=cmds.ikHandle(sol='ikSplineSolver', ns=4, n='c_tailSolver_IK', sj=tailRootJnt, ee=tailJointChain[-1]+'End')
IkHandleGrp=cmds.group(IkTailHandle[0],IkTailHandle[2], n='C_IK_tailSystem_GRP' )
cmds.setAttr(IkHandleGrp+'.inheritsTransform',0)
cmds.rename(IkTailHandle[1], 'c_tailSolverEffector')
cmds.rename(IkTailHandle[2], 'c_tailSolverCurve')

# create clusters for the tail...
cmds.select('c_tailSolverCurve.cv[1:2]')
cls1=cmds.cluster( rel=True, n='tail_root_cls')
cmds.select('c_tailSolverCurve.cv[3:4]')
cls2=cmds.cluster( rel=True, n='tail_mid_cls')
cmds.select('c_tailSolverCurve.cv[5:6]')
cls3=cmds.cluster( rel=True, n='tail_end_cls')
cls1Grp=cmds.group(cls1, n='tailCluster1_GRP')
cls2Grp=cmds.group(cls2, n='tailCluster2_GRP')
cls3Grp=cmds.group(cls3, n='tailCluster3_GRP')

# a left over cv to be static in rig...
cmds.select('c_tailSolverCurve.cv[0]')
cls4=cmds.cluster( rel=True, n='c_neutral_cls')
cls4Grp=cmds.group(cls4, n='c_cluster4_GRP')

# group em...
cmds.parent(cls1Grp,cls2Grp,cls3Grp,cls4Grp,IkHandleGrp)

# create controllers for the tail...
tailCtl1=cmds.circle( nr=(0,0,1), c=(0,0,0), n='c_tailRoot_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(tailCtl1,apply=True,t=1,r=1,s=1,n=0)
lockScale(tailCtl1[0])
yellowcon(tailCtl1[0])
tailCtl1Grp=cmds.group(tailCtl1, n='c_tailRootCtrl_GRP')
tailCtl2=cmds.circle( nr=(0,0,1), c=(0,0,0), n='c_tailMid_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(tailCtl2,apply=True,t=1,r=1,s=1,n=0)
lockScale(tailCtl2[0])
yellowcon(tailCtl2[0])
tailCtl2Grp=cmds.group(tailCtl2, n='c_tailMidCtrl_GRP')
tailCtl3=cmds.circle( nr=(0,0,1), c=(0,0,0), n='c_tailPoint_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(tailCtl3,apply=True,t=1,r=1,s=1,n=0)
lockScale(tailCtl3[0])
yellowcon(tailCtl3[0])
tailCtl3Grp=cmds.group(tailCtl3, n='c_tailPointCtrl_GRP')

# place controllers...
cmds.setAttr(tailCtl1Grp+'.rx',rotation)
cmds.setAttr(tailCtl2Grp+'.rx',rotation)
cmds.setAttr(tailCtl3Grp+'.rx',rotation)
clsXform=cmds.xform(cls1[1], piv=True, q=True)
cmds.setAttr(tailCtl1Grp+'.tx',clsXform[0])
cmds.setAttr(tailCtl1Grp+'.ty',clsXform[1])
cmds.setAttr(tailCtl1Grp+'.tz',clsXform[2])
clsXform=cmds.xform(cls2[1], piv=True, q=True)
cmds.setAttr(tailCtl2Grp+'.tx',clsXform[0])
cmds.setAttr(tailCtl2Grp+'.ty',clsXform[1])
cmds.setAttr(tailCtl2Grp+'.tz',clsXform[2])
clsXform=cmds.xform(cls3[1], piv=True, q=True)
cmds.setAttr(tailCtl3Grp+'.tx',clsXform[0])
cmds.setAttr(tailCtl3Grp+'.ty',clsXform[1])
cmds.setAttr(tailCtl3Grp+'.tz',clsXform[2])

# connect tail controllers...
cmds.parentConstraint(tailCtl1,cls1, mo=True, n='c_tailRoot_controller')
cmds.parentConstraint(tailCtl2,cls2, mo=True, n='c_tailMid_controller')
cmds.parentConstraint(tailCtl3,cls3, mo=True, n='c_tailPoint_controller')

# tail FK controllers...
tailFkCtl1=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='c_tail1FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(tailFkCtl1,apply=True,t=1,r=1,s=1,n=0)
lockScale(tailFkCtl1)
tailFkCtlGrp=cmds.group(tailFkCtl1, n='c_tailFkCtrl1_GRP')
tailFkCtl2=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='c_tail2FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(tailFkCtl2,apply=True,t=1,r=1,s=1,n=0)
lockScale(tailFkCtl2)
tailFkCtl2Grp=cmds.group(tailFkCtl2, n='c_tailFkCtrl2_GRP')
rotation=cmds.getAttr(tailCtl1Grp+'.rx')
cmds.setAttr(tailFkCtlGrp+'.rx',rotation)
cmds.setAttr(tailFkCtl2Grp+'.rx',rotation)
constr=cmds.pointConstraint(tailCtl1,tailFkCtlGrp)
cmds.delete(constr)
constr=cmds.pointConstraint(tailCtl2,tailFkCtl2Grp)
cmds.delete(constr)

# place pivot at tail root...
coordinate=cmds.xform(tail1, ws=True, t=True, q=True)
cmds.xform(tailFkCtl1, piv=(coordinate), ws=True)
cmds.parent(tailFkCtl2Grp, tailFkCtl1)
cmds.parent(tailCtl1Grp, tailFkCtl1)
cmds.parent(tailCtl2Grp,tailFkCtl2)
cmds.parent(tailCtl3Grp, tailFkCtl2)

# group the tail elements...
tailGrp=cmds.group(tailRootJnt, IkHandleGrp, tailFkCtlGrp, n='c_tailRig_GRP')
cmds.setAttr(IkHandleGrp+'.visibility', 0)

# parentConstraint the neutral cluster to make tail follow the parent group and enable scaling...
cmds.parentConstraint(tailFkCtl1,cls4, mo=True)

# twist and no twist
mult=cmds.shadingNode('multiplyDivide', asUtility=True, n='c_tailTwist_reverseValueRotation_multiply')
cmds.setAttr(mult+'.input2X',-1)
cmds.connectAttr(tailCtl3[0]+'.rz',mult+'.input1X')
cmds.connectAttr(mult+'.outputX', IkTailHandle[0]+'.twist')


''' create spine/spine module '''
''' create spine/spine module '''
# meassure the distance between joints and get spine root placement...
dist=cmds.createNode('distanceDimShape', n='delete_me_my_boy')
spineStart=cmds.xform(hindPelvis,q=True,ws=True,rp=True)
spineEnd=cmds.xform(frontPelvis,q=True,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(spineEnd))
cmds.setAttr(dist+'.startPoint',*(spineStart))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist, p=True))
# joints in chain...
initialAmmountOfJoints=8
#
ammountOfJoints=initialAmmountOfJoints-1
cmds.select(d=True)
spineRootJnt=cmds.joint(n='c_spine9_JNT')
while ammountOfJoints > 0:
    spineJnt=cmds.joint(n='c_spine'+str(ammountOfJoints)+'_JNT')
    ammountOfJoints-=1
cmds.select(spineRootJnt, hi=True)
spineJointChain=cmds.ls(sl=True)
# calculate translation distance between each joint...
ammountOfJoints=initialAmmountOfJoints-1
distancePerJoint=distance/ammountOfJoints
for e in spineJointChain:
    cmds.setAttr(e+'.tz',-distancePerJoint)
cmds.setAttr(spineRootJnt+'.tz',0)
cmds.rename(spineJointChain[-1],spineJointChain[-1]+'End')
constr=cmds.pointConstraint(frontPelvis,spineJointChain[0])

# rotate joint to aim for the end of the chain...
tempcon=cmds.aimConstraint(hindPelvis,spineRootJnt, aimVector=(0,0,-1))
rotation=cmds.getAttr(spineRootJnt+'.rx')
cmds.delete(tempcon)
cmds.parent(spineJointChain[1],w=True)
cmds.setAttr(spineRootJnt+'.rx',0)
cmds.setAttr(spineRootJnt+'.ry',0)
cmds.setAttr(spineRootJnt+'.rz',0)
cmds.parent(spineJointChain[1],spineRootJnt)
cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True)

# create IK solver...
IkspineHandle=cmds.ikHandle(sol='ikSplineSolver', ns=4, n='c_spineSolver_IK', sj=spineRootJnt, ee=spineJointChain[-1]+'End')
IkHandleGrp=cmds.group(IkspineHandle[0],IkspineHandle[2], n='C_IK_spineSystem_GRP' )
cmds.setAttr(IkHandleGrp+'.inheritsTransform',0)
cmds.rename(IkspineHandle[1], 'c_spineSolverEffector')
cmds.rename(IkspineHandle[2], 'c_spineSolverCurve')

# create clusters for the spine...
cmds.select('c_spineSolverCurve.cv[1:2]')
cls1=cmds.cluster( rel=True, n='spine_root_cls')
cmds.select('c_spineSolverCurve.cv[3:4]')
cls2=cmds.cluster( rel=True, n='spine_mid_cls')
cmds.select('c_spineSolverCurve.cv[5:6]')
cls3=cmds.cluster( rel=True, n='spine_end_cls')
cls1Grp=cmds.group(cls1, n='spineCluster1_GRP')
cls2Grp=cmds.group(cls2, n='spineCluster2_GRP')
cls3Grp=cmds.group(cls3, n='spineCluster3_GRP')

# a left over cv to be static in rig...
cmds.select('c_spineSolverCurve.cv[0]')
cls4=cmds.cluster( rel=True, n='c_neutral_cls')
cls4Grp=cmds.group(cls4, n='c_cluster4_GRP')

# group em...
cmds.parent(cls1Grp,cls2Grp,cls3Grp,cls4Grp,IkHandleGrp)

# create controllers for the spine...
spineCtl1=cmds.circle( nr=(0,0,1), c=(0,0,0), n='c_spineRoot_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(spineCtl1,apply=True,t=1,r=1,s=1,n=0)
lockScale(spineCtl1[0])
yellowcon(spineCtl1[0])
spineCtl1Grp=cmds.group(spineCtl1, n='c_spineRootCtrl_GRP')
spineCtl2=cmds.circle( nr=(0,0,1), c=(0,0,0), n='c_spineMid_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(spineCtl2,apply=True,t=1,r=1,s=1,n=0)
lockScale(spineCtl2[0])
yellowcon(spineCtl2[0])
spineCtl2Grp=cmds.group(spineCtl2, n='c_spineMidCtrl_GRP')
spineCtl3=cmds.circle( nr=(0,0,1), c=(0,0,0), n='c_spinePoint_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(spineCtl3,apply=True,t=1,r=1,s=1,n=0)
lockScale(spineCtl3[0])
yellowcon(spineCtl3[0])
spineCtl3Grp=cmds.group(spineCtl3, n='c_spinePointCtrl_GRP')

# place controllers...
cmds.setAttr(spineCtl1Grp+'.rx',rotation)
cmds.setAttr(spineCtl2Grp+'.rx',rotation)
cmds.setAttr(spineCtl3Grp+'.rx',rotation)
clsXform=cmds.xform(cls1[1], piv=True, q=True)
cmds.setAttr(spineCtl1Grp+'.tx',clsXform[0])
cmds.setAttr(spineCtl1Grp+'.ty',clsXform[1])
cmds.setAttr(spineCtl1Grp+'.tz',clsXform[2])
clsXform=cmds.xform(cls2[1], piv=True, q=True)
cmds.setAttr(spineCtl2Grp+'.tx',clsXform[0])
cmds.setAttr(spineCtl2Grp+'.ty',clsXform[1])
cmds.setAttr(spineCtl2Grp+'.tz',clsXform[2])
clsXform=cmds.xform(cls3[1], piv=True, q=True)
cmds.setAttr(spineCtl3Grp+'.tx',clsXform[0])
cmds.setAttr(spineCtl3Grp+'.ty',clsXform[1])
cmds.setAttr(spineCtl3Grp+'.tz',clsXform[2])

# connect spine controllers...
cmds.parentConstraint(spineCtl1,cls1, mo=True, n='c_spineRoot_controller')
cmds.parentConstraint(spineCtl2,cls2, mo=True, n='c_spineMid_controller')
cmds.parentConstraint(spineCtl3,cls3, mo=True, n='c_spinePoint_controller')

# spine FK controllers...
spineFkCtl1=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='c_spine1FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(spineFkCtl1,apply=True,t=1,r=1,s=1,n=0)
lockScale(spineFkCtl1)
spineFkCtlGrp=cmds.group(spineFkCtl1, n='c_spineFkCtrl1_GRP')
spineFkCtl2=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='c_spine2FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(spineFkCtl2,apply=True,t=1,r=1,s=1,n=0)
lockScale(spineFkCtl2)
spineFkCtl2Grp=cmds.group(spineFkCtl2, n='c_spineFkCtrl2_GRP')
rotation=cmds.getAttr(spineCtl1Grp+'.rx')
cmds.setAttr(spineFkCtlGrp+'.rx',rotation)
cmds.setAttr(spineFkCtl2Grp+'.rx',rotation)
constr=cmds.pointConstraint(spineCtl1,spineFkCtlGrp)
cmds.delete(constr)
constr=cmds.pointConstraint(spineCtl2,spineFkCtl2Grp)
cmds.delete(constr)

# connect spine end to hind JNT...
cmds.parentConstraint(spineCtl1[0],spineCtl2Grp, mo=True)
cmds.parentConstraint(spineCtl3[0],spineCtl2Grp, mo=True)
cmds.parentConstraint(spineCtl1[0],frontPelvisJnt, mo=True)
cmds.parentConstraint(spineCtl3[0],hindPelvisJnt, mo=True)
cmds.parentConstraint(spineCtl3[0],tailFkCtlGrp, mo=True)

# master spine controller...
spineMasterCtrl=cmds.curve(d=1, p=[(0.5,0.5,0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,-0.5,-0.5),(0.5,-0.5,-0.5),(0.5,0.5,-0.5),(-0.5,0.5,-0.5),(-0.5,0.5,0.5),(0.5,0.5,0.5),(0.5,-0.5,0.5),(0.5,-0.5,-0.5),(-0.5,-0.5,-0.5),(-0.5,-0.5,0.5),(0.5,-0.5,0.5),(-0.5,-0.5,0.5),(-0.5,0.5,0.5)], k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],n='c_spineMaster_CTRL')
cmds.scale(distance/4,distance/4,distance*1.5)
cmds.makeIdentity(spineMasterCtrl, apply=True, t=1, r=1, s=1, n=0)
spineMasterCtrlGrp=cmds.group(spineMasterCtrl, n='c_spineMasterCtrl_GRP')
constr=cmds.pointConstraint(spineFkCtl2, spineMasterCtrlGrp)
cmds.delete(constr)
dist=cmds.getAttr(spineMasterCtrlGrp+'.ty')
cmds.setAttr(spineMasterCtrlGrp+'.ty',dist*1.5)
cmds.parent(spineFkCtl2Grp, spineFkCtl1)
cmds.parent(spineCtl1Grp, spineFkCtl1)
cmds.parent(spineCtl2Grp,spineFkCtl2)
cmds.parent(spineCtl3Grp, spineFkCtl2)
cmds.parentConstraint(spineCtl1[0],cls4, mo=True)

cmds.setAttr(IkHandleGrp+'.visibility',0)
spineGrp=cmds.group(IkHandleGrp, spineRootJnt, spineFkCtlGrp, n='c_spineRig_GRP')



''' create neck/neck module '''
''' create neck/neck module '''
# meassure the distance between joints and get neck root placement...
dist=cmds.createNode('distanceDimShape', n='delete_me_my_boy')
neckStart=cmds.xform(neckRoot,q=True,ws=True,rp=True)
neckEndPos=cmds.xform(neckEnd,q=True,ws=True,rp=True)
cmds.setAttr(dist+'.endPoint',*(neckEndPos))
cmds.setAttr(dist+'.startPoint',*(neckStart))
distance=cmds.getAttr(dist+'.distance')
cmds.delete(cmds.listRelatives(dist, p=True))
# joints in chain...
initialAmmountOfJoints=8
#
ammountOfJoints=initialAmmountOfJoints-1
cmds.select(d=True)
neckRootJnt=cmds.joint(n='c_neck9_JNT')
while ammountOfJoints > 0:
    neckJnt=cmds.joint(n='c_neck'+str(ammountOfJoints)+'_JNT')
    ammountOfJoints-=1
cmds.select(neckRootJnt, hi=True)
neckJointChain=cmds.ls(sl=True)
# calculate translation distance between each joint...
ammountOfJoints=initialAmmountOfJoints-1
distancePerJoint=distance/ammountOfJoints
for e in neckJointChain:
    cmds.setAttr(e+'.tz',distancePerJoint)
cmds.setAttr(neckRootJnt+'.tz',0)
cmds.rename(neckJointChain[-1],neckJointChain[-1]+'End')
constr=cmds.pointConstraint(neckRoot,neckJointChain[0])

# rotate joint to aim for the end of the chain...
tempcon=cmds.aimConstraint(neckEnd,neckRootJnt, aimVector=(0,0,1))
rotation=cmds.getAttr(neckRootJnt+'.rx')
cmds.delete(tempcon)
cmds.parent(neckJointChain[1],w=True)
cmds.setAttr(neckRootJnt+'.rx',0)
cmds.setAttr(neckRootJnt+'.ry',0)
cmds.setAttr(neckRootJnt+'.rz',0)
cmds.parent(neckJointChain[1],neckRootJnt)
cmds.joint(e=True, zso=True, oj='xyz', secondaryAxisOrient='yup', ch=True)

# create IK solver...
IkneckHandle=cmds.ikHandle(sol='ikSplineSolver', ns=4, n='c_neckSolver_IK', sj=neckRootJnt, ee=neckJointChain[-1]+'End')
IkHandleGrp=cmds.group(IkneckHandle[0],IkneckHandle[2], n='C_IK_neckSystem_GRP' )
cmds.setAttr(IkHandleGrp+'.inheritsTransform',0)
cmds.rename(IkneckHandle[1], 'c_neckSolverEffector')
cmds.rename(IkneckHandle[2], 'c_neckSolverCurve')

# create clusters for the neck...
cmds.select('c_neckSolverCurve.cv[1:2]')
cls1=cmds.cluster( rel=True, n='neck_root_cls')
cmds.select('c_neckSolverCurve.cv[3:4]')
cls2=cmds.cluster( rel=True, n='neck_mid_cls')
cmds.select('c_neckSolverCurve.cv[5:6]')
cls3=cmds.cluster( rel=True, n='neck_end_cls')
cls1Grp=cmds.group(cls1, n='neckCluster1_GRP')
cls2Grp=cmds.group(cls2, n='neckCluster2_GRP')
cls3Grp=cmds.group(cls3, n='neckCluster3_GRP')

# a left over cv to be static in rig...
cmds.select('c_neckSolverCurve.cv[0]')
cls4=cmds.cluster( rel=True, n='c_neutral_cls')
cls4Grp=cmds.group(cls4, n='c_cluster4_GRP')

# group em...
cmds.parent(cls1Grp,cls2Grp,cls3Grp,cls4Grp,IkHandleGrp)

# create controllers for the neck...
neckCtl1=cmds.circle( nr=(0,0,1), c=(0,0,0), n='c_neckRoot_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(neckCtl1,apply=True,t=1,r=1,s=1,n=0)
lockScale(neckCtl1[0])
yellowcon(neckCtl1[0])
neckCtl1Grp=cmds.group(neckCtl1, n='c_neckRootCtrl_GRP')
neckCtl2=cmds.circle( nr=(0,0,1), c=(0,0,0), n='c_neckMid_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(neckCtl2,apply=True,t=1,r=1,s=1,n=0)
lockScale(neckCtl2[0])
yellowcon(neckCtl2[0])
neckCtl2Grp=cmds.group(neckCtl2, n='c_neckMidCtrl_GRP')
neckCtl3=cmds.circle( nr=(0,0,1), c=(0,0,0), n='c_neckPoint_CTRL')
cmds.scale(distance/3,distance/3,distance/3)
cmds.makeIdentity(neckCtl3,apply=True,t=1,r=1,s=1,n=0)
lockScale(neckCtl3[0])
yellowcon(neckCtl3[0])
neckCtl3Grp=cmds.group(neckCtl3, n='c_neckPointCtrl_GRP')

# place controllers...
cmds.setAttr(neckCtl1Grp+'.rx',rotation)
cmds.setAttr(neckCtl2Grp+'.rx',rotation)
cmds.setAttr(neckCtl3Grp+'.rx',rotation)
clsXform=cmds.xform(cls1[1], piv=True, q=True)
cmds.setAttr(neckCtl1Grp+'.tx',clsXform[0])
cmds.setAttr(neckCtl1Grp+'.ty',clsXform[1])
cmds.setAttr(neckCtl1Grp+'.tz',clsXform[2])
clsXform=cmds.xform(cls2[1], piv=True, q=True)
cmds.setAttr(neckCtl2Grp+'.tx',clsXform[0])
cmds.setAttr(neckCtl2Grp+'.ty',clsXform[1])
cmds.setAttr(neckCtl2Grp+'.tz',clsXform[2])
clsXform=cmds.xform(cls3[1], piv=True, q=True)
cmds.setAttr(neckCtl3Grp+'.tx',clsXform[0])
cmds.setAttr(neckCtl3Grp+'.ty',clsXform[1])
cmds.setAttr(neckCtl3Grp+'.tz',clsXform[2])

# connect neck controllers...
cmds.parentConstraint(neckCtl1,cls1, mo=True, n='c_neckRoot_controller')
cmds.parentConstraint(neckCtl2,cls2, mo=True, n='c_neckMid_controller')
cmds.parentConstraint(neckCtl3,cls3, mo=True, n='c_neckPoint_controller')

# neck FK controllers...
neckFkCtl1=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='c_neck1FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(neckFkCtl1,apply=True,t=1,r=1,s=1,n=0)
lockScale(neckFkCtl1)
neckFkCtlGrp=cmds.group(neckFkCtl1, n='c_neckFkCtrl1_GRP')
neckFkCtl2=cmds.curve(d=1, p=[(1,0,-1),(-1,0,-1),(-1,0,1),(1,0,1),(1,0,-1)], k=[0,1,2,3,4], n='c_neck2FK_CTRL')
cmds.scale(distance/4,distance/4,distance/4)
cmds.makeIdentity(neckFkCtl2,apply=True,t=1,r=1,s=1,n=0)
lockScale(neckFkCtl2)
neckFkCtl2Grp=cmds.group(neckFkCtl2, n='c_neckFkCtrl2_GRP')
rotation=cmds.getAttr(neckCtl1Grp+'.rx')
cmds.setAttr(neckFkCtlGrp+'.rx',rotation)
cmds.setAttr(neckFkCtl2Grp+'.rx',rotation)
constr=cmds.pointConstraint(neckCtl1,neckFkCtlGrp)
cmds.delete(constr)
constr=cmds.pointConstraint(neckCtl2,neckFkCtl2Grp)
cmds.delete(constr)

# move neck root pivot and parent controllers...
coordinate=cmds.xform(neckRoot, ws=True, t=True, q=True)
cmds.xform(neckFkCtl1, piv=(coordinate), ws=True)
cmds.parent(neckFkCtl2Grp, neckFkCtl1)
cmds.parent(neckCtl1Grp, neckFkCtl1)
cmds.parent(neckCtl2Grp,neckFkCtl2)
cmds.parent(neckCtl3Grp, neckFkCtl2)
cmds.parentConstraint(spineFkCtl1,neckFkCtlGrp,mo=True)
cmds.parentConstraint(spineFkCtl1,cls4,mo=True)

# cleanup...
cmds.setAttr(IkHandleGrp+'.visibility',0)
neckGrp=cmds.group(neckRootJnt,IkHandleGrp,neckFkCtlGrp, n='c_neckRig_GRP')



''' create foot rool module '''
''' create foot rool module '''
# l side hind...
cmds.select(d=True)
LHAnkleRotate=cmds.joint(n='l_hindAnkleRotate_JNT')
LHHeelJnt=cmds.joint(n='l_hindHeelRool_JNT')
LHBallJnt=cmds.joint(n='l_hindBallRool_JNT')
LHAnkleJnt=cmds.joint(n='l_hindAnkleRool_JNT')
constr=cmds.pointConstraint(L_hindAnkleJnt, LHAnkleRotate)
cmds.delete(constr)
constr=cmds.pointConstraint(L_hindToeJnt, LHHeelJnt)
cmds.delete(constr)
cmds.setAttr(LHHeelJnt+'.tz',0)
constr=cmds.pointConstraint(L_hindToeJnt, LHBallJnt)
cmds.delete(constr)
constr=cmds.pointConstraint(L_hindAnkleJnt, LHAnkleJnt)
cmds.delete(constr)
cmds.parent(L_Ik[0], LHAnkleJnt)
cmds.parent(L_IkToe[0], LHBallJnt)
coordinate=cmds.xform(LHAnkleRotate, ws=True, t=True, q=True)
cmds.xform(L_hindIkCtl, piv=(coordinate), ws=True)
LHHeelCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='l_hindHeel_CTRL')
LHHeelCtrlGrp=cmds.group(n='l_hindHeelCtrl_GRP')
constr=cmds.pointConstraint(LHHeelJnt, LHHeelCtrl[0])
cmds.delete(constr)
LHToeTipCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='l_hindToeTip_CTRL')
LHToeTipCtrlGrp=cmds.group(n='l_hindToeTipCtrl_GRP')
constr=cmds.pointConstraint(LHBallJnt, LHToeTipCtrlGrp)
cmds.delete(constr)
cmds.parent(LHToeTipCtrlGrp, LHHeelCtrl[0])
cmds.parentConstraint(LHHeelCtrl[0], LHHeelJnt, mo=True)
cmds.parentConstraint(LHToeTipCtrl[0], LHBallJnt, mo=True)
cmds.parent(LHHeelCtrlGrp, L_hindIkCtl)
cmds.parentConstraint(L_hindIkCtl, LHAnkleRotate, mo=True)
cmds.setAttr(LHAnkleRotate+'.visibility',0)
# r side hind...
cmds.select(d=True)
RHAnkleRotate=cmds.joint(n='r_hindAnkleRotate_JNT')
RHHeelJnt=cmds.joint(n='r_hindHeelRool_JNT')
RHBallJnt=cmds.joint(n='r_hindBallRool_JNT')
RHAnkleJnt=cmds.joint(n='r_hindAnkleRool_JNT')
constr=cmds.pointConstraint(R_hindAnkleJnt, RHAnkleRotate)
cmds.delete(constr)
constr=cmds.pointConstraint(R_hindToeJnt, RHHeelJnt)
cmds.delete(constr)
cmds.setAttr(RHHeelJnt+'.tz',0)
constr=cmds.pointConstraint(R_hindToeJnt, RHBallJnt)
cmds.delete(constr)
constr=cmds.pointConstraint(R_hindAnkleJnt, RHAnkleJnt)
cmds.delete(constr)
cmds.parent(R_Ik[0], RHAnkleJnt)
cmds.parent(R_IkToe[0], RHBallJnt)
coordinate=cmds.xform(RHAnkleRotate, ws=True, t=True, q=True)
cmds.xform(R_hindIkCtl, piv=(coordinate), ws=True)
RHHeelCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='r_hindHeel_CTRL')
RHHeelCtrlGrp=cmds.group(n='r_hindHeelCtrl_GRP')
constr=cmds.pointConstraint(RHHeelJnt, RHHeelCtrl[0])
cmds.delete(constr)
RHToeTipCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='r_hindToeTip_CTRL')
RHToeTipCtrlGrp=cmds.group(n='r_hindToeTipCtrl_GRP')
constr=cmds.pointConstraint(RHBallJnt, RHToeTipCtrlGrp)
cmds.delete(constr)
cmds.parent(RHToeTipCtrlGrp, RHHeelCtrl[0])
cmds.parentConstraint(RHHeelCtrl[0], RHHeelJnt, mo=True)
cmds.parentConstraint(RHToeTipCtrl[0], RHBallJnt, mo=True)
cmds.parent(RHHeelCtrlGrp, R_hindIkCtl)
cmds.parentConstraint(R_hindIkCtl, RHAnkleRotate, mo=True)
cmds.setAttr(RHAnkleRotate+'.visibility',0)
# l front leg...
cmds.select(d=True)
LFAnkleRotate=cmds.joint(n='l_frontAnkleRotate_JNT')
LFHeelJnt=cmds.joint(n='l_frontHeelRool_JNT')
LFBallJnt=cmds.joint(n='l_frontBallRool_JNT')
LFAnkleJnt=cmds.joint(n='l_frontAnkleRool_JNT')
constr=cmds.pointConstraint(L_frontAnkleJnt, LFAnkleRotate)
cmds.delete(constr)
constr=cmds.pointConstraint(L_frontToeJnt, LFHeelJnt)
cmds.delete(constr)
cmds.setAttr(LFHeelJnt+'.tz',0)
constr=cmds.pointConstraint(L_frontToeJnt, LFBallJnt)
cmds.delete(constr)
constr=cmds.pointConstraint(L_frontAnkleJnt, LFAnkleJnt)
cmds.delete(constr)
cmds.parent(L_FIk[0], LFAnkleJnt)
cmds.parent(L_FToeIk[0], LFBallJnt)
coordinate=cmds.xform(LFAnkleRotate, ws=True, t=True, q=True)
cmds.xform(L_frontIkCtl, piv=(coordinate), ws=True)
LFHeelCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='l_frontHeel_CTRL')
LFHeelCtrlGrp=cmds.group(n='l_frontHeelCtrl_GRP')
constr=cmds.pointConstraint(LFHeelJnt, LFHeelCtrl[0])
cmds.delete(constr)
LFToeTipCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='l_frontToeTip_CTRL')
LFToeTipCtrlGrp=cmds.group(n='l_frontToeTipCtrl_GRP')
constr=cmds.pointConstraint(LFBallJnt, LFToeTipCtrlGrp)
cmds.delete(constr)
cmds.parent(LFToeTipCtrlGrp, LFHeelCtrl[0])
cmds.parentConstraint(LFHeelCtrl[0], LFHeelJnt, mo=True)
cmds.parentConstraint(LFToeTipCtrl[0], LFBallJnt, mo=True)
cmds.parent(LFHeelCtrlGrp, L_frontIkCtl)
cmds.parentConstraint(L_frontIkCtl, LFAnkleRotate, mo=True)
cmds.setAttr(LFAnkleRotate+'.visibility',0)
# r front leg...
cmds.select(d=True)
RFAnkleRotate=cmds.joint(n='r_frontAnkleRotate_JNT')
RFHeelJnt=cmds.joint(n='r_frontHeelRool_JNT')
RFBallJnt=cmds.joint(n='r_frontBallRool_JNT')
RFAnkleJnt=cmds.joint(n='r_frontAnkleRool_JNT')
constr=cmds.pointConstraint(R_frontAnkleJnt, RFAnkleRotate)
cmds.delete(constr)
constr=cmds.pointConstraint(R_frontToeJnt, RFHeelJnt)
cmds.delete(constr)
cmds.setAttr(RFHeelJnt+'.tz',0)
constr=cmds.pointConstraint(R_frontToeJnt, RFBallJnt)
cmds.delete(constr)
constr=cmds.pointConstraint(R_frontAnkleJnt, RFAnkleJnt)
cmds.delete(constr)
cmds.parent(R_FIk[0], RFAnkleJnt)
cmds.parent(R_FToeIk[0], RFBallJnt)
coordinate=cmds.xform(RFAnkleRotate, ws=True, t=True, q=True)
cmds.xform(R_frontIkCtl, piv=(coordinate), ws=True)
RFHeelCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='r_frontHeel_CTRL')
RFHeelCtrlGrp=cmds.group(n='r_frontHeelCtrl_GRP')
constr=cmds.pointConstraint(RFHeelJnt, RFHeelCtrl[0])
cmds.delete(constr)
RFToeTipCtrl=cmds.circle(nr=(1,0,0), r=distance/4, n='r_frontToeTip_CTRL')
RFToeTipCtrlGrp=cmds.group(n='r_frontToeTipCtrl_GRP')
constr=cmds.pointConstraint(RFBallJnt, RFToeTipCtrlGrp)
cmds.delete(constr)
cmds.parent(RFToeTipCtrlGrp, RFHeelCtrl[0])
cmds.parentConstraint(RFHeelCtrl[0], RFHeelJnt, mo=True)
cmds.parentConstraint(RFToeTipCtrl[0], RFBallJnt, mo=True)
cmds.parent(RFHeelCtrlGrp, R_frontIkCtl)
cmds.parentConstraint(R_frontIkCtl, RFAnkleRotate, mo=True)
cmds.setAttr(RFAnkleRotate+'.visibility',0)

roolJntGrp=cmds.group(LFAnkleRotate,RFAnkleRotate,LHAnkleRotate,RHAnkleRotate, n='c_footRoolJnt_GRP')

# constraint front leg translation ctrl to IK controller...
constrpoint=cmds.parentConstraint(frontPelvisJnt, L_frontLegTranslateGrp, mo=True)
cmds.parentConstraint(L_frontLegTranslate, L_frontFemurJntIk, mo=True)
cmds.parentConstraint(L_frontIkCtl, L_frontLegTranslateGrp, mo=True)
cmds.setAttr(constrpoint[0]+'.l_frontIK_CTRLW1',.3)
constrpoint=cmds.parentConstraint(frontPelvisJnt, R_frontLegTranslateGrp, mo=True)
cmds.parentConstraint(R_frontLegTranslate, R_frontFemurJntIk, mo=True)
cmds.parentConstraint(R_frontIkCtl, R_frontLegTranslateGrp, mo=True)
cmds.setAttr(constrpoint[0]+'.r_frontIK_CTRLW1',.3)


# nullify placement locators...
cmds.delete(mainLocGrp)

''' cleanup '''
''' cleanup '''
# group body...
cmds.parent(spineGrp, spineMasterCtrl)
rigGrp=cmds.group(tailGrp,legCtlGrp,legSwitchGrp,spineMasterCtrlGrp,neckGrp, n='c_rig_GRP')
jntGrp=cmds.group(roolJntGrp,hindPelvisJnt,frontPelvisJnt,tailRootJnt,spineRootJnt,neckRootJnt, n='c_jnt_GRP')

cmds.parent(rigGrp,jntGrp,subworld)
cmds.setAttr(L_hindFemurJntIk+'.visibility',0)
cmds.setAttr(R_hindFemurJntIk+'.visibility',0)
cmds.setAttr(L_frontFemurJntIk+'.visibility',0)
cmds.setAttr(R_frontFemurJntIk+'.visibility',0)
cmds.setAttr(L_hindFemurJntFk+'.visibility',0)
cmds.setAttr(R_hindFemurJntFk+'.visibility',0)
cmds.setAttr(L_frontFemurJntFk+'.visibility',0)
cmds.setAttr(R_frontFemurJntFk+'.visibility',0)


''' stretchy spine '''
''' stretchy spine '''
baseLoc=cmds.spaceLocator(n='baseSpine_LOC')
poseLoc=cmds.spaceLocator(n='poseSpine_LOC')
targetLoc=cmds.spaceLocator(n='targetSpine_LOC')
cmds.setAttr(baseLoc[0]+'.visibility',0)
cmds.setAttr(poseLoc[0]+'.visibility',0)
cmds.setAttr(targetLoc[0]+'.visibility',0)
cmds.parent(baseLoc, spineJointChain[0], r=True)
cmds.parent(targetLoc, hindPelvisJnt, r=True)
cmds.parent(poseLoc, hindPelvisJnt, r=True)
spineStretchGrp=cmds.group(baseLoc[0], poseLoc[0], targetLoc[0], n='c_spineDistanceReader_GRP')
cmds.pointConstraint(spineCtl3[0], poseLoc[0], sk=('x','y'), mo=True)


dist=cmds.createNode('distanceDimShape', n='distanceMasterSpine')
cmds.connectAttr(baseLoc[0]+'.worldPosition[0]', dist+'.startPoint')
cmds.connectAttr(poseLoc[0]+'.worldPosition[0]', dist+'.endPoint')

dist2=cmds.createNode('distanceDimShape', n='distancePoseSpine')
cmds.connectAttr(baseLoc[0]+'.worldPosition[0]', dist2+'.startPoint')
cmds.connectAttr(targetLoc[0]+'.worldPosition[0]', dist2+'.endPoint')

divide=cmds.shadingNode('multiplyDivide', asUtility=True, n='stretchSpine_divideWithScale')
cmds.setAttr(divide+'.operation', 2)
cmds.connectAttr(dist+'.distance', divide+'.input1X')
cmds.connectAttr(dist2+'.distance', divide+'.input2X')
cmds.addAttr(baseLoc[0], longName='output_value', at='enum', en=('____'), max=1, min=0, k=True)
cmds.setAttr(baseLoc[0]+'.output_value', lock=True)
cmds.addAttr(baseLoc[0], longName='distance', at='float', k=True)
cmds.connectAttr(divide+'.outputX', baseLoc[0]+'.distance')
nonShape=cmds.listRelatives(dist, p=True)
cmds.setAttr(nonShape[0]+'.visibility', 0)
nonShape=cmds.rename(nonShape[0], 'distanceMaster_DST')
nonShape2=cmds.listRelatives(dist2, p=True)
cmds.setAttr(nonShape2[0]+'.visibility', 0)
nonShape2=cmds.rename(nonShape2[0], 'distancePose_DST')
for e in spineJointChain:
    try:
        cmds.connectAttr(baseLoc[0]+'.distance', e+'.scaleX')
    except:
        print 'spine end jnt ignored'
cmds.parent(nonShape, nonShape2, spineStretchGrp)
cmds.parent(spineStretchGrp, spineGrp)
cmds.select(d=True) 

