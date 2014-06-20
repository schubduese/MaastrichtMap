#!/usr/bin/env python

#from  mapnik import *
#m = Map(18000,9000)
#m.background = Color('steelblue')
#s = Style()
#r = Rule()
#polygon_symbolizer = PolygonSymbolizer(Color('#f2eff9'))
#r.symbols.append(polygon_symbolizer)
#line_symbolizer = LineSymbolizer(Color('rgb(50%,50%,50%)'),0.1)
#r.symbols.append(line_symbolizer)
#s.rules.append(r)
#m.append_style('My Style',s)
##ds = Shapefile(file='ne_110m_admin_0_countries.shp')
#ds = PostGIS(host='10.3.0.1',user='osmuser',password='blub1234',dbname='osmmaastricht',table='planet_osm_polygon')
#layer = Layer('world')
#layer.datasource = ds
#layer.styles.append('My Style')
#m.layers.append(layer)
#m.zoom_all()
#render_to_file(m,'world.png', 'png')
#print "rendered image to 'world.png'"

#import mapnik
#m = mapnik.Map(9000,3000)
#m.background = mapnik.Color('steelblue')
#s = mapnik.Style()
#r = mapnik.Rule()
#polygon_symbolizer = mapnik.PolygonSymbolizer(mapnik.Color('#f2eff9'))
#r.symbols.append(polygon_symbolizer)
#line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('rgb(50%,50%,50%)'),0.1)
#r.symbols.append(line_symbolizer)
#s.rules.append(r)
#m.append_style('My Style',s)
##ds = Shapefile(file='ne_110m_admin_0_countries.shp')
#ds = mapnik.PostGIS(host='10.3.0.1',user='osmuser',password='blub1234',dbname='osmmaastricht',table='planet_osm_polygon')
#layer = mapnik.Layer('world')
#layer.datasource = ds
#layer.styles.append('My Style')
#m.layers.append(layer)
#m.zoom_all()
#mapnik.render_to_file(m,'world.png', 'png')
#print "rendered image to 'world.png'"






import mapnik
stylesheet = 'maastricht.xml'
image = 'maastricht.png'
m = mapnik.Map(8000, 4000)
mapnik.load_map(m, stylesheet)
m.zoom_all() 
mapnik.render_to_file(m, image)
print "rendered image to '%s'" % image

