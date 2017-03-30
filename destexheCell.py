# Destexhe cell class
from neuron import h, gui

class destexheCell(object):
	'''
		This cell constains only a soma.
	'''
	def __init__(self):
		self.create_sections()
        	self.build_subsets()
        	self.define_geometry()
        	self.define_biophysics()
	#
	def create_sections(self):
		"""Create the sections of the cell."""
        # NOTE: cell=self is required to tell NEURON of this object.
		self.soma = h.Section(name = 'soma', cell = self)

	#
	def define_geometry(self):
		"""Set the 3D geometry of the cell."""
		self.soma.L     = 105   # microns
		self.soma.diam  = 105   # microns
		h.define_shape() # Translate into 3D points.

	#
	def define_biophysics(self):
		"""Assign the membrane properties across the cell."""
		# Insert passive properties
		self.soma.insert('pas')
		self.soma.g_pas = 4.52e-5
		self.soma.e_pas = -80
		self.soma.cm = 1
		self.soma.Ra = 250
		# Insert ionic chanels
		self.soma.insert("inaT")
		self.soma.ena = 50
		self.soma.vtraub_inaT = -63
		self.soma.gnabar_inaT = 20e-4
		self.soma.insert('ikdT')
		self.soma.ek = -90
		self.soma.vtraub_ikdT = -63
		self.soma.gkbar_ikdT = 200e-4
		self.soma.insert('imZ')
		self.soma.ek = -90
		self.soma.gkbar_imZ = 3e-4
		self.soma.gnabar_inaT = 4.3 * 120e-4
		self.soma.gkbar_ikdT = 100e-4
		self.soma.gkbar_imZ = 5e-4
		self.soma.shift_inaT = -10
		self.soma.vtraub_inaT = -63
		self.soma.vtraub_ikdT = -63

	#
	def build_subsets(self):
		''' Build subsets lists. For now we define all.'''
		self.all = h.SectionList()
		self.all.wholetree(sec = self.soma)
