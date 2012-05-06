# -*- coding: UTF-8 -*-
"""
Aplicacion para localizar coordenadas GPS en formato UTM WGS84, DMS y Decimales.
"""

def latWgs84ToDecimal(lat):
	lat = list(lat)
	lat.insert(3, '.')
	lat = "".join(lat).partition('.')
	return "%s%s%s" % (int(lat[0]), lat[1], lat[2])



def lonWgs84ToDecimal(lon):
	lon = list(lon)
	lon.insert(4, '.')
	lon = "".join(lon).partition('.')
	return "%s%s%s" % (int(lon[0]), lon[1], lon[2])


