#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, os
from array import array
from ROOT import *

import warnings
warnings.filterwarnings( action='ignore', category=RuntimeWarning, message='creating converter.*' )

gROOT.SetBatch()

gROOT.LoadMacro("AtlasStyle.C")
gROOT.LoadMacro("AtlasUtils.C")
gROOT.LoadMacro("AtlasLabels.C")

SetAtlasStyle()

gStyle.SetErrorX(0.5) # !!! must after SetAtlasStyle()
gStyle.SetOptStat(0)

infName = 'final_SFs.root'
outName = "Plot_SFs"

CRs = ['nom', 'Zjets', 'top']
ntrks = ['1p', '3p']

inf = TFile(infName, 'read')

SF_nom_1p = inf.Get('SF_nom_1p')
SF_nom_1p_trueMCUncer_up = inf.Get('SF_nom_1p_trueMCUncer_up')
SF_nom_1p_trueMCUncer_dn = inf.Get('SF_nom_1p_trueMCUncer_dn')
SF_Zjets_1p = inf.Get('SF_Zjets_1p')
SF_top_1p = inf.Get('SF_top_1p')
SF_nom_1p_Composition_sys = inf.Get('SF_nom_1p_Composition_sys')
SF_nom_1p_Numerator_sys = inf.Get('SF_nom_1p_Numerator_sys')
SF_nom_1p_All_sys = inf.Get('SF_nom_1p_All_sys')

SF_nom_1p.SetLineColor(1)
SF_nom_1p_trueMCUncer_up.SetLineColor(2)
SF_nom_1p_trueMCUncer_dn.SetLineColor(3)
SF_Zjets_1p.SetLineColor(4)
SF_top_1p.SetLineColor(5)

SF_nom_1p_Composition_sys.SetMarkerSize(0)
SF_nom_1p_Composition_sys.SetLineWidth(0)
SF_nom_1p_Composition_sys.SetFillStyle(3004)
SF_nom_1p_Composition_sys.SetFillColor(6)
SF_nom_1p_Numerator_sys.SetMarkerSize(0)
SF_nom_1p_Numerator_sys.SetLineWidth(0)
SF_nom_1p_Numerator_sys.SetFillStyle(3004)
SF_nom_1p_Numerator_sys.SetFillColor(7)
SF_nom_1p_All_sys.SetMarkerSize(0)
SF_nom_1p_All_sys.SetLineWidth(0)
SF_nom_1p_All_sys.SetFillStyle(3004)
SF_nom_1p_All_sys.SetFillColor(8)

canv1 = TCanvas('canv1', 'canvas', 800, 800);
lg1 = TLegend(0.45, 0.15, 0.85, 0.45)
lg1.SetBorderSize(0)
lg1.SetFillColorAlpha(kBlue, 0)

SF_nom_1p_Composition_sys.Draw('same e2')
SF_nom_1p.Draw('same')
SF_Zjets_1p.Draw('same')
SF_top_1p.Draw('same')

lg1.AddEntry(SF_nom_1p_Composition_sys, SF_nom_1p_Composition_sys.GetName().replace('SF_', ''), 'f')
lg1.AddEntry(SF_nom_1p, SF_nom_1p.GetName().replace('SF_', ''), 'lep')
lg1.AddEntry(SF_Zjets_1p, SF_Zjets_1p.GetName().replace('SF_', ''), 'lep')
lg1.AddEntry(SF_top_1p, SF_top_1p.GetName().replace('SF_', ''), 'lep')

lg1.Draw('same')
canv1.SaveAs(outName+'_1p_compSys.png')
canv1.SaveAs(outName+'_1p_compSys.pdf')


canv2 = TCanvas('canv2', 'canvas', 800, 800);
lg2 = TLegend(0.45, 0.15, 0.85, 0.45)
lg2.SetBorderSize(0)
lg2.SetFillColorAlpha(kBlue, 0)

SF_nom_1p_Numerator_sys.Draw('same e2')
SF_nom_1p.Draw('same')
SF_nom_1p_trueMCUncer_up.Draw('same')
SF_nom_1p_trueMCUncer_dn.Draw('same')

lg2.AddEntry(SF_nom_1p_Numerator_sys, SF_nom_1p_Numerator_sys.GetName().replace('SF_', ''), 'f')
lg2.AddEntry(SF_nom_1p, SF_nom_1p.GetName().replace('SF_', ''), 'lep')
lg2.AddEntry(SF_nom_1p_trueMCUncer_up, SF_nom_1p_trueMCUncer_up.GetName().replace('SF_', ''), 'lep')
lg2.AddEntry(SF_nom_1p_trueMCUncer_dn, SF_nom_1p_trueMCUncer_dn.GetName().replace('SF_', ''), 'lep')

lg2.Draw('same')
canv2.SaveAs(outName+'_1p_numeratorSys.png')
canv2.SaveAs(outName+'_1p_numeratorSys.pdf')

#####

SF_nom_3p = inf.Get('SF_nom_3p')
SF_nom_3p_trueMCUncer_up = inf.Get('SF_nom_3p_trueMCUncer_up')
SF_nom_3p_trueMCUncer_dn = inf.Get('SF_nom_3p_trueMCUncer_dn')
SF_Zjets_3p = inf.Get('SF_Zjets_3p')
SF_top_3p = inf.Get('SF_top_3p')
SF_nom_3p_Composition_sys = inf.Get('SF_nom_3p_Composition_sys')
SF_nom_3p_Numerator_sys = inf.Get('SF_nom_3p_Numerator_sys')
SF_nom_3p_All_sys = inf.Get('SF_nom_3p_All_sys')

SF_nom_3p.SetLineColor(1)
SF_nom_3p_trueMCUncer_up.SetLineColor(2)
SF_nom_3p_trueMCUncer_dn.SetLineColor(3)
SF_Zjets_3p.SetLineColor(4)
SF_top_3p.SetLineColor(5)

SF_nom_3p_Composition_sys.SetMarkerSize(0)
SF_nom_3p_Composition_sys.SetLineWidth(0)
SF_nom_3p_Composition_sys.SetFillStyle(3004)
SF_nom_3p_Composition_sys.SetFillColor(6)
SF_nom_3p_Numerator_sys.SetMarkerSize(0)
SF_nom_3p_Numerator_sys.SetLineWidth(0)
SF_nom_3p_Numerator_sys.SetFillStyle(3004)
SF_nom_3p_Numerator_sys.SetFillColor(7)
SF_nom_3p_All_sys.SetMarkerSize(0)
SF_nom_3p_All_sys.SetLineWidth(0)
SF_nom_3p_All_sys.SetFillStyle(3004)
SF_nom_3p_All_sys.SetFillColor(8)

canv3 = TCanvas('canv3', 'canvas', 800, 800);
lg3 = TLegend(0.45, 0.15, 0.85, 0.45)
lg3.SetBorderSize(0)
lg3.SetFillColorAlpha(kBlue, 0)

SF_nom_3p_Composition_sys.Draw('same e2')
SF_nom_3p.Draw('same')
SF_Zjets_3p.Draw('same')
SF_top_3p.Draw('same')

lg3.AddEntry(SF_nom_3p_Composition_sys, SF_nom_3p_Composition_sys.GetName().replace('SF_', ''), 'f')
lg3.AddEntry(SF_nom_3p, SF_nom_3p.GetName().replace('SF_', ''), 'lep')
lg3.AddEntry(SF_Zjets_3p, SF_Zjets_3p.GetName().replace('SF_', ''), 'lep')
lg3.AddEntry(SF_top_3p, SF_top_3p.GetName().replace('SF_', ''), 'lep')

lg3.Draw('same')
canv3.SaveAs(outName+'_3p_compSys.png')
canv3.SaveAs(outName+'_3p_compSys.pdf')


canv4 = TCanvas('canv4', 'canvas', 800, 800);
lg4 = TLegend(0.45, 0.15, 0.85, 0.45)
lg4.SetBorderSize(0)
lg4.SetFillColorAlpha(kBlue, 0)

SF_nom_3p_Numerator_sys.Draw('same e2')
SF_nom_3p.Draw('same')
SF_nom_3p_trueMCUncer_up.Draw('same')
SF_nom_3p_trueMCUncer_dn.Draw('same')

lg4.AddEntry(SF_nom_3p_Numerator_sys, SF_nom_3p_Numerator_sys.GetName().replace('SF_', ''), 'f')
lg4.AddEntry(SF_nom_3p, SF_nom_3p.GetName().replace('SF_', ''), 'lep')
lg4.AddEntry(SF_nom_3p_trueMCUncer_up, SF_nom_3p_trueMCUncer_up.GetName().replace('SF_', ''), 'lep')
lg4.AddEntry(SF_nom_3p_trueMCUncer_dn, SF_nom_3p_trueMCUncer_dn.GetName().replace('SF_', ''), 'lep')

lg4.Draw('same')
canv4.SaveAs(outName+'_3p_numeratorSys.png')
canv4.SaveAs(outName+'_3p_numeratorSys.pdf')

###
canv5 = TCanvas('canv5', 'canvas', 800, 800);
lg5 = TLegend(0.55, 0.25, 0.85, 0.35)
lg5.SetBorderSize(0)
lg5.SetFillColorAlpha(kBlue, 0)

SF_nom_1p.Draw('same')

lg5.AddEntry(SF_nom_1p, SF_nom_1p.GetName().replace('SF_', ''), 'lep')

lg5.Draw('same')
canv5.SaveAs(outName+'_1p_nom.png')
canv5.SaveAs(outName+'_1p_nom.pdf')


canv6 = TCanvas('canv6', 'canvas', 800, 800);
lg6 = TLegend(0.55, 0.25, 0.85, 0.35)
lg6.SetBorderSize(0)
lg6.SetFillColorAlpha(kBlue, 0)

SF_nom_3p.Draw('same')

lg6.AddEntry(SF_nom_3p, SF_nom_3p.GetName().replace('SF_', ''), 'lep')

lg6.Draw('same')
canv6.SaveAs(outName+'_3p_nom.png')
canv6.SaveAs(outName+'_3p_nom.pdf')

###
canv7 = TCanvas('canv7', 'canvas', 800, 800);
lg7 = TLegend(0.20, 0.20, 0.50, 0.30)
lg7.SetBorderSize(0)
lg7.SetFillColorAlpha(kBlue, 0)

SF_nom_1p_All_sys.Draw('same e2')
SF_nom_1p.Draw('same')

lg7.AddEntry(SF_nom_1p_All_sys, SF_nom_1p_All_sys.GetName().replace('SF_', ''), 'f')
lg7.AddEntry(SF_nom_1p, SF_nom_1p.GetName().replace('SF_', ''), 'lep')

lg7.Draw('same')
canv7.SaveAs(outName+'_1p_allSys.png')
canv7.SaveAs(outName+'_1p_allSys.pdf')


canv8 = TCanvas('canv8', 'canvas', 800, 800);
lg8 = TLegend(0.20, 0.20, 0.50, 0.30)
lg8.SetBorderSize(0)
lg8.SetFillColorAlpha(kBlue, 0)

SF_nom_3p_All_sys.Draw('same e2')
SF_nom_3p.Draw('same')

lg8.AddEntry(SF_nom_3p_All_sys, SF_nom_3p_All_sys.GetName().replace('SF_', ''), 'f')
lg8.AddEntry(SF_nom_3p, SF_nom_3p.GetName().replace('SF_', ''), 'lep')

lg8.Draw('same')
canv8.SaveAs(outName+'_3p_allSys.png')
canv8.SaveAs(outName+'_3p_allSys.pdf')
