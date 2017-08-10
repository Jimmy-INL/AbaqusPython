# -*- coding: mbcs -*-

from interaction import *
from optimization import *
from sketch import *
from visualization import *
from connectorBehavior import *

import regionToolset

#session.journalOptions.setValues(replayGeometry=COORDINATE,recoverGeometry=COORDINATE)

beamLength=4.0
cLoad=10000	#only refers to scale

#-----------------------------------------------------

# Create a model.

myModel = mdb.Model(name='ssBeamModel')

#-----------------------------------------------------

from part import *

# Create a sketch for the base feature.
	
mySketch = myModel.ConstrainedSketch(name='beamSketch',sheetSize=10.0)

# Create the line.

mySketch.Line(point1=(0.0, 0.0), point2=(beamLength/2, 0.0))

mySketch.Line(point1=(beamLength/2, 0.0), point2=(beamLength, 0.0))
	
# Create a three-dimensional, deformable part.

myBeamPart = myModel.Part(name='beamPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)
	
# Create the part's base feature
myBeamPart.BaseWire(sketch=mySketch)

#-----------------------------------------------------

from material import *

# Create a material.

#mySteel = myModel.Material(name='Steel')

# Create the elastic properties

#elasticProperties = (209.E9, 0.28)
#mySteel.Elastic(table=(elasticProperties, ) )


#-------------------------------------------------------

from section import *
# Create the beam section.

myModel.IProfile(name='IProfile', b1=0.1, b2=0.1, h=0.2, l=0.1,
    t1=0.01, t2=0.01, t3=0.01)

mySection=myModel.BeamSection(name='beamSection', profile='IProfile',
    poissonRatio=0.28, integration=BEFORE_ANALYSIS,
	table=((210000000000.0, 82030000000.0), ), alphaDamping=0.0, beamShape=CONSTANT,
    betaDamping=0.0, centroid=(0.0, 0.0), compositeDamping=0.0,
	consistentMassMatrix=False, dependencies=0, shearCenter=(0.0, 0.0),
	temperatureDependency=OFF, thermalExpansion=OFF)
	
# Assign the section to the region. The region refers 
# to the single cell in this model.

#mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
#    offsetField='', offsetType=MIDDLE_SURFACE, region=
#    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName=
#    'Section-1', thicknessAssignment=FROM_SECTION)

#beamRegion = (myBeamPart.cells,)
beamRegion=regionToolset.Region(edges=myBeamPart.edges)

myBeamPart.SectionAssignment(region=beamRegion, sectionName='beamSection',
    offset=0.0, offsetField='',offsetType=MIDDLE_SURFACE,
	thicknessAssignment=FROM_SECTION)
	
myModel.parts['beamPart'].assignBeamSectionOrientation(method=
    N1_COSINES, n1=(0.0, 0.0, 1.0), region=Region(
    edges=myBeamPart.edges.findAt(((0.5, 0.0, 0.0), 
    ), ((2.5, 0.0, 0.0), ), )))

#-------------------------------------------------------

from assembly import *

# Create a part instance.
myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)
myInstance = myAssembly.Instance(name='beamInstance',
    part=myBeamPart, dependent=OFF)

#-------------------------------------------------------

from step import *

# Create a step. The time period of the static step is 1.0, 
# and the initial incrementation is 0.1; the step is created
# after the initial step. 

myModel.StaticStep(name='beamStep', previous='Initial',
    nlgeom=OFF, description='Load of the beam.')

#-------------------------------------------------------

from load import *

#mdb.models['Model-1'].rootAssembly.Set(name='Set-1', vertices=
#    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((
#    0.0, 0.0, 0.0), )))

#v=myAssembly.instances('beamInstance').vertices
#verts=v.findAt(((0.0, 0.0, 0.0), ),)

v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt(((0.0, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts,name='Set-fix1')
	
#mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
#    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
#    'BC-1', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'], u1=0.0, 
#    u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET)

region=myAssembly.sets['Set-fix1']



myModel.DisplacementBC(name='BC-1', createStepName='beamStep',
    region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
	amplitude=UNSET, fixed=OFF, distributionType=UNIFORM,fieldName='',
    localCsys=None)
	
#mdb.models['Model-1'].rootAssembly.Set(name='Set-2', vertices=
#    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((
#    4.0, 0.0, 0.0), )))

v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt(((beamLength, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts, name='Set-fix2')

#mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
#    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
#    'BC-2', region=mdb.models['Model-1'].rootAssembly.sets['Set-2'], u1=UNSET, 
#    u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET)

region=myAssembly.sets['Set-fix2']
	
myModel.DisplacementBC(name='BC-2', createStepName='beamStep',
    region=region, u1=UNSET, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=UNSET,
	amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
	localCsys=None)
	
#mdb.models['Model-1'].rootAssembly.Set(name='Set-3', vertices=
#    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.findAt(((
#   2.0, 0.0, 0.0), )))
	
v=myAssembly.instances['beamInstance'].vertices
verts=v.findAt(((beamLength/2, 0.0, 0.0), ),)
myAssembly.Set(vertices=verts, name='Set-force')

region=myAssembly.sets['Set-force']

myModel.ConcentratedForce(name='beamLoad', createStepName='beamStep',
    region=region, cf2=-1.0*cLoad, distributionType=UNIFORM, field='',
    localCsys=None)
#-------------------------------------------------------

from mesh import *
	
# Assign an element type to the part instance.
#region = (myInstance.cells,)
#elemType = mesh.ElemType(elemCode=B31, elemLibrary=STANDARD)
#myAssembly.setElementType(regions=region, elemTypes=(elemType,))

# Seed the part instance.
myAssembly.seedPartInstance(regions=(myInstance,), size=0.2,
    deviationFactor=0.1, minSizeFactor=0.1)
	
# Mesh the part instance.
myAssembly.generateMesh(regions=(myInstance,))

#-------------------------------------------------------

myAssembly.regenerate()
#-------------------------------------------------------

from job import *
# Create an analysis job for the model and submit it.

jobName='ssBeam'

myJob=mdb.Job(name=jobName, model='ssBeamModel')
	
myJob.submit(consistencyChecking=OFF)


# Save by ldn
