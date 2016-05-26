#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle
import argparse

import requests
import appdirs

# https://smsapi.free-mobile.fr/sendmsg?user=<>&pass=<>&msg=<>

class Contacts:
  def __init__(self):
    _appname="NBotiFreeSms"
    _appauthor = "YP"
    _config_dir=user_config_dir(_appname,_appauthor)
    if (not os.direxists(_config_dir)):
      os.makedirs(_config_dir)
    self._file_name=os.path.join(_config_dir,"contacts.dat")
    if (os.path.isfile(self._file_name)):
      f=open(self._file_name)
        self._contacts=pickle.load(f)
    else:
      self._contacts={}
     
    
    


# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
  pass



if __name__ == '__main__':
  main()

