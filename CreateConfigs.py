#!/usr/bin/python

# ------------------------------------------------------------------------------
# Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Marlin_Configurations
# version: 3.1
# date: 2022/02/14
# ------------------------------------------------------------------------------

import sys
import re
import os
import io
import json

verbose = True

SourceDir = 'Original Configs/'

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
    match = re.search(r''+self.searchfor+'(.*)', lines)
    if match :
      if verbose: print('>>>> found ',self.searchfor)
      return lines.replace(match[0], match[0]+'\n'+self.newline)
    else :
      print('>>>> Not found '+self.searchfor)
      quit()
      #return lines

  def Replace(self) :
    global lines
    lines, n = re.subn(self.searchfor, self.value, lines)
    if n :
      if verbose: print('>>>> found',n,self.searchfor)
    else:
      print('>>>> Not found '+self.searchfor)
      quit()
    return lines
  
  def Custom(self) :
    global lines
    self.mask = '('+self.mask+')'
    if self.comment : self.comment = '  // '+self.comment
    lines, n = re.subn(r'(\n *)(//)?( *)(?P<searchfor>#define +'+self.searchfor+r'\b *)'+self.mask+r'( *.*)', r'\1\3\g<searchfor>'+self.value+r'\6'+self.comment, lines)
    if n :
      if verbose: print('>>>> found',n,self.searchfor)
    else:
      print('>>>> Not found '+self.searchfor+' mask:'+self.mask)
      quit()
    return lines

  def CustomVal(self) :
    self.mask='[-,0-9,.]+'
    return self.Custom()

  def Enable(self) :
    self.mask = ''
    self.value = ''
    return self.Custom();

  def Disable(self) :
    global lines
    if self.comment : self.comment = '  // '+self.comment
    lines, n = re.subn(r'(\n *)(//)?( *)(?P<searchfor>#define +'+self.searchfor+r'\b *.*)', r'\1//\3\g<searchfor>'+self.comment, lines)
    if n :
      if verbose: print('>>>> found',n,self.searchfor)
    else:
      print('>>>> Not found '+self.searchfor)
      quit()
    return lines

  def Invalid(self) :
    print('>>>> Invalid operation:',self.op)
    quit()
    #return lines

def ProcessLines(jsonfile, config):
  global lines
  C = Customize()
  if os.path.isfile(jsonfile) :
    j = open(jsonfile, 'r')
    data = json.load(j)
    if not data.get(config) :
      print('>>>>',jsonfile,'section',config,'not in use')
      return lines
    for l in data[config] :
      C.op = l.get('op')
      C.searchfor = l.get('searchfor')
      C.newline = l.get('newline')
      C.mask = l.get('mask')
      C.value = l.get('value')
      C.comment = l.get('comment')
      if not C.comment : C.comment = ''
      lines = C.Do()
    j.close()
  return lines

def CustomizeFile(Machine_Name, SourceDir, TargetDir, Mode, config) :  
  global lines
  Source = SourceDir+config
  Target = TargetDir+config
    
  if os.path.isfile(Source) :
    print('-Process', Target)
    os.makedirs(TargetDir, exist_ok=True)
    f = open(Source, 'r', encoding="utf8")
    lines = f.read()

    lines = ProcessLines("Common.json", config)
    for val in Mode:
      JsonFile = val + '.json'
      if not os.path.isfile(JsonFile) :
        print('Json file:', JsonFile,'not found')
        quit()
      lines = ProcessLines(JsonFile, config)

    if Machine_Name :
      lines = lines.replace('//#define CUSTOM_MACHINE_NAME "3D Printer"','#define CUSTOM_MACHINE_NAME "'+Machine_Name+'"')
      lines = lines.replace('//#define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION','#define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION "based on bugfix-2.0.x"')
    else :
      lines = lines.replace('//#define CUSTOM_MACHINE_NAME "3D Printer"','#define CUSTOM_MACHINE_NAME "'+'Ender3v2 '+' '.join(Mode)+'"')
      lines = lines.replace('//#define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION','#define DETAILED_BUILD_VERSION SHORT_BUILD_VERSION " '+' '.join(Mode)+', based on bugfix-2.0.x"')
    with open(Target, "w", encoding="utf8") as of:
      of.write(lines)
      of.close()
    f.close();
    if verbose: print('-----')
  else :
    print('Source file:', Source,'not found')
    quit()

def Generate(Machine_Name, Mode) :
  print('Configurations generator script for the Professional Firmware')
  print('Author: Miguel A. Risco Castillo (c) 2022\n')

  if Machine_Name:
    TargetDir = Machine_Name+'/'
  else:
    TargetDir = '-'.join(Mode)+'/'
  CustomizeFile(Machine_Name, SourceDir, TargetDir, Mode, 'Configuration.h')
  CustomizeFile(Machine_Name, SourceDir, TargetDir, Mode, 'Configuration_adv.h')
  CustomizeFile(Machine_Name, SourceDir, TargetDir, Mode, 'Version.h')


