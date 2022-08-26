#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
from array import array
from ROOT import *

import warnings
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )

gROOT.SetBatch()

infName = 'raw_SFs.root'
outRootName = "final_SFs.root"

CRs = ['nom', 'Zjets', 'top']
ntrks = ['1p', '3p']

'SF_nom_1p_trueMCUncer_up'

inf = TFile(infName, 'read')
outf = TFile(outRootName, 'recreate')

numSFs = {}
for key in inf.GetListOfKeys():
 cl = gROOT.GetClass(key.GetClassName())
 if not cl.InheritsFrom("TH1"): continue
 hsfName = key.GetName()
 hist = inf.Get(hsfName)
 outf.cd()
 hist.Write()
 sfName = hsfName.replace('SF_', '')
 numSFs[sfName] = []
 for i in range(hist.GetNbinsX()):
  numSFs[sfName].append(hist.GetBinContent(i+1))
#print numSFs

for ntrk in ntrks:
 hSF_Numerator_sys = inf.Get('SF_nom_'+ntrk).Clone('SF_nom_'+ntrk+'_Numerator_sys')
 hSF_Composition_sys = inf.Get('SF_nom_'+ntrk).Clone('SF_nom_'+ntrk+'_Composition_sys')

 #for cr in CRs:
 # hist = inf.Get('SF_'+cr+'_'+ntrk)
 # numSFs[cr+'_'+ntrk] = []
 # for i in range(hist.GetNbinsX()):
 #  numSFs[cr+'_'+ntrk].append(hist.GetBinContent(i+1))

 for i in range(len(numSFs['nom_'+ntrk])):
  maxdiff = 0
  for cr in CRs:
   if cr == 'nom': continue
   if abs(numSFs['nom_'+ntrk][i] - numSFs[cr+'_'+ntrk][i]) > maxdiff:
    maxdiff = abs(numSFs['nom_'+ntrk][i] - numSFs[cr+'_'+ntrk][i])
  hSF_Composition_sys.SetBinError(i+1, maxdiff)

 outf.cd()
 hSF_Composition_sys.Write()

 hSF_trueMCUncer_up = inf.Get('SF_nom_'+ntrk+'_trueMCUncer_up')
 hSF_trueMCUncer_dn = inf.Get('SF_nom_'+ntrk+'_trueMCUncer_dn')
 for i in range(len(numSFs['nom_'+ntrk])):
  uncer = abs(hSF_trueMCUncer_up.GetBinContent(i+1) - hSF_trueMCUncer_dn.GetBinContent(i+1))
  hSF_Numerator_sys.SetBinError(i+1, uncer/2)
 outf.cd()
 hSF_Numerator_sys.Write()

outf.Close()
