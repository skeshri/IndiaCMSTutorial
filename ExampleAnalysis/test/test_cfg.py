import FWCore.ParameterSet.Config as cms

process = cms.Process("DemoAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("IndiaCMSTutorial.ExampleAnalysis.ExampleAnalysis_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:myfile.root'
    )
)

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('demo.root')
                                   )

process.p = cms.Path(process.exampleminiAOD)