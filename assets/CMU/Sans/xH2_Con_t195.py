# state file generated using paraview version 5.11.0
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [2379, 1149]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [1525.0, 1525.0, 5595.25]
renderView1.UseLight = 0
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [3465.409723422402, 4011.5647965734815, 1904.149762574992]
renderView1.CameraFocalPoint = [1674.5379721496936, 1416.1526018609875, 5591.262996212552]
renderView1.CameraViewUp = [-0.514481278901163, -0.5633803558005951, -0.6464608173417926]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 2224.533111126917
renderView1.UseColorPaletteForBackground = 0
renderView1.Background = [1.0, 1.0, 1.0]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(2379, 1149)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Cylinder'
cylinder1 = Cylinder(registrationName='Cylinder1')
cylinder1.Resolution = 152
cylinder1.Height = 700.0
cylinder1.Radius = 10.0

# create a new 'Transform'
transform2 = Transform(registrationName='Transform2', Input=cylinder1)
transform2.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform2.Transform.Translate = [1525.0, 1675.0, 5400.0]
transform2.Transform.Rotate = [90.0, 0.0, 0.0]
transform2.Transform.Scale = [0.9999999999999932, 1.0, 0.9999999999999833]

# create a new 'PVD Reader'
cc2pcornerpointpvd = PVDReader(registrationName='cc2pcornerpoint.pvd', FileName='/home/shogeweg/Documents/Dumux/Hogeweg2022a/dumux/dumux-ite/build-cmake/test/porousmediumflow/2pncgeobio/cornerpoint/cc2pcornerpoint.pvd')
cc2pcornerpointpvd.CellArrays = ['S_liq', 'p_liq', 'rho_liq', 'mob_liq', 'S_gas', 'p_gas', 'rho_gas', 'mob_gas', 'pc', 'porosity', 'x^SimpleH2O_liq', 'x^CH4_liq', 'x^CO2_liq', 'x^H2_liq', 'x^N2_liq', 'x^H2S_liq', 'x^SO4_liq', 'rhoMolar_liq', 'x^SimpleH2O_gas', 'x^CH4_gas', 'x^CO2_gas', 'x^H2_gas', 'x^N2_gas', 'x^H2S_gas', 'x^SO4_gas', 'rhoMolar_gas', 'phase presence', 'precipitateVolumeFraction^Pyrite', 'precipitateVolumeFraction^Pyrrhotite', 'n_MG', 'n_SR', 'process rank', 'PERMX [mD]', 'PERMY [mD]', 'PERMZ [mD]']

# create a new 'Transform'
transform1 = Transform(registrationName='Transform1', Input=cc2pcornerpointpvd)
transform1.Transform = 'Transform'

# init the 'Transform' selected for 'Transform'
transform1.Transform.Scale = [1.0, 1.0, 5.0]

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=transform1)
threshold1.Scalars = ['CELLS', 'x^H2_gas']
threshold1.LowerThreshold = 0.05
threshold1.UpperThreshold = 0.1

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=transform1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['CELLS', 'PERMX [mD]']
clip1.Value = 368.364614456892
clip1.Crinkleclip = 1

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [1575.0, 1575.0, 5880.400146484375]
clip1.ClipType.Normal = [0.5, 0.5, 0.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [1525.0, 1525.0, 5880.400146484375]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from clip1
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'xH2_gas'
xH2_gasTF2D = GetTransferFunction2D('xH2_gas')
xH2_gasTF2D.ScalarRangeInitialized = 1
xH2_gasTF2D.Range = [0.0, 0.1, 0.0, 1.0]

# get color transfer function/color map for 'xH2_gas'
xH2_gasLUT = GetColorTransferFunction('xH2_gas')
xH2_gasLUT.AutomaticRescaleRangeMode = 'Never'
xH2_gasLUT.TransferFunction2D = xH2_gasTF2D
xH2_gasLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.05, 0.865003, 0.865003, 0.865003, 0.1, 0.705882, 0.0156863, 0.14902]
xH2_gasLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'xH2_gas'
xH2_gasPWF = GetOpacityTransferFunction('xH2_gas')
xH2_gasPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.1, 1.0, 0.5, 0.0]
xH2_gasPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip1Display.Representation = 'Surface With Edges'
clip1Display.ColorArrayName = ['CELLS', 'x^H2_gas']
clip1Display.LookupTable = xH2_gasLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'None'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 305.0
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 15.25
clip1Display.SetScaleArray = [None, '']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = [None, '']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = xH2_gasPWF
clip1Display.ScalarOpacityUnitDistance = 138.82992596603617
clip1Display.OpacityArrayName = ['CELLS', 'PERMX [mD]']
clip1Display.SelectInputVectors = [None, '']
clip1Display.WriteLog = ''

# show data from transform2
transform2Display = Show(transform2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
transform2Display.Representation = 'Surface'
transform2Display.AmbientColor = [0.0, 0.0, 0.0]
transform2Display.ColorArrayName = [None, '']
transform2Display.DiffuseColor = [0.0, 0.0, 0.0]
transform2Display.SelectTCoordArray = 'TCoords'
transform2Display.SelectNormalArray = 'Normals'
transform2Display.SelectTangentArray = 'None'
transform2Display.OSPRayScaleArray = 'Normals'
transform2Display.OSPRayScaleFunction = 'PiecewiseFunction'
transform2Display.SelectOrientationVectors = 'None'
transform2Display.ScaleFactor = 50.02728881835938
transform2Display.SelectScaleArray = 'None'
transform2Display.GlyphType = 'Arrow'
transform2Display.GlyphTableIndexArray = 'None'
transform2Display.GaussianRadius = 2.501364440917969
transform2Display.SetScaleArray = ['POINTS', 'Normals']
transform2Display.ScaleTransferFunction = 'PiecewiseFunction'
transform2Display.OpacityArray = ['POINTS', 'Normals']
transform2Display.OpacityTransferFunction = 'PiecewiseFunction'
transform2Display.DataAxesGrid = 'GridAxesRepresentation'
transform2Display.PolarAxes = 'PolarAxesRepresentation'
transform2Display.SelectInputVectors = ['POINTS', 'Normals']
transform2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
transform2Display.ScaleTransferFunction.Points = [-0.9998477101325989, 0.0, 0.5, 0.0, 0.9998477101325989, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
transform2Display.OpacityTransferFunction.Points = [-0.9998477101325989, 0.0, 0.5, 0.0, 0.9998477101325989, 1.0, 0.5, 0.0]

# show data from threshold1
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface With Edges'
threshold1Display.ColorArrayName = ['CELLS', 'x^H2_gas']
threshold1Display.LookupTable = xH2_gasLUT
threshold1Display.SelectTCoordArray = 'None'
threshold1Display.SelectNormalArray = 'None'
threshold1Display.SelectTangentArray = 'None'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = 305.0
threshold1Display.SelectScaleArray = 'None'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'None'
threshold1Display.GaussianRadius = 15.25
threshold1Display.SetScaleArray = [None, '']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = [None, '']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = xH2_gasPWF
threshold1Display.ScalarOpacityUnitDistance = 122.46260676944041
threshold1Display.OpacityArrayName = ['CELLS', 'PERMX [mD]']
threshold1Display.SelectInputVectors = [None, '']
threshold1Display.WriteLog = ''

# setup the color legend parameters for each legend in this view

# get color legend/bar for xH2_gasLUT in view renderView1
xH2_gasLUTColorBar = GetScalarBar(xH2_gasLUT, renderView1)
xH2_gasLUTColorBar.WindowLocation = 'Upper Right Corner'
xH2_gasLUTColorBar.Title = '$x^{H_2}_{gas}$, [-]'
xH2_gasLUTColorBar.ComponentTitle = ''
xH2_gasLUTColorBar.HorizontalTitle = 1
xH2_gasLUTColorBar.TitleFontFamily = 'File'
xH2_gasLUTColorBar.TitleFontFile = '/home/shogeweg/Templates/CMU/Sans/cmunss.ttf'
xH2_gasLUTColorBar.TitleFontSize = 60
xH2_gasLUTColorBar.LabelFontFamily = 'File'
xH2_gasLUTColorBar.LabelFontFile = '/home/shogeweg/Templates/CMU/Sans/cmunss.ttf'
xH2_gasLUTColorBar.LabelFontSize = 55
xH2_gasLUTColorBar.ScalarBarThickness = 25
xH2_gasLUTColorBar.ScalarBarLength = 0.8
xH2_gasLUTColorBar.UseCustomLabels = 1
xH2_gasLUTColorBar.CustomLabels = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09]
xH2_gasLUTColorBar.RangeLabelFormat = '%-#6.1f'

# set color bar visibility
xH2_gasLUTColorBar.Visibility = 1

# show color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# restore active source
SetActiveSource(threshold1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')