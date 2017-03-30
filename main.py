import numpy
from matplotlib.pyplot import *
from neuron import h,gui
from destexheCell import *



h.dt = 0.05
npoints = 200000

tstop = npoints * h.dt
h.runStopAt = tstop
h.steps_per_ms = 1/h.dt
h.celsius = 36
h.v_init = -70

cell = destexheCell()

fl = h.Gfluct2(cell.soma(0.5))
fl.std_e = 0.012               
fl.std_i = 0.0264

v_vec = h.Vector()
t_vec = h.Vector()
v_vec.record(cell.soma(0.5)._ref_v)
t_vec.record(h._ref_t)


h.tstop = tstop
h.run()


savdata = h.File()
savdata.wopen('m_pot_python.dat')
for i in range(0, len(v_vec)):
        savdata.printf("%f\n", v_vec[i])

plot(t_vec, v_vec, color = 'black')
xlabel('Tempo [ms]')
ylabel('Potencial de Membrana')

