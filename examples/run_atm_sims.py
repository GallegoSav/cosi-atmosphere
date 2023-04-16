# Imports:
from MassModels import MakeMassModels
from RunSims import Simulate 
from ProcessSims import Process

# Make mass model:
instance = MakeMassModels("Atmosphere.BestCrabDay.txt")
instance.plot_atmosphere()
instance.get_cart_vectors(angle, altitude)
instance.rectangular_model()
instance.spherical_model()

# Run sim:
instance = Simulate()
instance.run_sim("AtmospherePencilBeam.source", seed=3000)
instance.parse_sim_file("Atmosphere_PencilBeam.inc1.id1.sim")

# Process sim:
instance = Process(theta)
instance.bin_sim()
instance.make_scattering_plots()
instance.calc_tp()
instance.get_total_edisp_matrix()
model_flux=instance.PL_interp(2)
instance.ff_correction(model_flux)