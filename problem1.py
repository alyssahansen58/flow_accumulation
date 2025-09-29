import matplotlib.pyplot as plt
import arcpy

elevation =  r'C:\GEOG4860_AlyssaHansen\Week_08\Week_08\data\cach_ned10_clip_int.img'
flow_raster = r'C:\GEOG4860_AlyssaHansen\Week_08\Week_08\data\flowoutput.tif'
flow_plot = r'C:\GEOG4860_AlyssaHansen\Week_08\Week_08\data\flowplot.png'
cutoff = 1000

# Check out spatial analyst
arcpy.CheckOutExtension('spatial')

# make elevation a raster to use in flow direction
fd = arcpy.Raster(elevation)
# run flow direction tool
flowdirect = arcpy.sa.FlowDirection(fd)

# run flowaccum
flowaccum = arcpy.sa.FlowAccumulation(flow_raster)
# save flow accum
flowaccum.save(flow_raster)
arcpy.Raster(flow_raster)

# min, max, renamed value
# float('inf') is a floating point value that represents poistive infinity
# this means that the max is any number greater than the cutoff
values = [[0, cutoff, 0],
         [(cutoff+1), 999999999, 1]] 
remap = arcpy.sa.RemapRange(values)
arcpy.sa.Reclassify(flow_raster, 'VALUE', remap).save('flow_raster')

# raster to numpy
numpy_reclass = arcpy.RasterToNumPyArray(flow_raster)

# save with imsave
plt.imsave(flow_plot, numpy_reclass, cmap= 'gray_r')


plt.imshow(numpy_reclass, cmap='gray')

# Show the plot
plt.show()
