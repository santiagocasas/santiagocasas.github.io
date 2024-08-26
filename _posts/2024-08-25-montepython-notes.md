---
layout: post
title: Montepython issues
date: 2024-08-25 08:57:00-0400
description: Montepython problems
tags: cosmology
categories: sample-posts
giscus_comments: true
related_posts: false
---

# GCspectro likelihood

Run technicalities in [[MontePython Oneloop Runs]] 

1. Installation issues:
	1.  Class Oneloop C-code not compatible with older `gcc 9.4`, it is compatible with `gcc~>11.0`  
	2.  Classy does not work with `numpy >=2.0` .  
	3. Montepython requires `numpy>1.23.5`  because of a `scipy.optimize import fsolve`  
2. w0, wa priors are not important in (Analytical Marginalized) AM likelihoods.
3. w0, wa priors are important in full likelihoods, getting constantly errors like: 
   
```
desinomarg.err:48:Error in Class: perturbations_init(L:796) :condition (w_fld_ini >= 0.) is true; The fluid is meant to be negligible at early time, and unimportant for defining the initial conditions of other species. You are using parameters for which this assumption may break down, since at early times you have w_fld(a--->0) = 1.406016e-03 >= 0
```

4. AM likelihoods do not generate their own fiducials, one has to generate them using the full likelihoods and be very careful with fiducial parameters.
5.  MP likelihoods when reaching max number of Nsteps, finish (on the cluster at least) with `FAILED, ExitCode 137`  giving the wrong impression that the run has failed or there was a problem. They should exit with `ExitCode 0` 
6.  When generating the fiducial, the MP likelihood returns : 
```
256             warnings.warn(
257                 "Writing fiducial model in %s, for %s likelihood\n" % (
258                     self.fid_filename, self.name))
259             return 1j

```
This is a strange complex number return, because in the case of using the option `--display-each-chi2`  at the same time as `-f0`  to generate the fiducial, this return value gets added to the other chi2 of other likelihoods and one gets the wrong impression that something is going on.  The logic here should be clarified.

7. The public (Casas et al 2023) ISTF-like `euclid_spectroscopic` likelihood does not work for `m_nu=0`  because it automatically requests `P_cb`, `f_cb` and other `cb` quantities, which are not available in this case from class.
8. The oneloop spectroscopic likelihoods do not contain `P_cb`  explicitly, working with `P_mm` only.
9.  The runs of the MP validation paper were done in the `Omega_m, sigma8` and **camb** basis. The oneloop runs have been done using the **class** basis and `logAs`  making a comparison more difficult.