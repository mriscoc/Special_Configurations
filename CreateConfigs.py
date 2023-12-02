#!/usr/bin/env python3

# ------------------------------------------------------------------------------
# Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# version: 6.2
# date: 2022/11/05
# ------------------------------------------------------------------------------

import re
import os
import json

os.system('color')

verbose = False
error = False
loglines = ""

SourceDir = 'Original Configs/'

REDTEXT = '\033[41m'
GREENTEXT = '\033[32m'
NORMTEXT = '\033[0m'

def log(*text):
  global loglines
  txt = ' '.join(text)
  loglines += txt + "\n"
  print(txt + NORMTEXT)

class Customize:
  op = ''
  searchfor = ''
  newline = ''
  mask = ''
  value = ''
  comment = ''

  def Do(self):
    return getattr(self, self.op, self.Invalid)()
  
  def InsertAfter(self):
    global error
    match = re.search(r''+self.searchfor+'(.*)', lines)
    if match :
      if verbose: log('>>>> found ',self.searchfor)
      return lines.replace(match[0], match[0]+'\n'+self.newline)
    else :
      log('>>>> Not found '+self.searchfor)
      error = True
      return lines

  def Replace(self) :
    global lines
    global error
    lines, n = re.subn(self.searchfor, self.value, lines)
    if n :
      if verbose: log('>>>> found',n,self.searchfor)
    else:
      log('>>>> Not found '+self.searchfor)
      error = True
    return lines
  
  def Custom(self) :
    global lines
    global error
    self.mask = '('+self.mask+')'
    if self.comment : self.comment = '  // '+self.comment
    lines, n = re.subn(r'(\n *)(//)?( *)(?P<searchfor>#define +'+self.searchfor+r'\b *)'+self.mask+r'( *.*)', r'\1\3\g<searchfor>'+self.value+r'\6'+self.comment, lines)
    if n :
      if verbose: log('>>>> found',n,self.searchfor)
    else:
      log('>>>> Not found '+self.searchfor+' mask:'+self.mask)
      error = True
    return lines

  def CustomVal(self) :
    self.mask='[-,0-9,.,a-z,A-Z,_]+'
    return self.Custom()

  def Enable(self) :
    self.mask = ''
    self.value = ''
    return self.Custom();

  def Disable(self) :
    global lines
    global error
    if self.comment : self.comment = '  // '+self.comment
    lines, n = re.subn(r'(\n *)(//)?( *)(?P<searchfor>#define +'+self.searchfor+r'\b *.*)', r'\1//\3\g<searchfor>'+self.comment, lines)
    if n :
      if verbose: log('>>>> found',n,self.searchfor)
    else:
      log('>>>> Not found '+self.searchfor)
      error = True
    return lines

  def Invalid(self) :
    global error
    log('>>>> Invalid operation:',self.op)
    error = True
    return lines

def ProcessLines(jsonfile, config):
  global lines
  global error
  C = Customize()
  try:
    j = open(jsonfile, 'r')
    data = json.load(j)
    if not data.get(config) :
      if verbose: log('>>>>',jsonfile,'section',config,'not in use')
      return lines
    for l in data[config] :
      C.op = l.get('op')
      if not C.op : continue
      C.searchfor = l.get('searchfor')
      C.newline = l.get('newline')
      C.mask = l.get('mask')
      C.value = l.get('value')
      C.comment = l.get('comment')
      if not C.comment : C.comment = ''
      lines = C.Do()
      if error : break
  except Exception as e:
    log(str(e))
    error = True
  j.close()
  if error: log(">>>> While processing file:",jsonfile)
  return lines

def CustomizeFile(Machine_Name, SourceDir, TargetDir, Mode, config) :  
  global lines
  global error
  Source = SourceDir+config
  Target = TargetDir+config
    
  if os.path.isfile(Source) :

    log('-Process', Target)
    os.makedirs(TargetDir, exist_ok=True)
    f = open(Source, 'r', encoding="utf8")
    lines = f.read()

    if verbose: log(">>>> using: _printers/Common.json")
    lines = ProcessLines("_printers/Common.json", config)

    PathConfig = ['_printers/','_boards/','_displays/','_leveling/','_thermistor/','_features/']
    for val in Mode:
      for path in PathConfig:
        JsonFile = path + val + '.json'
        if os.path.isfile(JsonFile) :
          if verbose: log(">>>> using:", JsonFile)
          lines = ProcessLines(JsonFile, config)
          break
      if not os.path.isfile(JsonFile):
        log(">>>>",val+".json","was not found")
        error = True
      if error: break

    if not error:
      if Machine_Name :
        lines = lines.replace('//#define CUSTOM_MACHINE_NAME "3D Printer"','#define CUSTOM_MACHINE_NAME "'+Machine_Name+'"')
        lines = lines.replace('//#define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION','#if ENABLED(IS_DEMO)\n  #define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION " DEMO, NOT FOR PRODUCTION"\n#else\n  #define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION " '+Machine_Name+', based on bugfix-2.1.x"\n#endif')
      else :
        lines = lines.replace('//#define CUSTOM_MACHINE_NAME "3D Printer"','#define CUSTOM_MACHINE_NAME "'+' '.join(Mode)+'"')
        lines = lines.replace('//#define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION','#if ENABLED(IS_DEMO)\n  #define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION " DEMO, NOT FOR PRODUCTION"\n#else\n  #define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION " '+' '.join(Mode)+', based on bugfix-2.1.x"\n#endif')

    with open(Target, "w", encoding="utf8") as of:
      of.write(lines)
      of.close()
    f.close()
    if verbose: log('-----')

  else :
    log('Source file:', Source,'not found')
    error = True



def Generate(Machine_Name, Mode) :
  global error
  error = False
  global loglines
  loglines = ""
  print()

  log('Configurations generator script for the Professional Firmware')
  log('Author: Miguel A. Risco Castillo (c) 2022\n')

  if Machine_Name:
    TargetDir = Machine_Name+'/'
  else:
    TargetDir = '-'.join(Mode)+'/'
  
  SourceList = ['Configuration.h','Configuration_adv.h','Version.h','platformio.ini']
  for SourceFile in SourceList:
    CustomizeFile(Machine_Name, SourceDir, TargetDir, Mode, SourceFile)
    if error: break

  if error:
    print(REDTEXT, end="")
    log("\nAn error was found while processing your request")
  else:
    print(GREENTEXT, end="")
    log("\nConfiguration files correctly generated")

  with open(TargetDir+"/log.txt", "w", encoding="utf8") as logf:
    logf.write(loglines)
    logf.close()

  return error
