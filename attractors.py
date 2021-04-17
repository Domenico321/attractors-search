# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 12:03:57 2020

@author: Utente
"""

import boolean2 as b2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab

model_definition = """
# Initial values of the nodes
TRIB3 = False
PLAU = False
IFI16 = False
BTG3 = False
LAPTM5 = False
ST14 = False
EPHA2 = False
PML = False
STAT5A = False
CD82 = False
TP53 = False
PLK2 = False
CTSD = False
KRT15 = False
DDR1 = False
SERPINA3 = False
EZH2 = False
RELA = False
ETS1 = False
MCM7 = False
ACTB = False
VIM = False
MTA1 = False
ITGB4 = False
CAV1 = False
SETDB1 = False
KRT17 = False
HSP90AB1 = False
CCND1 = False
E2F1 = False
BCL2L1 = False
BRCA1 = False
HIF1A = False
PLAUR = False
STAT1 = False
STAT3 = False
TGFB1 = False
RB1 = False
FOS = False
CREB1 = False
PLAT = False
SQSTM1 = False
REL = False
NFKB1 = False
CD44 = False
TK1 = False
PARP1 = False
SOD1 = False
HDAC1 = False
LDHB = False
CSNK2B = False
KRT5 = False
TGFBR2 = False
ARNT = False
YWHAB = False
ARAF = False
NFE2L2 = False
S100A10 = False
PSMD4 = False
HMGCR = False
AKT2 = False
TNRC6A = False
ERBB2 = False
IKBKG = False
ATF2 = False
PPARD = False
SLC3A2 = False
UBQLN1 = False
SYNPO = False
BAX = False
EGFR = False
ETV1 = False
MAP3K7 = False
TGFBR1 = False
SMAD4 = False
MAP3K4 = False
INSR = False
A2M = False
PAX6 = False
CYP3A4 = False
NEDD9 = False
GADD45B = False
PPARG = False
NR3C1 = False
SMAD3 = False
PCGF5 = False
HSPB1 = False
IRF9 = False
ANXA1 = False
UBE2D1 = False
WWP1 = False
E2F4 = False
GABP = False
ARRB1 = False
EEF1G = False
HINT1 = False
TM4SF1 = False
MYC = False
SAT1 = False
NCOA4 = False
AR = False
BCL6 = False
TRIM29 = False










# Update rules

TRIB3* = not TP53
PLAU* = (TP53 or NFKB1 or HIF1A or ATF2 or ETS1 or PLAUR or ST14 or RELA) and not HDAC1
IFI16* = TP53
BTG3* = TP53
LAPTM5* = TP53
ST14* = (TP53 or PPARD or STAT1 or ST14) and not RELA
EPHA2* = (TP53 or AKT2 or ETS1 or CREB1) and not(MTA1 or RELA)
PML* = (TP53 or IRF9 or STAT5A or STAT1 or RB1) and not CSNK2B
STAT5A* = (TP53 or HSP90AB1 or RELA or STAT5A) and not(BRCA1 or UBE2D1)
CD82* = TP53 or HIF1A
TP53* = (TP53 or CREB1 or NFKB1 or E2F1 or HIF1A or STAT1 or BRCA1 or HSP90AB1 or ETS1 or PML or YWHAB or PLK2 or IRF9 or IFI16 or RELA) and not(HDAC1 or STAT3 or CSNK2B or PARP1 or EZH2 or ARRB1 or PSMD4 or PLAU or BCL2L1 or BCL6 or SETDB1 or EEF1G or UBE2D1 or WWP1 or TRIM29 or MTA1)
PLK2* = TP53
CTSD* = TP53 or CTSD
KRT15* = TP53
DDR1* = TP53 or E2F1 or DDR1 or TM4SF1
SERPINA3* = TP53 or NFKB1 or STAT3 or STAT1 or RELA
EZH2* = (E2F1 or STAT3 or REL or HSP90AB1 or STAT5A) and not(TP53 or RB1)
RELA* = (E2F1 or ATF2 or CSNK2B or BRCA1 or PARP1 or EZH2 or ARRB1 or AKT2 or HIF1A or CREB1 or FOS) and not(TP53 or STAT1 or PML or SQSTM1 or TRIB3 or HDAC1)
ETS1* = (FOS or HIF1A or ARNT) and not(TP53 or RB1 or RELA)
MCM7* = (E2F1 or CCND1) and not(TP53 or RB1)
ACTB* = (HSP90AB1 or SYNPO) and not TP53
VIM* = (NFKB1 or E2F1 or STAT3 or FOS or HIF1A or ATF2 or STAT1 or PARP1 or HSP90AB1 or EEF1G or ARRB1 or STAT5A or SQSTM1 or HSPB1 or ITGB4 or RELA) and not(CREB1 or ANXA1 or TP53)
MTA1* = RELA and not(TP53 or PARP1)
ITGB4* = (NFKB1 or ERBB2 or AKT2) and not(TP53 or HDAC1)
CAV1* = (STAT3 or ETS1 or EGFR or ARNT or PLAUR or CD82 or RELA) and not(TP53 or SQSTM1)
SETDB1* = AKT2 and not TP53
KRT17* = (FOS or STAT1) and not(TP53 or BRCA1 or EZH2)
HSP90AB1* = (HDAC1 or STAT3 or CSNK2B or STAT1 or HSPB1) and not TP53
CCND1* = (CREB1 or NFKB1 or E2F1 or FOS or ATF2 or STAT1 or PARP1 or REL or EZH2 or ETS1 or STAT5A or MTA1 or EGFR or RELA) and not(HDAC1 or TP53 or PML or CAV1 or PSMD4 or HINT1 or TNRC6A or HIF1A or NR3C1)
E2F1* = (CREB1 or E2F1 or ARRB1) and not(TP53 or HDAC1 or PARP1 or IFI16 or BTG3 or RELA or NFKB1 or HDAC1 or SETDB1 or RB1 or E2F4)
BCL2L1* = (CREB1 or NFKB1 or STAT3 or FOS or HIF1A or ATF2 or STAT1 or REL or ETS1 or STAT5A or NFE2L2 or GABP or RELA) and not(TP53 or HDAC1 or ERBB2 or BCL2L1)
BRCA1* = (CREB1 or PARP1 or NFE2L2 or AKT2 or GABP) and not(TP53 or HDAC1 or RB1 or MTA1 or PML)
HIF1A* = (CREB1 or NFKB1 or STAT3 or BRCA1 or REL or HSP90AB1 or ARRB1 or MTA1 or ARNT or RELA or ATF2 or E2F1 or HIF1A or PARP1 or HDAC1 or SAT1) and not(TP53 or PSMD4 or MCM7 or SQSTM1 or STAT1)
PLAUR* = (NFKB1 or FOS or HIF1A or ATF2 or PLAU or RELA or CAV1) and not(TP53 or HDAC1)
STAT1* = (CREB1 or BRCA1) and not(ARRB1 or PML or HDAC1)
STAT3* = (CREB1 or STAT3 or FOS or ATF2 or EZH2 or MTA1 or HIF1A or NFKB1 or SETDB1 or CD44 or RELA) and not(HDAC1 or RB1 or PML or CAV1 or CCND1)
TGFB1* = (CREB1 or NFKB1 or STAT3 or HIF1A or FOS or ATF2 or PPARD or RELA or REL) and not(HSP90AB1 or NFE2L2)
RB1* = (CREB1 or E2F1 or ATF2 or BRCA1 or GABP or PML) and not(HDAC1 or BCL6)
FOS* = (CREB1 or E2F1 or STAT3 or FOS or ATF2 or STAT1 or PARP1 or STAT5A or NFE2L2 or IKBKG) and not HDAC1 
CREB1* = CREB1 or ARRB1 or AKT2
PLAT* = CREB1 or ATF2 or RELA or FOS 
SQSTM1* = NFKB1 or RELA or NFE2L2 or FOS 
REL* = HIF1A and not NFKB1
NFKB1* = (FOS or BRCA1 or PARP1 or PSMD4 or RELA or HIF1A or ETS1) and not(E2F1 or HDAC1 or ARRB1)
CD44* = (FOS or NFKB1 or ETS1 or RELA) and not E2F1
TK1* = E2F1
PARP1* = ETS1 and not(AKT2 or PARP1 or HDAC1)
SOD1* = (NFE2L2 or RELA) and not(HDAC1 or CAV1 or PSMD4)
HDAC1* = (CSNK2B or STAT3 or EZH2 or RB1 or STAT5A or MTA1 or CCND1 or RELA) and not HDAC1 
LDHB* = STAT3 or PPARD
CSNK2B* = (STAT3 or CSNK2B or HSP90AB1 or ETS1 or PLAU) and not ACTB
KRT5* = FOS and not BRCA1
TGFBR2* = FOS or TGFB1
ARNT* = (HIF1A or RELA or BRCA1) and not STAT5A
YWHAB* = (PPARD or AKT2) and not SOD1 
ARAF* = CSNK2B
NFE2L2* = (CSNK2B or BRCA1 or NFE2L2 or AKT2) and not(EZH2 or PML or CAV1 or RELA)
S100A10* = STAT1
PSMD4* = PARP1
HMGCR* = PARP1
AKT2* = (ARRB1 or HSP90AB1 or CAV1) and not(BRCA1 or EZH2 or TRIB3)
TNRC6A* = HSP90AB1
ERBB2* = HSP90AB1 or EGFR or HSPB1 or ITGB4 or ETV1
IKBKG* = HSP90AB1 or ANXA1 or MAP3K7 or SQSTM1
ATF2* = RB1 or BRCA1
PPARD* = not HSP90AB1 and not RELA
SLC3A2* = NFE2L2 or RELA
UBQLN1* = GABP
SYNPO* = YWHAB
BAX* = not BCL2L1
EGFR* = EGFR or ERBB2
ETV1* = ERBB2
MAP3K7* = MAP3K7 or TGFBR1
TGFBR1* = (TGFB1 or TGFBR2 or YWHAB) and not CAV1
SMAD4* = not MAP3K7
MAP3K4* = GADD45B
INSR* = PPARG
A2M* = PPARG
PAX6* = PPARG
CYP3A4* = NR3C1
NEDD9* = NR3C1
GADD45B* = REL or TP53 or E2F1 or MYC
PPARG* = (NCOA4 or AKT2) and not SMAD3
NR3C1* = AR
SMAD3* = PPARG
RELA* = PCGF5
"""


#Refers to the text containing in the model definition and the model update
model = b2.Model(text=model_definition, mode='sync')
model.initialize()
#Number of iteration
model.iterate(steps=18)

for node in model.data:
    print node, model.data[node]
#Cheking for fixed states
model.report_cycles()


#Save the result
model.save_states('single_cell_name.xls')


