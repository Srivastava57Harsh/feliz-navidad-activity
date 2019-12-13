#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Feliz Navidad!
# Saber.py - Devuelve cuantos días faltan para navidad
# Ignacio Rodríguez <nachoel01@gmail.com>
# CeibalJAM! - Uruguay
import gi
gi.require_version('Gtk', '3.0')
from datetime import date
from gi.repository import Gtk
from gi.repository import Gdk
hoy = date.today()
navidad = date(hoy.year,12,24)
anonuevo = date(hoy.year+1,1,1)
faltan = navidad - hoy
faltanc = anonuevo - hoy
def saber():
	if faltan.days == 0:
		return '¡Hoy es Navidad!, Feliz Navidad!'
	elif faltanc.days == 0:
		return 'Feliz año nuevo!'
	else:
		return 'Faltan ' + str(faltan.days) + ' días para navidad y '+ str(faltanc.days-1) + ' días para año nuevo'
def color(label):
	if faltan.days == 0 or faltanc.days == 0: 
		label.modify_fg(Gtk.StateType.NORMAL,Gdk.color_parse('blue'))
	else:
		label.modify_fg(Gtk.StateType.NORMAL,Gdk.color_parse('yellow'))
	label.show_all()
print (saber())
