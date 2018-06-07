import ROOT

fall = open("DECISION.txt", 'r')

lall = fall.readlines()

fall.close()

dict_desc = dict((ev.split()[2], ev.split()[-1].strip()) for ev in lall)

print("all: ", len(dict_desc))

fpass = open("DECORATION.txt", 'r')

lpass = fpass.readlines()

fpass.close()

passev = [lpass[i*2].split()[2] for i in range(len(lpass)/2)]

print("pass: ", len(passev))


failev =  list(set(dict_desc.keys())-set(passev))

print("fail: ", len(failev))

ROOT.gROOT.SetBatch(1)
c = ROOT.TCanvas('c', 'c', 800, 600)

algversion = "R21 filter"

h = ROOT.TH2F("h", "Jet cleaning %s alg"%algversion, 2, -0.5, 1.5, 2, -0.5, 1.5)

for evP in passev:
    h.Fill(1, float(dict_desc[evP]))

for evF in failev:
    h.Fill(0, float(dict_desc[evF]))

xlabels = ["Veto", "Pass"]
ylabels = ["0", "1"]
for i in range(2):
    h.GetXaxis().SetBinLabel(i+1,xlabels[i])
    h.GetYaxis().SetBinLabel(i+1,ylabels[i])

h.GetXaxis().SetTitle("Outcome")

h.GetYaxis().SetTitle("DFCommonJets_eventClean_LooseBad")

h.Draw('COL')
h.Draw('TEXT SAME')
c.Print("passMatrix.eps")
