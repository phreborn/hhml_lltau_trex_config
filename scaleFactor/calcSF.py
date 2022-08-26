#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
from array import array
from ROOT import *

import warnings
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )

gROOT.SetBatch()

outRootName = "raw_SFs.root"

trueMCUncer = 0.5

CRs = ['nom', 'Zjets', 'top']
ntrks = ['1p', '3p']
rebinArray = array('d', [0, 25, 45, 70, 200])
nRebins = len(rebinArray)-1

samples = []
with open("sampleNames", 'r') as f:
  for line in f.readlines():
   if '#' in line: continue
   samples.append(line.replace('\n', ''))
print samples

outf = TFile(outRootName, 'recreate')
for ntrk in ntrks:
 for cr in CRs:
  hdata = TH1D()
  hsig = TH1D()
  hstrue = []
  hsfake = []
  inf = TFile("../tauFakeSF/jobtauFakeSF_hh_2l1tau_tauSFCR_"+cr+"_tauPt_"+ntrk+"_histos.root")
  for samp in samples:

   fsamp = samp+'_fakeTau'

   htname = 'hh_2l1tau_tauSFCR_'+cr+'_tauPt_'+ntrk+'/'+samp+'/nominal/'+'hh_2l1tau_tauSFCR_'+cr+'_tauPt_'+ntrk+'_'+samp+'_orig'
   hfname = 'hh_2l1tau_tauSFCR_'+cr+'_tauPt_'+ntrk+'/'+fsamp+'/nominal/'+'hh_2l1tau_tauSFCR_'+cr+'_tauPt_'+ntrk+'_'+fsamp+'_orig'

   if samp == 'Data':
    hdata_orig = inf.Get(htname)
    hdata = hdata_orig.Rebin(nRebins, 'hdata', rebinArray)
    continue
   if samp == 'HH':
    hsig_orig = inf.Get(htname)
    hsig = hsig_orig.Rebin(nRebins, 'hsig', rebinArray)
    continue

   htrue_orig = inf.Get(htname)
   htrue = htrue_orig.Rebin(nRebins, 'htrue', rebinArray)
   hfake_orig = inf.Get(hfname)
   hfake = hfake_orig.Rebin(nRebins, 'hfake', rebinArray)

   hstrue.append(htrue)
   hsfake.append(hfake)

   htruebkgs = hstrue[0].Clone('htruebkgs')
   htruebkgs.Scale(0.)
   hfakebkgs = hsfake[0].Clone('hfakebkgs')
   hfakebkgs.Scale(0.)
   for hist in hstrue:
     htruebkgs.Add(hist)
   for hist in hsfake:
     hfakebkgs.Add(hist)

  #canv = TCanvas('canv', 'canvas', 800, 800);
  #hdata.Draw()
  #htruebkgs.Draw('same')
  #hfakebkgs.Draw('same')
  #canv.SaveAs('out.png')
  #canv.SaveAs('out.pdf')

  hdata_minus_trueTau = hdata.Clone('hdata_minus_trueTau')
  hdata_minus_trueTau.Add(htruebkgs, -1)
  hscale_factor = hdata_minus_trueTau.Clone('SF_'+cr+'_'+ntrk)
  hscale_factor.Divide(hfakebkgs)

  outf.cd()
  hscale_factor.Write()

  if cr == 'nom':

   htruebkgs_up = htruebkgs.Clone('htruebkgs_up')
   htruebkgs_up.Scale(1+trueMCUncer)
   hdata_minus_trueTau_up = hdata.Clone('hdata_minus_trueTau_up')
   hdata_minus_trueTau_up.Add(htruebkgs_up, -1)
   hscale_factor_trueMCUncer_up = hdata_minus_trueTau_up.Clone('SF_'+cr+'_'+ntrk+'_trueMCUncer_up')
   hscale_factor_trueMCUncer_up.Divide(hfakebkgs)

   htruebkgs_dn = htruebkgs.Clone('htruebkgs_dn')
   htruebkgs_dn.Scale(1-trueMCUncer)
   hdata_minus_trueTau_dn = hdata.Clone('hdata_minus_trueTau_dn')
   hdata_minus_trueTau_dn.Add(htruebkgs_dn, -1)
   hscale_factor_trueMCUncer_dn = hdata_minus_trueTau_dn.Clone('SF_'+cr+'_'+ntrk+'_trueMCUncer_dn')
   hscale_factor_trueMCUncer_dn.Divide(hfakebkgs)

   outf.cd()
   hscale_factor_trueMCUncer_up.Write()
   hscale_factor_trueMCUncer_dn.Write()

outf.Close()
