===========================================
pyF4all: the Free energies for all library
===========================================

|docs| |devdocs| |usergroup| |developergroup| |pygbe| |nanoshaper| |SIRAH| |Molssi| |BioExcel|

Warning: This library is young. It is a current outcome of a scientific publication on multiscale molecular simulation [MartinezJCIM2020]. By all means, do use it and help improve it, but note that it will change with time, as the main contributors are also increasing, like the SPQR coarse-graining of RNA [spqrNAR2017].

**pyF4all** is an approach to make Poisson Boltzmann (PB) free energy calculations of macromolecular systems easier to perform based on the collaborative pythonic stack. Such calculations help to identify leads for therapies, diagnostics and vaccines of diseases, like COVID-19:

.. raw:: html

   <div align="center">
      <a href="https://github.com/pyF4all/Notebooks_phase1">
         <img height="120px" 
            src="pyF4all_scheme.png"
            alt="pyF4all stack"
            align="center">
      </a>
   </div>
   <br />

The current main features of pyF4all are:

1. Scripts for extracting PB input data from output files of common molecular dynamics (both all-atom and coarse-grained-CG) trajectories such as GROMACS[Gromacs2015], LAMMPS[Lammps1995], ESPResSo++[e++2019], AMBER[Amber2013], VOTCA[Votca2015] among others. Including also the mesh (.face, .vert) creation required by the PB-solver by using e.g. nanoshaper.
2. Jupyter-Notebook interface between PB-solver and the molecular dynamics packages.
3. Development of new methodologies for mapping positions of the coarse-grained particles to the explicit atomistic representations.
4. Estimators and samplers for obtaining the free energies uncertainty of the PB method.

Note also that PB-mediated energy calculations can be performed in a GPU-workstation or small cluster, which broadens the access to molecular simulations researchs also in the regions of the globe wiht less computaional resources.
The particular PB-engine used is [pyGBe](https://github.com/pygbe/pygbe). Biomolecular trajectories, are shared through MoolSSI and BioExcel communities [Amaro2020].

============
References
============

.. [MartinezJCIM2020] Martinez, M., Cooper, C. D., Poma,  A., Guzman, H. V. (2020), Free energies of the disassembly of viral capsids from a multiscale molecular simulation approach, https://doi.org/10.1021/acs.jcim.9b00883.
Journal of Chem. Inf. and Modeling, 60, 2, 974–981.

.. [spqrNAR2017] Poblete, S, Bottaro, S, Bussi, G., A nucleobase-centered coarse-grained representation for structure prediction of RNA motifs, Nucleic Acids Research, (2018) 46,4,1674–1683

.. [Gromacs2015] Abraham, M.J., Murtola, T., Schulz, R., Páll, S., Smith, J.C.,
    Hess, B., and Lindahl, E. (2015). GROMACS: High performance molecular
    simulations through multi-level parallelism from laptops to supercomputers.
    SoftwareX 1–2, 19–25.
    
.. [Lammps1995] Plimpton, S. (1995), Fast parallel algorithms for short-range molecular dynamics, J. Comput. Phys. 117.

.. [e++2019] Guzman, H. V., Tretyakov, N., Kobayashi, H., Kreis, K., Fogarty, A., Kranjak, J., Junghans, C., Kremer, K. 
    and Stuehn,T., ESPResSo++ 2.0: Advanced methods for multiscale molecular simulation, (2019) , Comput. Phys.
    Comm., 238, 66–76.

.. [Amber2013] Salomon-Ferrer, R., Case, D.A., Walker, R.C., (2013), An overview of the Amber biomolecular simulation package. WIREs Comput. Mol. Sci. 3, 198-210.

.. [Votca2015] Mashayak SY, Jochum MN, Koschke K, Aluru NR, Rühle V, Junghans C (2015) Relative Entropy and Optimization-Driven Coarse-Graining Methods in VOTCA. PLoS ONE 10(7): e0131754

.. [Amaro2020] Amaro, R. E. and Mulholland, A. J., (2020)A Community Letter Regarding Sharing Biomolecular Simulation Data for COVID-19, https://doi.org/10.1021/acs.jcim.0c00319.
