# Auto generated configuration file
# using: 
# Revision: 1.20 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/ThirteenTeV/WH_ZH_HToTauTau_M_125_TuneZ2star_13TeV_pythia6_cff.py --fileout file:HIG-Fall13-00001.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM --conditions POSTLS162_V1::All --step GEN,SIM --magField 38T_PostLS1 --geometry Extended2015 --python_filename HIG-Fall13-00001_1_cfg.py --no_exec -n 29
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2000)
)

# Input source

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
		"file:MCDBtoEDM_NONE.root"
	  )
)



process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('PYTHIA6 WH/ZH, H->2tau mH=125GeV with TAUOLA at 13TeV'),
    name = cms.untracked.string('$Source: /cvs/CMSSW/CMSSW/Configuration/GenProduction/python/ThirteenTeV/WH_ZH_HToTauTau_M_125_TuneZ2star_13TeV_pythia6_cff.py,v $')
)

# Output definition
ofile = 'EDM2GEN_PY8.root'

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string(ofile),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
#from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *


process.generator = cms.EDFilter("Pythia8HadronizerFilter",
#    ExternalDecays = cms.PSet(
#        Tauola = cms.untracked.PSet(
#            UseTauolaPolarization = cms.bool(True),
#            InputCards = cms.PSet(
#                mdtau = cms.int32(240),
#                pjak2 = cms.int32(0),
#                pjak1 = cms.int32(0)
#            ),
#        ),
#        parameterSets = cms.vstring('Tauola'),
#    ),
    maxEventsToPrint = cms.untracked.int32(2),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    SLHATableForPythia8 = cms.string('BLOCK SPINFO\n     1   FeynHiggs\n     2   2.10.3\n     2   built on Mar 24, 2015\nBLOCK MODSEL\n         1                  0   # Model\n         2                  1   # GridPts\n         3                  0   # Content\n         4                  0   # RPV\n         5                  0   # CPV\n         6                  0   # FV\nBLOCK SMINPUTS\n         1     1.28952896E+02   # invAlfaMZ\n         2     1.16637000E-05   # GF\n         3     1.19000000E-01   # AlfasMZ\n         4     9.11876000E+01   # MZ\n         5     4.16000000E+00   # Mb\n         6     1.72500000E+02   # Mt\n         7     1.77703000E+00   # Mtau\n        11     5.10998902E-04   # Me\n        13     1.05658357E-01   # Mmu\n        21     6.00000000E-03   # Md\n        22     3.00000000E-03   # Mu\n        23     9.50000000E-02   # Ms\n        24     1.28600000E+00   # Mc\nBLOCK MINPAR\n         3     2.00000000E+00   # TB\nBLOCK EXTPAR\n         0     0.00000000E+00   # Q\n         1     9.54716519E+01   # M1\n         2     2.00000000E+02   # M2\n         3     1.50000000E+03   # M3\n        11     1.60000000E+03   # At\n        12     1.60000000E+03   # Ab\n        13     1.60000000E+03   # Atau\n        23     2.00000000E+02   # MUE\n        25     2.00000000E+00   # TB\n        26     3.00000000E+02   # MA0\n        27     3.10586282E+02   # MHp\n        31     5.00000000E+02   # MSL(1)\n        32     5.00000000E+02   # MSL(2)\n        33     1.00000000E+03   # MSL(3)\n        34     5.00000000E+02   # MSE(1)\n        35     5.00000000E+02   # MSE(2)\n        36     1.00000000E+03   # MSE(3)\n        41     1.50000000E+03   # MSQ(1)\n        42     1.50000000E+03   # MSQ(2)\n        43     1.00000000E+03   # MSQ(3)\n        44     1.50000000E+03   # MSU(1)\n        45     1.50000000E+03   # MSU(2)\n        46     1.00000000E+03   # MSU(3)\n        47     1.50000000E+03   # MSD(1)\n        48     1.50000000E+03   # MSD(2)\n        49     1.00000000E+03   # MSD(3)\nBLOCK MASS\n   1000012     4.97499192E+02   # MSf(1,1,1)\n   1000011     5.01109573E+02   # MSf(1,2,1)\n   2000011     5.01381840E+02   # MSf(2,2,1)\n   1000002     1.49941521E+03   # MSf(1,3,1)\n   2000002     1.49975313E+03   # MSf(2,3,1)\n   1000001     1.50012342E+03   # MSf(1,4,1)\n   2000001     1.50070793E+03   # MSf(2,4,1)\n   1000014     4.97499192E+02   # MSf(1,1,2)\n   1000013     5.01103204E+02   # MSf(1,2,2)\n   2000013     5.01388228E+02   # MSf(2,2,2)\n   1000004     1.49941041E+03   # MSf(1,3,2)\n   2000004     1.49975904E+03   # MSf(2,3,2)\n   1000003     1.50012315E+03   # MSf(1,4,2)\n   2000003     1.50070820E+03   # MSf(2,4,2)\n   1000016     9.98751944E+02   # MSf(1,1,3)\n   1000015     9.99556720E+02   # MSf(1,2,3)\n   2000015     1.00169218E+03   # MSf(2,2,3)\n   1000006     8.77358807E+02   # MSf(1,3,3)\n   2000006     1.13457458E+03   # MSf(2,3,3)\n   1000005     9.98113673E+02   # MSf(1,4,3)\n   2000005     1.00314394E+03   # MSf(2,4,3)\n        25     1.00961246E+02   # Mh0\n        35     3.13972176E+02   # MHH\n        36     3.00000000E+02   # MA0\n        37     3.10228633E+02   # MHp\n   1000022     7.56619961E+01   # MNeu(1)\n   1000023     1.40474137E+02   # MNeu(2)\n   1000025    -2.02345060E+02   # MNeu(3)\n   1000035     2.81680580E+02   # MNeu(4)\n   1000024     1.25337244E+02   # MCha(1)\n   1000037     2.77881723E+02   # MCha(2)\n   1000021     1.50000000E+03   # MGl\nBLOCK DMASS\n         0     1.72500000E+02   # Q\n        25     1.75708877E+00   # Delta Mh0\n        35     3.86498167E-01   # Delta MHH\n        36     0.00000000E+00   # Delta MA0\n        37     2.26391567E-01   # Delta MHp\nBLOCK NMIX\n     1   1     8.58898923E-01   # ZNeu(1,1)\n     1   2    -2.55692064E-01   # ZNeu(1,2)\n     1   3     3.56943761E-01   # ZNeu(1,3)\n     1   4    -2.63638693E-01   # ZNeu(1,4)\n     2   1     4.84276326E-01   # ZNeu(2,1)\n     2   2     6.84110384E-01   # ZNeu(2,2)\n     2   3    -4.07445438E-01   # ZNeu(2,3)\n     2   4     3.62570873E-01   # ZNeu(2,4)\n     3   1     4.79153443E-02   # ZNeu(3,1)\n     3   2    -6.62715547E-02   # ZNeu(3,2)\n     3   3    -6.92309834E-01   # ZNeu(3,3)\n     3   4    -7.16951389E-01   # ZNeu(3,4)\n     4   1    -1.59603261E-01   # ZNeu(4,1)\n     4   2     6.79869569E-01   # ZNeu(4,2)\n     4   3     4.76745699E-01   # ZNeu(4,3)\n     4   4    -5.33870496E-01   # ZNeu(4,4)\nBLOCK UMIX\n     1   1    -6.61019827E-01   # UCha(1,1)\n     1   2     7.50368435E-01   # UCha(1,2)\n     2   1     7.50368435E-01   # UCha(2,1)\n     2   2     6.61019827E-01   # UCha(2,2)\nBLOCK VMIX\n     1   1    -7.50368435E-01   # VCha(1,1)\n     1   2     6.61019827E-01   # VCha(1,2)\n     2   1     6.61019827E-01   # VCha(2,1)\n     2   2     7.50368435E-01   # VCha(2,2)\nBLOCK STAUMIX\n     1   1    -6.84153540E-01   # USf(1,1)\n     1   2     7.29338010E-01   # USf(1,2)\n     2   1     7.29338010E-01   # USf(2,1)\n     2   2     6.84153540E-01   # USf(2,2)\nBLOCK STOPMIX\n     1   1     7.07798847E-01   # USf(1,1)\n     1   2    -7.06414038E-01   # USf(1,2)\n     2   1     7.06414038E-01   # USf(2,1)\n     2   2     7.07798847E-01   # USf(2,2)\nBLOCK SBOTMIX\n     1   1    -6.42558653E-01   # USf(1,1)\n     1   2     7.66236502E-01   # USf(1,2)\n     2   1     7.66236502E-01   # USf(2,1)\n     2   2     6.42558653E-01   # USf(2,2)\nBLOCK ALPHA\n              -5.54949020E-01   # Alpha\nBLOCK DALPHA\n               4.31612762E-03   # Delta Alpha\nBLOCK HMIX Q= -0.99900000E+03\n         1     2.00000000E+02   # MUE\n         2     2.00000000E+00   # TB\nBLOCK MSOFT Q=  0.00000000E+00\n         1     9.54716519E+01   # M1\n         2     2.00000000E+02   # M2\n         3     1.50000000E+03   # M3\n        31     5.00000000E+02   # MSL(1)\n        32     5.00000000E+02   # MSL(2)\n        33     1.00000000E+03   # MSL(3)\n        34     5.00000000E+02   # MSE(1)\n        35     5.00000000E+02   # MSE(2)\n        36     1.00000000E+03   # MSE(3)\n        41     1.50000000E+03   # MSQ(1)\n        42     1.50000000E+03   # MSQ(2)\n        43     1.00000000E+03   # MSQ(3)\n        44     1.50000000E+03   # MSU(1)\n        45     1.50000000E+03   # MSU(2)\n        46     1.00000000E+03   # MSU(3)\n        47     1.50000000E+03   # MSD(1)\n        48     1.50000000E+03   # MSD(2)\n        49     1.00000000E+03   # MSD(3)\nBLOCK AE Q=  0.00000000E+00\n     1   1     0.00000000E+00   # Af(1,1)\n     2   2     0.00000000E+00   # Af(2,2)\n     3   3     1.60000000E+03   # Af(3,3)\nBLOCK AU Q=  0.00000000E+00\n     1   1     0.00000000E+00   # Af(1,1)\n     2   2     0.00000000E+00   # Af(2,2)\n     3   3     1.60000000E+03   # Af(3,3)\nBLOCK AD Q=  0.00000000E+00\n     1   1     0.00000000E+00   # Af(1,1)\n     2   2     0.00000000E+00   # Af(2,2)\n     3   3     1.60000000E+03   # Af(3,3)\nBLOCK YE Q=  0.00000000E+00\n     1   1     6.56289772E-06   # Yf(1,1)\n     2   2     1.35699898E-03   # Yf(2,2)\n     3   3     2.28228791E-02   # Yf(3,3)\nBLOCK YU Q=  0.00000000E+00\n     1   1     1.92649075E-05   # Yf(1,1)\n     2   2     8.25822369E-03   # Yf(2,2)\n     3   3     1.10773218E+00   # Yf(3,3)\nBLOCK YD Q=  0.00000000E+00\n     1   1     7.69024755E-05   # Yf(1,1)\n     2   2     1.21761573E-03   # Yf(2,2)\n     3   3     5.30474110E-02   # Yf(3,3)\nBLOCK VCKMIN\n         1     2.25300000E-01   # lambda\n         2     8.08000000E-01   # A\n         3     1.32000000E-01   # rhobar\n         4     3.41000000E-01   # etabar\nBLOCK MSL2 Q=  0.00000000E+00\n     1   1     2.50000000E+05   # MSL2(1,1)\n     2   2     2.50000000E+05   # MSL2(2,2)\n     3   3     1.00000000E+06   # MSL2(3,3)\nBLOCK MSE2 Q=  0.00000000E+00\n     1   1     2.50000000E+05   # MSE2(1,1)\n     2   2     2.50000000E+05   # MSE2(2,2)\n     3   3     1.00000000E+06   # MSE2(3,3)\nBLOCK MSQ2 Q=  0.00000000E+00\n     1   1     2.25000000E+06   # MSQ2(1,1)\n     2   2     2.25000000E+06   # MSQ2(2,2)\n     3   3     1.00000000E+06   # MSQ2(3,3)\nBLOCK MSU2 Q=  0.00000000E+00\n     1   1     2.25000000E+06   # MSU2(1,1)\n     2   2     2.25000000E+06   # MSU2(2,2)\n     3   3     1.00000000E+06   # MSU2(3,3)\nBLOCK MSD2 Q=  0.00000000E+00\n     1   1     2.25000000E+06   # MSD2(1,1)\n     2   2     2.25000000E+06   # MSD2(2,2)\n     3   3     1.00000000E+06   # MSD2(3,3)\nBLOCK TE Q=  0.00000000E+00\n     1   1     0.00000000E+00   # Tf(1,1)\n     2   2     0.00000000E+00   # Tf(2,2)\n     3   3     3.65166065E+01   # Tf(3,3)\nBLOCK TU Q=  0.00000000E+00\n     1   1     0.00000000E+00   # Tf(1,1)\n     2   2     0.00000000E+00   # Tf(2,2)\n     3   3     1.77237149E+03   # Tf(3,3)\nBLOCK TD Q=  0.00000000E+00\n     1   1     0.00000000E+00   # Tf(1,1)\n     2   2     0.00000000E+00   # Tf(2,2)\n     3   3     8.48758577E+01   # Tf(3,3)\nBLOCK CVHMIX\n     1   1     9.98839600E-01   # UH(1,1)\n     1   2     4.81607071E-02   # UH(1,2)\n     1   3     0.00000000E+00   # UH(1,3)\n     2   1    -4.81607071E-02   # UH(2,1)\n     2   2     9.98839600E-01   # UH(2,2)\n     2   3     0.00000000E+00   # UH(2,3)\n     3   1     0.00000000E+00   # UH(3,1)\n     3   2     0.00000000E+00   # UH(3,2)\n     3   3     1.00000000E+00   # UH(3,3)\nBLOCK PRECOBS\n         1     3.54533680E-05   # DeltaRho\n         2     8.03706761E+01   # MWMSSM\n         3     8.03686796E+01   # MWSM\n         4     2.31427075E-01   # SW2effMSSM\n         5     2.31438136E-01   # SW2effSM\n        11     2.11575150E-10   # gminus2mu\n        21     0.00000000E+00   # EDMeTh\n        22     0.00000000E+00   # EDMn\n        23     0.00000000E+00   # EDMHg\n        31     5.32611105E-04   # bsgammaMSSM\n        32     3.98873687E-04   # bsgammaSM\n        33     2.35414366E+01   # DeltaMsMSSM\n        34     2.11742768E+01   # DeltaMsSM\n        35     6.91749543E-08   # BsmumuMSSM\n        36     3.48843376E-09   # BsmumuSM\nDECAY        25     3.07011619E-03   # Gamma(h0)\n     -1.52860895E-03   2        22        22   # BR(h0 -> photon photon)\n     -5.49452083E-05   2        22        23   # BR(h0 -> photon Z)\n     -7.54912902E-04   2        23        23   # BR(h0 -> Z Z)\n     -7.60121212E-03   2       -24        24   # BR(h0 -> W W)\n     -4.37619426E-02   2        21        21   # BR(h0 -> gluon gluon)\n     -7.22514216E-09   2       -11        11   # BR(h0 -> Electron electron)\n     -3.21366305E-04   2       -13        13   # BR(h0 -> Muon muon)\n     9.25320213E-02   2       -15        15   # BR(h0 -> Tau tau)\n     -1.98809873E-07   2        -2         2   # BR(h0 -> Up up)\n     -2.75261691E-02   2        -4         4   # BR(h0 -> Charm charm)\n     -1.23601996E-06   2        -1         1   # BR(h0 -> Down down)\n     -3.10407708E-04   2        -3         3   # BR(h0 -> Strange strange)\n     -8.25606972E-01   2        -5         5   # BR(h0 -> Bottom bottom)\nDECAY        35     6.74171451E-01   # Gamma(HH)\n     1.46538029E-05   2        22        22   # BR(HH -> photon photon)\n     8.63781545E-06   2        22        23   # BR(HH -> photon Z)\n     3.83407953E-02   2        23        23   # BR(HH -> Z Z)\n     8.52374975E-02   2       -24        24   # BR(HH -> W W)\n     4.12898570E-03   2        21        21   # BR(HH -> gluon gluon)\n     2.58714092E-10   2       -11        11   # BR(HH -> Electron electron)\n     1.15112506E-05   2       -13        13   # BR(HH -> Muon muon)\n     3.30953059E-03   2       -15        15   # BR(HH -> Tau tau)\n     8.41766329E-10   2        -2         2   # BR(HH -> Up up)\n     1.16469490E-04   2        -4         4   # BR(HH -> Charm charm)\n     3.62433478E-08   2        -1         1   # BR(HH -> Down down)\n     9.10221659E-06   2        -3         3   # BR(HH -> Strange strange)\n     2.38726168E-02   2        -5         5   # BR(HH -> Bottom bottom)\n     5.13725362E-02   2  -1000024   1000024   # BR(HH -> Chargino1 chargino1)\n     3.55301476E-02   2   1000022   1000022   # BR(HH -> neutralino1 neutralino1)\n     2.33282288E-02   2   1000022   1000023   # BR(HH -> neutralino1 neutralino2)\n     3.10438016E-01   2   1000022   1000025   # BR(HH -> neutralino1 neutralino3)\n     1.47787867E-03   2   1000023   1000023   # BR(HH -> neutralino2 neutralino2)\n     8.15528073E-07   2        23        36   # BR(HH -> Z A0)\n     4.22802539E-01   2        25        25   # BR(HH -> h0 h0)\nDECAY        36     1.22163099E+00   # Gamma(A0)\n     -3.54389963E-05   2        22        22   # BR(A0 -> photon photon)\n     -4.29009785E-05   2        22        23   # BR(A0 -> photon Z)\n     -3.98535706E-03   2        21        21   # BR(A0 -> gluon gluon)\n     -1.53861013E-10   2       -11        11   # BR(A0 -> Electron electron)\n     -6.84581695E-06   2       -13        13   # BR(A0 -> Muon muon)\n     -1.96838197E-03   2       -15        15   # BR(A0 -> Tau tau)\n     -3.07070446E-10   2        -2         2   # BR(A0 -> Up up)\n     -4.25828980E-05   2        -4         4   # BR(A0 -> Charm charm)\n     -2.17127136E-08   2        -1         1   # BR(A0 -> Down down)\n     -5.45297488E-06   2        -3         3   # BR(A0 -> Strange strange)\n     -1.43344112E-02   2        -5         5   # BR(A0 -> Bottom bottom)\n     -5.40146148E-01   2  -1000024   1000024   # BR(A0 -> Chargino1 chargino1)\n     -1.69920573E-01   2   1000022   1000022   # BR(A0 -> neutralino1 neutralino1)\n     -2.05461399E-01   2   1000022   1000023   # BR(A0 -> neutralino1 neutralino2)\n     -1.45591374E-03   2   1000022   1000025   # BR(A0 -> neutralino1 neutralino3)\n     -3.53312083E-02   2   1000023   1000023   # BR(A0 -> neutralino2 neutralino2)\n     2.72633638E-02   2        23        25   # BR(A0 -> Z h0)\n     -1.54335939E-34   2        25        25   # BR(A0 -> h0 h0)\nDECAY        37     2.37240577E+00   # Gamma(Hp)\n     8.65691402E-11   2       -11        12   # BR(Hp -> Electron nu_e)\n     3.70109963E-06   2       -13        14   # BR(Hp -> Muon nu_mu)\n     1.04684935E-03   2       -15        16   # BR(Hp -> Tau nu_tau)\n     1.08584933E-08   2        -1         2   # BR(Hp -> Down up)\n     1.21278657E-07   2        -3         2   # BR(Hp -> Strange up)\n     7.64992069E-08   2        -5         2   # BR(Hp -> Bottom up)\n     1.03247787E-06   2        -1         4   # BR(Hp -> Down charm)\n     2.54717888E-05   2        -3         4   # BR(Hp -> Strange charm)\n     1.07463560E-05   2        -5         4   # BR(Hp -> Bottom charm)\n     5.49637351E-05   2        -1         6   # BR(Hp -> Down top)\n     1.19839151E-03   2        -3         6   # BR(Hp -> Strange top)\n     8.73328818E-01   2        -5         6   # BR(Hp -> Bottom top)\n     8.29216555E-02   2   1000022   1000024   # BR(Hp -> neutralino1 chargino1)\n     2.31943935E-02   2   1000023   1000024   # BR(Hp -> neutralino2 chargino1)\n     1.82137060E-02   2        24        25   # BR(Hp -> W h0)\n     6.16875863E-08   2        24        36   # BR(Hp -> W A0)\nDECAY         6     1.35195755E+00   # Gamma(top)\n     1.00000000E+00   2         5        24   # BR(top -> bottom W)\n'),
    comEnergy = cms.double(13000.0),
    UseExternalGenerators = cms.untracked.bool(True),
    #jetMatching = cms.untracked.PSet(
        #MEMAIN_nqmatch = cms.int32(5),
        #MEMAIN_showerkt = cms.double(0),
        #MEMAIN_minjets = cms.int32(-1),
        #MEMAIN_qcut = cms.double(-1),
        #MEMAIN_excres = cms.string(''),
        #MEMAIN_etaclmax = cms.double(-1),
        #outTree_flag = cms.int32(0),
        #scheme = cms.string('Madgraph'),
        #MEMAIN_maxjets = cms.int32(-1),
        #mode = cms.string('auto')
    #),
#    SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
    PythiaParameters = cms.PSet(
            processParameters = cms.vstring(
				'Main:timesAllowErrors    = 10000', 
				'ParticleDecays:limitTau0 = on',
				'ParticleDecays:tau0Max = 10',
				'Tune:ee 3',
				'Tune:pp 5',
				'SpaceShower:pTmaxMatch = 1',
				'SpaceShower:pTmaxFudge = 1',
				'SpaceShower:MEcorrections = off',
				'TimeShower:pTmaxMatch = 1',
				'TimeShower:pTmaxFudge = 1',
				'TimeShower:MEcorrections = off',
				'TimeShower:globalRecoil = on',
				'TimeShower:limitPTmaxGlobal = on',
				'TimeShower:nMaxGlobalRecoil = 1',
				'TimeShower:globalRecoilMode = 2',
				'TimeShower:nMaxGlobalBranch = 1',
				'SLHA:keepSM = on',
				'SLHA:minMassSM = 1000.', #reset masses/widths/branching ratios for W/Z/top to match internal madgraph/madspin values        
				'Check:epTolErr = 0.01',
                '36:onMode = off',      # turn OFF all A decays
                '36:onIfMatch = 23 25', # turn ON A->Zh
                '23:onMode = off',      # turn OFF all A decays
                '23:onIfAny = 15 13 11',# turn ON Z->ll, l = t, m ,e
				'25:onMode = off',      # turn OFF all H decays
				'25:onIfAny = 15',      # turn ON H->tautau
                
                # RIC
                'Higgs:useBSM = on',
                'HiggsBSM:gg2A3 = on',
                'SLHA:allowUserOverride = on',


				),
	    parameterSets = cms.vstring('processParameters')
	    )
)




# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
#process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)

process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)


# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
