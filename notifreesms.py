#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle
import argparse

import requests
import appdirs

# https://smsapi.free-mobile.fr/sendmsg?user=<>&pass=<>&msg=<>

class Contact:
  def __init__(self,name,cid,cpass):
    self._name=name
    self._id=cid
    self._pass=cpass

  def __str__(self):
    return self._name+" "+self._id+" "+self._pass
  


class Contacts:
  def __init__(self):
    _appname="NotiFreeSms"
    _appauthor = "YP"
    _config_dir=appdirs.user_config_dir(_appname,_appauthor)
    if (not os.path.isdir(_config_dir)):
      os.makedirs(_config_dir)
    self._file_name=os.path.join(_config_dir,"contacts.dat")
    if (os.path.isfile(self._file_name)):
      f=open(self._file_name)
      self._contacts=pickle.load(f)
    else:
      self._contacts={}
     
  def __str__(self):
    s="Contacts: "
    for c in self._contacts:
      s+="\n"+str(c)
    s+="\n"
    return s


def add(c):
    if (self._contacts.has_key(c._name)):
      print ("Erreur: un contact avec le même nom ("+c._name+") existe déjà")
      print ("Utilisez --replacecontact et non --addcontact")
      return
    self._contacts[c._name]=c
 
  
    


# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
  parser = argparse.ArgumentParser(description="""
    Permet d'utiliser l'option Notification SMS Free Mobile SMS depuis un PC
    """)
  parser.add_argument('--addcontact', dest='addcontact', action='store_true',
                      default=False,
                      help="Nouveau contact")
  parser.add_argument('--name', dest='name', action='store',
                      default=None,
                      help="Nom du contact")
  parser.add_argument('--userid', dest='userid', action='store',
                      default=None,
                      help="Identifiant Free du contact")
  parser.add_argument('--userpass', dest='userpass', action='store',
                      default=None,
                      help="Mot de passe Free du contact")
  
  args = parser.parse_args()
  
  ct=Contacts()
  
  if (args.addcontact):
    print ("Ajout d'un contact")
    c=Contact(args.name,args.userid,args.userpass)
    print c
    ct.add(c)
    print ct
    ct.write()


if __name__ == '__main__':
  main()

