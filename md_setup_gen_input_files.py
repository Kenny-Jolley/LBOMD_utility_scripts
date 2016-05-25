#!/usr/bin/env python

#  This script generates a default set of input files for the LBOMD code.
#  These input files are for glass systems.

#~~  Note: We do not generate the structure file, lattice.dat, here!!  ~~

import os

def md_setup_gen_input_files():
    print("~~ Generated input files ~~")
    print(" Note: We do not generate the structure file, lattice.dat, here!!")
    print(" You must also provide LBOMD.exe\n")

    # buck.IN
    # not needed for carbon, but needs to be present.
    # remove existing file if present.
    if (os.path.isfile("buck.IN")):
        os.remove('buck.IN')
    # Generate file
    outfile = open('buck.IN', 'w')
    outfile.write("F         /* Extra output (spline coefficients, etc...)\n")
    outfile.write("23        /* Number of species.  Format: Number (id), Atomic number, ZBL number, Charge\n")
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
    outfile.write("23   15    15.0    3.0        /* P_\n")
    outfile.write("46        /* Number of interactions. Format: \"ID A, ID B, Type, A, rho, C, R1, R2, R3, Spline offset\"\n")
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
    outfile.write("10  14  0   0               1               0               0.5       1.2       1.5       50        /* Ar-Si\n")
    outfile.write("21  1   2   0.333           1.618           2.590           0.6       1.4       6.0       1.057     /* Ag-O_\n")
    outfile.write("21  22  2   0.389279502     1.629119759     3.254305777     0.4       0.9       2.80      1.5       /* Ag-Zn\n")
    outfile.write("23  12  0   0.0              0.1            0.0             0.8       1.45      13.0      0.0       /* P_-Ce\n")
    outfile.write("12  12  0   0.0              0.1            0.0             1.2       2.0       13.0      0.0       /* Ce-Ce\n")
    outfile.write("12  1   0   122500           0.185          0.0             1.1       1.75      13.0      20.0      /* Ce-O_\n")
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
    outfile.write("O_           /* PKA atom symbol\n")
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
    outfile.write("14   /* Total number of defined interacting-pair types\n")
    outfile.write("Fe   Fe    FePO4\n")
    outfile.write("Fe   FF    FePO4\n")
    outfile.write("Fe   O_    FePO4\n")
    outfile.write("Fe   P_    FePO4\n")
    outfile.write("FF   FF    FePO4\n")
    outfile.write("FF   O_    FePO4\n")
    outfile.write("FF   P_    FePO4\n")
    outfile.write("O_   O_    FePO4\n")
    outfile.write("O_   P_    FePO4\n")
    outfile.write("P_   P_    FePO4\n")
    outfile.write("He   He    AzizHe2\n")
    outfile.write("P_   Ce    BPUPOTL\n")
    outfile.write("Ce   Ce    BPUPOTL\n")
    outfile.write("Ce   O_    BPUPOTL\n")
    outfile.close()

if __name__ == '__main__':
    md_setup_gen_input_files()
