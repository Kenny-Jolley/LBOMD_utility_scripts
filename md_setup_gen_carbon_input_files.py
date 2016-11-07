#!/usr/bin/env python

#  This script generates a default set of input files for the LBOMD code.
#  These input files are for carbon systems using the Reaxff potential.

#~~  Note: We do not generate the structure file, lattice.dat, here!!  ~~

import os, sys

def md_setup_gen_carbon_input_files():
    print("  +---------------------------------------------------------+")
    print("  | Generate generic input files for a ReaxFF carbon system |")
    print("  +---------------------------------------------------------+\n")
    print("~~ Generating input files ~~\n")
    print(" Generic copies of:")
    print("   buck.IN")
    print("   collisions.IN")
    print("   conjugate_gradient.IN")
    print("   control")
    print("   dpmta.IN")
    print("   equilibration.IN")
    print("   lattice.IN")
    print("   lbomd.IN")
    print("   potfor.IN")
    print("   ffield  May 2016 version")
    print(" ~~ DONE ~~")
    print(" NOW: Check and edit the input files for your potential / simulation job. \n")
    print(" Note: The structure file, lattice.dat, is not generated here!!")
    print(" You must also provide LBOMD.exe\n")

    # buck.IN
    # not needed for carbon, but needs to be present.
    # remove existing file if present.
    if (os.path.isfile("buck.IN")):
        os.remove('buck.IN')
    # Generate file
    outfile = open('buck.IN', 'w')
    outfile.write("F         /* Extra output (spline coefficients, etc...)\n")
    outfile.write("22        /* Number of species.  Format: Number (id), Atomic number, ZBL number, Charge\n")
    outfile.write("1     8    8.0    -2.0        /* O_\n")
    outfile.write("2    12    12.0    2.0        /* Mg\n")
    outfile.write("3    72    72.0    4.0        /* Hf\n")
    outfile.write("4    68    68.0    3.0        /* Er\n")
    outfile.write("5    22    22.0    4.0        /* Ti\n")
    outfile.write("6    66    66.0    3.0        /* Dy\n")
    outfile.write("7    13    13.0    3.0        /* Al\n")
    outfile.write("8    31    31.0    0.0        /* Ga\n")
    outfile.write("9    49    49.0    3.0        /* In\n")
    outfile.write("10   18    18.0    0.0        /* Ar\n")
    outfile.write("11   79    79.0    0.0        /* Au\n")
    outfile.write("12   58    58.0    4.0        /* Ce\n")
    outfile.write("13   40    40.0    4.0        /* Zr\n")
    outfile.write("14   14    14.0    0.0        /* Si\n")
    outfile.write("15   54    54.0    0.0        /* Xe\n")
    outfile.write("16    6     6.0    0.0        /* C_\n")
    outfile.write("17   39    39.0    3.0        /* Y_\n")
    outfile.write("18   94    94.0    0.0        /* Pu\n")
    outfile.write("19    1     1.0    0.0        /* H_\n")
    outfile.write("20    2     2.0    0.0        /* He\n")
    outfile.write("21   47    47.0    0.0        /* Ag\n")
    outfile.write("22   30    30.0    0.0        /* Zn\n")
    outfile.write("45        /* Number of interactions. Format: \"ID A, ID B, Type, A, rho, C, R1, R2, R3, Spline offset\"\n")
    outfile.write("19  20  1   0.0006          0               3.0862          0.5       2.5       5.5       0         /* H_-He LJ\n")
    outfile.write("20  1   1   2.400014734     0.0             0.015386425     2.0       3.5       7.4       50        /* He-O (L-J)\n")
    outfile.write("18  19  0   0               1               0               2.0       3.5       3.8       1         /* Pu-H_ (ZBL)\n")
    outfile.write("8   19  0   0               1               0               2.0       3.5       3.8       1         /* Ga-H_ (ZBL)\n")
    outfile.write("17  17  0   0               1               0               0.5       1.77      7.4       50        /* Y-Y\n")
    outfile.write("1   17  0   1345.6          0.3491          0.0             0.55      1.4       7.4       50        /* Y-O\n")
    outfile.write("1   1   0   22764.0         0.149           27.88           0.5       1.05      7.4       0         /* O-O\n")
    outfile.write("2   1   0   1428.5          0.29450         0               0.3       0.8       7.4       0         /* Mg-O (from MgO potential)\n")
    outfile.write("2   2   0   0               1               0               0.5       1.05      1.3       0         /* Mg-Mg\n")
    outfile.write("3   2   0   0               1               0               0.4       1.05      1.4       0         /* Hf-Mg\n")
    outfile.write("3   1   0   1492.60         0.34780         7.60            0.3       0.9       7.4       100       /* Hf-O\n")
    outfile.write("3   3   0   0               1               0               0.2       0.8       1.1       0         /* Hf-Hf\n")
    outfile.write("10  10  1   0.0104          1               3.4             2.1       3.0       7.4       0         /* Ar-Ar (L-J)\n")
    outfile.write("10  5   0   0               1               0               2.0       4.0       4.3       1         /* Ti-Ar\n")
    outfile.write("10  1   0   0               1               0               0.5       2.2       2.5       50        /* Ar-O\n")
    outfile.write("15  14  0   0               1               0               0.5       2.0       2.3       1         /* Xe-Si\n")
    outfile.write("15  15  0   0               1               0               0.5       2.2       2.5       1         /* Xe-Xe\n")
    outfile.write("16  10  0   0               1               0               0.7       2.3       2.6       1         /* C_-Ar\n")
    outfile.write("14  10  0   0               1               0               0.7       2.3       2.6       1         /* Si-Ar\n")
    outfile.write("10  11  0   0               1               0               1.2       2.5       2.8       50        /* Ar-Au\n")
    outfile.write("4   4   0   0               1               0               0.3       0.9       1.14      0         /* Er-Er (from Er2Ti2O7 potential)\n")
    outfile.write("4   1   0   1739.91         0.3389          17.55           0.6       1.7       7.4       50.0      /* Er-O (from Er2Ti2O7 potential)\n")
    outfile.write("4   5   0   0               1               0               0.2       0.9       1.14      0         /* Er-Ti\n")
    outfile.write("5   5   0   0               1               0               0.2       0.8       1.14      0         /* Ti-Ti\n")
    outfile.write("5   1   0   2131.04         0.3038          0               0.4       1.0       7.4       50.0      /* Ti-O\n")
    outfile.write("2   7   0   0               1               0               0.3       1.05      1.3       0         /* Mg-Al\n")
    outfile.write("7   7   0   0               1               0               0.3       1.05      1.3       0         /* Al-Al\n")
    outfile.write("7   1   0   1374.79         0.3013          0               0.15      0.65      5.0       0         /* Al-O\n")
    outfile.write("2   9   0   0               1               0               0.3       1.05      1.3       0         /* Mg-In\n")
    outfile.write("9   9   0   0               1               0               0.3       1.05      1.3       0         /* In-In\n")
    outfile.write("9   1   0   1595.65         0.32960         7.402           0.45      1.1       5.0       1000      /* In-O (100 % inverted, with van der waals term)\n")
    outfile.write("10  2   0   0               1               0               0.5       1.5       1.8       50        /* Ar-Mg\n")
    outfile.write("10  3   0   0               1               0               0.5       1.5       1.8       50        /* Ar-Hf\n")
    outfile.write("6   6   0   0               1               0               0.8       1.5       1.8       0         /* Dy-Dy\n")
    outfile.write("6   1   0   1807.84         0.3393          18.77           0.5       1.25      7.4       50.0      /* Dy-O\n")
    outfile.write("11  3   0   0               1               0               0.5       1.5       1.8       50        /* Au-Hf\n")
    outfile.write("11  2   0   0               1               0               0.5       1.5       1.8       50        /* Au-Mg\n")
    outfile.write("11  1   0   0               1               0               0.5       1.5       1.8       50        /* Au-O\n")
    outfile.write("13  1   0   1502.11         0.3477          5.1             0.4       1.0       7.4       100       /* Zr-O, Grimes\n")
    outfile.write("13  13  0   0               1               0               0.4       1.0       1.3       0         /* Zr-Zr, full charge (+4)\n")
    outfile.write("12  1   0   1809.68         0.3547          20.40           0.4       1.2       7.4       100       /* Ce-O\n")
    outfile.write("12  12  0   0               1               0               0.4       1.0       1.3       0         /* Ce-Ce\n")
    outfile.write("10  14  0   0               1               0               0.5       1.2       1.5       50        /* Ar-Si\n")
    outfile.write("21  1   2   0.333           1.618           2.590           0.6       1.4       6.0       1.057     /* Ag-O_\n")
    outfile.write("21  22  2   0.389279502     1.629119759     3.254305777     0.4       0.9       2.80      1.5       /* Ag-Zn\n")
    outfile.write("\n")
    outfile.write("/* parameters...\n")
    outfile.write("/* Type: 0 = Buckingham (or pure ZBL if Buckingham parameters are set to zero)\n")
    outfile.write("/*       1 = Lennard-Jones\n")
    outfile.write("/*       2 = Morse\n")
    outfile.write("/*       3 = Morse (different form)\n")
    outfile.write("\n")
    outfile.write("/* alternatives...\n")
    outfile.write("\n")
    outfile.write("18  19  3   1.18            7.5             2.326           0.2       2.2       3.6       10        /* Pu-H_ (Morse)\n")
    outfile.write("8   19  3   1.18            7.5             2.326           0.2       2.2       3.6       10        /* Ga-H_ (Morse)\n")
    outfile.write("\n")
    outfile.write("18  19  0   0               1               0               2.0       3.5       3.8       1         /* Pu-H_ (ZBL)\n")
    outfile.write("8   19  0   0               1               0               2.0       3.5       3.8       1         /* Ga-H_ (ZBL)\n")
    outfile.close()


    # collisions.IN
    # This file specify collision parameters, default 0 eV collision
    # remove existing file if present.
    if (os.path.isfile("collisions.IN")):
        os.remove('collisions.IN')
    # Generate file
    outfile = open('collisions.IN', 'w')
    outfile.write("2 3 5        /* INDX (TYPICALLY: 235 or 153)\n")
    outfile.write("0.0          /* PROJECTIL_KE (in eV)\n")
    outfile.write("T            /* SEARCH_FOR_PKA (PKA = PRIMARY KNOCK-ON ATOM)\n")
    outfile.write("0.2 0.2 0.2  /* approximate PKA_SITE in lattice units (x*LX,y*LY,z*LZ)\n")
    outfile.write("C_           /* PKA atom symbol\n")
    outfile.write("0            /* Timestep method: 0=variable (KE, default), 1=variable (speed), 2=fixed\n")
    outfile.close()


    # conjugate_gradient.IN
    # This file contains default options for the conjugate gradient method.
    # remove existing file if present.
    if (os.path.isfile("conjugate_gradient.IN")):
        os.remove('conjugate_gradient.IN')
    # Generate file
    outfile = open('conjugate_gradient.IN', 'w')
    outfile.write("5.0E-01     /* accuracy in line search: epsilon_linesearch (A)\n")
    outfile.write("energ       /* monitor convergence in : energy (energ) ; force (force) : < 5 characters>\n")
    outfile.write("1.0E-04     /* termination criterion  : epsilon_force (infinity norm) (ev/A)\n")
    outfile.write("1.0E-04     /* termination criterion  : epsilon_energy (eV)\n")
    outfile.close()


    # control
    # This file contains default options for the Reaxff potential.
    # remove existing file if present.
    if (os.path.isfile("control")):
        os.remove('control')
    # Generate file
    outfile = open('control', 'w')
    outfile.write("# General parameters\n")
    outfile.write("0.0010       cutof2     BO-cutoff for valency angles and torsion angles\n")
    outfile.write("0.050        cutof3     BO-cutoff for bond order for graphs\n")
    outfile.write("1            ichaen     Charges. 1:include charge energy 0: Do not include charge energy\n")
    outfile.close()

    # dpmta.IN
    # This file contains default options for the dpmta method.
    # remove existing file if present.
    if (os.path.isfile("dpmta.IN")):
        os.remove('dpmta.IN')
    # Generate file
    outfile = open('dpmta.IN', 'w')
    outfile.write("1           /* fpnproc    => no. of processors (deprecated, determines automatically)\n")
    outfile.write("5           /* fpnlevels  => no. of (spatial) decomposition levels : was 5\n")
    outfile.write("5           /* fpmp       => size of multipole expansion (me) : was 4\n")
    outfile.write("4           /* fpmplj     => size of the lj me\n")
    outfile.write("0           /* fpfft      => flag for use of fft enhancements\n")
    outfile.write("4           /* fpfftblk   => fft blocking factor\n")
    outfile.write("0           /* fppbc      => flag for use of pbcs\n")
    outfile.write("0           /* fpkterm    => levels of macroscopic expansion\n")
    outfile.write("0.5         /* fptheta    => separation criteria\n")
    outfile.write("80.0        /* fpv1x      => x-coord for first edge of cell and must be half a lattice unit bigger than the cell\n")
    outfile.write("0.0         /* fpv1y      => y-\n")
    outfile.write("0.0         /* fpv1z      => z-\n")
    outfile.write("0.0         /* fpv2x      => x-coord for second edge of cell\n")
    outfile.write("80.0        /* fpv2y      => y-\n")
    outfile.write("0.0         /* fpv2z      => z-\n")
    outfile.write("0.0         /* fpv3x      => x-coord for third edge of cell\n")
    outfile.write("0.0         /* fpv3y      => y-\n")
    outfile.write("80.0        /* fpv3z      => z-\n")
    outfile.write("40.0        /* fpcenterx  => x-coord of cell center\n")
    outfile.write("40.0        /* fpcentery  => y-\n")
    outfile.write("40.0        /* fpcenterz  => z-\n")
    outfile.write(".T.         /* dpmtaResizeFlag  => resize the box if atoms leave it (essential if running in parallel)\n")
    outfile.close()


    # equilibration.IN
    # This file contains default options for equilibration.
    # remove existing file if present.
    if (os.path.isfile("equilibration.IN")):
        os.remove('equilibration.IN')
    # Generate file
    outfile = open('equilibration.IN', 'w')
    outfile.write(".F.       /* RELAXATION .T. => YES ; .F. => NO\n")
    outfile.write("CONJGD    /* SELECT MINIMIZER (DAMPMD OR CONJGD)\n")
    outfile.write("0000.0    /* RELAXATION  TIME FOR DAMPED MD\n")
    outfile.write("0000.0    /* END TIME FOR THERMALISATION OF FULL SYSTEM (EXCET fixed atoms).\n")
    outfile.write("0000.0    /* END TIME FOR THERMALISATION OF CONSTRAINED SYSTEM (contraints\n")
    outfile.write("          /* are introduced in lattice.IN).\n")
    outfile.close()


    # lattice.IN
    # This file contains default options for lattice constraints.
    # remove existing file if present.
    if (os.path.isfile("lattice.IN")):
        os.remove('lattice.IN')
    # Generate file
    outfile = open('lattice.IN', 'w')
    outfile.write("0\n")
    outfile.write("0\n")
    outfile.write("0\n")
    outfile.write("\n")
    outfile.write("\n")
    outfile.write("2\n")
    outfile.write("    FX  0   5\n")
    outfile.write("    FX  5   0\n")
    outfile.write("2\n")
    outfile.write("    FX  0   5\n")
    outfile.write("    FX  5   0\n")
    outfile.write("2\n")
    outfile.write("    FX  0   5\n")
    outfile.write("    FX  5   0\n")
    outfile.write("\n")
    outfile.write("\n")
    outfile.write("    2                 \*NUMBER OF CONSTRAINS ALONG X DIRECTION\n")
    outfile.write("    TH  0  10\n")
    outfile.write("    TH  10  0\n")
    outfile.write("\n")
    outfile.write("    2                 \*NUMBER OF CONSTRAINS ALONG Y DIRECTION\n")
    outfile.write("    TH  0  10\n")
    outfile.write("    TH  10  0\n")
    outfile.write("\n")
    outfile.write("    2                 \*NUMBER OF CONSTRAINS ALONG Z DIRECTION\n")
    outfile.write("    TH  0  10\n")
    outfile.write("    TH  10  0\n")
    outfile.close()

    # lbomd.IN
    # This file contains the default simulation options.
    # remove existing file if present.
    if (os.path.isfile("lbomd.IN")):
        os.remove('lbomd.IN')
    # Generate file
    outfile = open('lbomd.IN', 'w')
    outfile.write("BEGIN          /* BGORCT => BEGIN or CNTIN (RESUME)\n")
    outfile.write("PRODU          /* SIMUSTAGE => EQUIL (EQUILIBRATION) or PRODU (PRODUCTION)\n")
    outfile.write("COLLI          /* SIMUTYPE : COLLI, INDEN\n")
    outfile.write("Graph          /* IDENT  => 5 character identifier of this run\n")
    outfile.write("1 1 1          /* PBCX,PBCY,PBCZ\n")
    outfile.write("5.0            /* PCSKIN => SKIN OF NEB-LIST AS % OF CUTOFF\n")
    outfile.write("1.0            /* DT     => INTEGTATION TIMESTEP (fs)\n")
    outfile.write("1.0            /* RUNTIM => TOTAL RUN TIME (fs) DURING PRODUCTION STAGE\n")
    outfile.write("0              /* FE_FLAG (SET 1 FOR EMBEDDING CONTINUUM)\n")
    outfile.write("0.8302         /* YOUNGS eV/A^3 (REQUIRED FOR MULTISCALE MODEL)\n")
    outfile.write("0.278          /* POISSONS (REQUIRED FOR MULTISCALE MODEL)\n")
    outfile.write("1.438          /* ROE (ATOMIC MASS)/A^3 (REQUIRED FOR MULTISCALE MODEL)\n")
    outfile.write("NO_THERMOSTAT  /* THERMTYPE => THERMOSTAT TYPE (NO_THERMOSTAT,LANGEVIN,NOSE-HOOVER,BERENDSEN..)\n")
    outfile.write("0.0            /* TTEMP => LATTICE TEMPERATURE (K)\n")
    outfile.write("0.0000         /* PTEMP => PROJECTILE/INDENTER TEMPERATURE (K)\n")
    outfile.write("100.00         /* SAFEVR => FAILSAFE FILE EVERY (fs)\n")
    outfile.write("100.00         /* PICEVR => PICTURE FILE OUTPUT EVERY (fs)\n")
    outfile.write(".T.     /* Include atom Kinetic Energy in PIC file\n")
    outfile.write(".T.     /* Include atom Potential Energy in PIC file\n")
    outfile.write(".T.     /* Animation flag\n")
    outfile.write("1.0E16  /* Update animation input every (fs)\n")
    outfile.write("3       /* Ionic systems only: DPMTA = 0; FMMP = 1; TLA = 2; parallel ewald = 3\n")
    outfile.write(".T.     /* Output for NEB\n")
    outfile.write(".F.     /* Output charges in xyz's\n")
    outfile.write(".F.     /* Output velocities in xyz's\n")
    outfile.write(".T.     /* Zip flag\n")
    outfile.write(".F.     /* fix atoms when outside certain range\n")
    outfile.write("100     /* fix atoms when more than this distance away (Ang) (when above is true)\n")
    outfile.write(".F.     /* charge recovery simulation\n")
    outfile.write("100     /* half life to use in charge recovery simulation (fs)\n")
    outfile.write("1.0     /* time step for updating charge recovery sim (fs)\n")
    outfile.write(".F.     /* create backup of FAILSAFE.DAT whenever a new one is written\n")
    outfile.write(".F.     /* Pipe positions in, return energy and forces (single point evaluation only!)\n")
    outfile.write(".F.     /* Minimal file output (only writes animation-reference.xyz)\n")
    outfile.close()


    # potfor.IN
    # This file contains default selection of the potential for each interaction.
    # remove existing file if present.
    if (os.path.isfile("potfor.IN")):
        os.remove('potfor.IN')
    # Generate file
    outfile = open('potfor.IN', 'w')
    outfile.write("/* INPUT FOR POTENTIAL MODULE\n")
    outfile.write("/* INTERACTION TYPES\n")
    outfile.write("3   /* Total number of defined interacting-pair types\n")
    outfile.write("C_    C_     REAXFF\n")
    outfile.write("C_    O_     REAXFF\n")
    outfile.write("O_    O_     REAXFF\n")
    outfile.close()


    # ffield (May 2016 version)
    # This file contains the reaxFF parameters for carbon interactions
    # remove existing file if present.
    if (os.path.isfile("ffield")):
        os.remove('ffield')
    # Generate file
    outfile = open('ffield', 'w')
    outfile.write("Reactive MD-force field: revised C-2013, May 2016\n")
    outfile.write(" 39       ! Number of general parameters\n")
    outfile.write("   50.0000 !Overcoordination parameter\n")
    outfile.write("    9.5469 !Overcoordination parameter\n")
    outfile.write("   26.5405 !Valency angle conjugation parameter\n")
    outfile.write("   -0.8370 !Triple bond stabilisation parameter\n")
    outfile.write("    4.3243 !Triple bond stabilisation parameter\n")
    outfile.write("   70.0000 !C2-correction\n")
    outfile.write("    1.0588 !Undercoordination parameter\n")
    outfile.write("    4.6000 !Triple bond stabilisation parameter\n")
    outfile.write("   12.1176 !Undercoordination parameter\n")
    outfile.write("   13.3056 !Undercoordination parameter\n")
    outfile.write("  -69.4358 !Triple bond stabilization energy\n")
    outfile.write("    0.0000 !Lower Taper-radius\n")
    outfile.write("   10.0000 !Upper Taper-radius\n")
    outfile.write("    2.8793 !Not used\n")
    outfile.write("   33.8667 !Valency undercoordination\n")
    outfile.write("    6.0891 !Valency angle/lone pair parameter\n")
    outfile.write("    1.0563 !Valency angle\n")
    outfile.write("    2.0384 !Valency angle parameter\n")
    outfile.write("    6.1431 !Not used\n")
    outfile.write("    6.9290 !Double bond/angle parameter\n")
    outfile.write("    0.3989 !Double bond/angle parameter: overcoord\n")
    outfile.write("    3.9954 !Double bond/angle parameter: overcoord\n")
    outfile.write("   -2.4837 !Not used\n")
    outfile.write("    5.7796 !Torsion/BO parameter\n")
    outfile.write("   10.0000 !Torsion overcoordination\n")
    outfile.write("    1.9487 !Torsion overcoordination\n")
    outfile.write("   -1.2327 !Conjugation 0 (not used)\n")
    outfile.write("    2.1645 !Conjugation\n")
    outfile.write("    1.5591 !vdWaals shielding\n")
    outfile.write("    0.1000 !Cutoff for bond order (*100)\n")
    outfile.write("    2.1365 !Valency angle conjugation parameter\n")
    outfile.write("    0.6991 !Overcoordination parameter\n")
    outfile.write("   50.0000 !Overcoordination parameter\n")
    outfile.write("    1.8512 !Valency/lone pair parameter\n")
    outfile.write("    0.5000 !Not used\n")
    outfile.write("   20.0000 !Not used\n")
    outfile.write("    5.0000 !Molecular energy (not used)\n")
    outfile.write("    0.0000 !Molecular energy (not used)\n")
    outfile.write("    2.6962 !Valency angle conjugation parameter\n")
    outfile.write("  4    ! Nr of atoms; cov.r; valency;a.m;Rvdw;Evdw;gammaEEM;cov.r2;#\n")
    outfile.write("            alfa;gammavdW;valency;Eunder;Eover;chiEEM;etaEEM;n.u.\n")
    outfile.write("            cov r3;Elp;Heat inc.;n.u.;n.u.;n.u.;n.u.\n")
    outfile.write("            ov/un;val1;n.u.;val3,vval4\n")
    outfile.write(" C_   1.3651   4.0000  12.0000   2.0346   0.1659   0.8485   1.1386   4.0000\n")
    outfile.write("      9.1849   1.5000   4.0000  37.4375  79.5548   4.8446   7.0000   0.0000\n")
    outfile.write("      1.0860   0.0000 181.0000  16.3532  26.3722   4.9538   0.8563   0.0000\n")
    outfile.write("     -5.1769   2.8877   1.0564   4.0000   2.9663   0.0000   0.0000   0.0000\n")
    outfile.write(" H_   0.8930   1.0000   1.0080   1.3550   0.0930   0.8203  -0.1000   1.0000\n")
    outfile.write("      8.2230  33.2894   1.0000   0.0000 121.1250   3.7248   9.6093   1.0000\n")
    outfile.write("     -0.1000   0.0000  61.6606   3.0408   2.4197   0.0003   1.0698   0.0000\n")
    outfile.write("    -19.4571   4.2733   1.0338   1.0000   2.8793   0.0000   0.0000   0.0000\n")
    outfile.write(" O_   1.2450   2.0000  15.9990   2.3890   0.1000   1.0898   1.0548   6.0000\n")
    outfile.write("      9.7300  13.8449   4.0000  37.5000 116.0768   8.5000   8.3122   2.0000\n")
    outfile.write("      0.9049   0.4056  59.0626   3.5027   0.7640   0.0021   0.9745   0.0000\n")
    outfile.write("     -3.5500   2.9000   1.0493   4.0000   2.9225   0.0000   0.0000   0.0000\n")
    outfile.write(" X_  -0.1000   2.0000   1.0080   2.0000   0.0000   0.0100  -0.1000   6.0000\n")
    outfile.write("     10.0000   2.5000   4.0000   0.0000   0.0000   5.00009999.9999   0.0000\n")
    outfile.write("     -0.1000   0.0000  -2.3700   8.7410  13.3640   0.6690   0.9745   0.0000\n")
    outfile.write("    -11.0000   2.7466   1.0338   2.0000   2.8793   0.0000   0.0000   0.0000\n")
    outfile.write("  6      ! Nr of bonds; Edis1;LPpen;n.u.;pbe1;pbo5;13corr;pbo6\n")
    outfile.write("                         pbe2;pbo3;pbo4;n.u.;pbo1;pbo2;ovcorr\n")
    outfile.write("  1  1  86.2088 133.9104  27.9063   0.5462  -0.4603   1.0000  34.9951   0.9667\n")
    outfile.write("         6.1765  -0.1546   7.9966   1.0000  -0.0613   7.8101   1.0000   0.0000\n")
    outfile.write("  1  2 188.8143   0.0000   0.0000  -0.4501   0.0000   1.0000   6.0000   0.5839\n")
    outfile.write("        12.0338   1.0000   0.0000   1.0000  -0.0775   6.1485   0.0000   0.0000\n")
    outfile.write("  2  2 153.3934   0.0000   0.0000  -0.4600   0.0000   1.0000   6.0000   0.7300\n")
    outfile.write("         6.2500   1.0000   0.0000   1.0000  -0.0790   6.0552   0.0000   0.0000\n")
    outfile.write("  1  3 163.3110  83.9973  54.4316  -0.5220  -0.3123   1.0000  10.2503   1.0000\n")
    outfile.write("         0.3553  -0.3757   7.0000   1.0000  -0.1331   4.6021   0.0000   0.0000\n")
    outfile.write("  2  3 160.0000   0.0000   0.0000  -0.5725   0.0000   1.0000   6.0000   0.5626\n")
    outfile.write("         1.1150   1.0000   0.0000   0.0000  -0.0920   4.2790   0.0000   0.0000\n")
    outfile.write("  3  3 142.2858 145.0000  50.8293   0.2506  -0.1000   1.0000  29.7503   0.6051\n")
    outfile.write("         0.3451  -0.1055   9.0000   1.0000  -0.1225   5.5000   1.0000   0.0000\n")
    outfile.write("  3    ! Nr of off-diagonal terms; Ediss;Ro;gamma;rsigma;rpi;rpi2\n")
    outfile.write("  1  2   0.1200   1.3861   9.8561   1.1254  -1.0000  -1.0000\n")
    outfile.write("  1  3   0.1347   1.8343   9.7934   1.3139   1.1498   1.1039\n")
    outfile.write("  2  3   0.0283   1.2885  10.9190   0.9215  -1.0000  -1.0000\n")
    outfile.write(" 18    ! Nr of angles;at1;at2;at3;Thetao,o;ka;kb;pv1;pv2\n")
    outfile.write("  1  1  1  71.4046  20.3586   2.6552   0.0000   0.0197  10.9275   1.1161\n")
    outfile.write("  1  1  2  67.7204  20.0371   3.1168   0.0000   1.2399   0.0000   1.0010\n")
    outfile.write("  2  1  2  71.1440  23.5562   4.7193   0.0000   0.0716   0.0000   2.5936\n")
    outfile.write("  1  1  3  15.7798   9.0805   4.0304   0.0000   1.8785  70.0000   1.1737\n")
    outfile.write("  2  1  3  65.0000  13.4505   1.8249   0.0000   1.5646   0.0000   1.2173\n")
    outfile.write("  3  1  3  74.7266  45.0000   1.8020 -16.7178   2.6091   0.1000   2.3556\n")
    outfile.write("  1  2  2   0.0000   0.0000   6.0000   0.0000   0.0000   0.0000   1.0400\n")
    outfile.write("  1  2  1   0.0000   7.5000   5.0000   0.0000   0.0000   0.0000   1.0400\n")
    outfile.write("  1  2  3   0.0000  45.0000   3.0000   0.0000   1.0000   0.0000   1.0400\n")
    outfile.write("  2  2  2   0.0000  27.9213   5.8635   0.0000   0.0000   0.0000   1.0400\n")
    outfile.write("  2  2  3   0.0000   8.5744   3.0000   0.0000   0.0000   0.0000   1.0421\n")
    outfile.write("  3  2  3   0.0000  15.0000   2.8900   0.0000   0.0000   0.0000   2.8774\n")
    outfile.write("  1  3  1  76.7840  44.2266   0.9343   0.0000   1.3483   0.0000   1.8301\n")
    outfile.write("  1  3  3  63.9120  17.1680   0.8751   0.0000   0.0693  50.9415   3.0000\n")
    outfile.write("  1  3  2  79.6413  28.6488   0.3789   0.0000   1.6776   0.0000   1.0010\n")
    outfile.write("  2  3  2  85.8000   9.8453   2.2720   0.0000   2.8635   0.0000   1.5800\n")
    outfile.write("  2  3  3  79.5453  45.0000   2.1630   0.0000   3.0000   0.0000   1.2391\n")
    outfile.write("  3  3  3  80.7324  30.4554   0.9953   0.0000   1.6310  50.0000   1.0783\n")
    outfile.write(" 26    ! Nr of torsions;at1;at2;at3;at4;;V1;V2;V3;V2(BO);vconj;n.u;n\n")
    outfile.write("  1  1  1  1   1.7987  80.0000   0.2100  -8.6369  -2.1145   0.0000   0.0000\n")
    outfile.write("  1  1  1  2   1.5816  36.2452   0.3067  -5.3163  -1.0125   0.0000   0.0000\n")
    outfile.write("  2  1  1  2   1.5695  28.0133   0.5199  -4.0658  -1.1500   0.0000   0.0000\n")
    outfile.write("  1  1  1  3   0.9963  17.2365   0.1491  -2.5000  -1.0000   0.0000   0.0000\n")
    outfile.write("  2  1  1  3   1.5159  28.6602   0.7169  -7.5489  -3.0000   0.0000   0.0000\n")
    outfile.write("  3  1  1  3  -0.2000  23.6540  -1.0000  -5.9155  -1.1552   0.0000   0.0000\n")
    outfile.write("  1  1  3  1   1.8231  46.5696  -1.0000  -3.0536  -3.0000   0.0000   0.0000\n")
    outfile.write("  1  1  3  2   1.4836  80.0000   0.0363  -4.7349  -1.0000   0.0000   0.0000\n")
    outfile.write("  2  1  3  1   0.5983  49.5033   0.7210  -3.4046  -1.6880   0.0000   0.0000\n")
    outfile.write("  2  1  3  2  -0.2000  76.3511   1.0000  -4.0709  -1.0000   0.0000   0.0000\n")
    outfile.write("  1  1  3  3  -0.2000   5.0000  -1.0000  -3.6523  -2.9000   0.0000   0.0000\n")
    outfile.write("  2  1  3  3   2.5000  80.0000   1.0000  -2.6071  -3.0000   0.0000   0.0000\n")
    outfile.write("  3  1  3  1  -0.2000  80.0000  -1.0000  -3.6863  -3.0000   0.0000   0.0000\n")
    outfile.write("  3  1  3  2   2.5000  38.8954  -0.8368  -4.6681  -2.9000   0.0000   0.0000\n")
    outfile.write("  3  1  3  3  -0.2000  78.1766   0.0250  -2.8895  -3.0000   0.0000   0.0000\n")
    outfile.write("  1  3  3  1   2.5000   0.1000   1.0000  -2.6905  -2.7573   0.0000   0.0000\n")
    outfile.write("  1  3  3  2   0.5241  69.2788  -1.0000  -4.4539  -2.8081   0.0000   0.0000\n")
    outfile.write("  2  3  3  2   2.5000   0.1000  -0.4869  -2.8372  -1.0000   0.0000   0.0000\n")
    outfile.write("  1  3  3  3   2.5000   0.1000   1.0000  -3.4298  -1.0000   0.0000   0.0000\n")
    outfile.write("  2  3  3  3  -0.2000   0.1000  -1.0000  -3.5698  -1.0000   0.0000   0.0000\n")
    outfile.write("  3  3  3  3  -0.2000   0.1000   1.0000  -3.8409  -1.0000   0.0000   0.0000\n")
    outfile.write("  0  1  2  0   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000\n")
    outfile.write("  0  2  2  0   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000\n")
    outfile.write("  0  2  3  0   0.0000   0.1000   0.0200  -2.5415   0.0000   0.0000   0.0000\n")
    outfile.write("  0  1  1  0   0.0000  50.0000   0.3000  -4.0000  -2.0000   0.0000   0.0000\n")
    outfile.write("  0  3  3  0   0.5511  25.4150   1.1330  -5.1903  -1.0000   0.0000   0.0000\n")
    outfile.write("  1    ! Nr of hydrogen bonds;at1;at2;at3;Rhb;Dehb;vhb1\n")
    outfile.write("  3  2  3   2.1200  -3.5800   1.4500  19.5000\n")
    outfile.close()



if __name__ == '__main__':
    md_setup_gen_carbon_input_files()
    sys.exit()



# remove existing file
# gen each file in turn


