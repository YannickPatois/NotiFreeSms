#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os, sys
import pickle
import argparse

import requests
import appdirs

# https://smsapi.free-mobile.fr/sendmsg?user=<>&pass=<>&msg=<>

class Contact:
  def __init__(self,name,cid,cpass):
    self._name=name
    self._id  =cid
    self._pass=cpass

  def __str__(self):
    return self._name.ljust(12)+" : "+self._id+" "+self._pass
  


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
      try:
        self._contacts=pickle.load(f)
      except EOFError:
        print ("Empty contact file")
        self._contacts={}
    else:
      self._contacts={}
     
  def __str__(self):
    s="Contacts:\n"
    s="NOM            ID       PASS"
    for k,c in self._contacts.items():
      s+="\n"+str(c)
    s+="\n"
    return s


  def add(self,c):
    if (self._contacts.has_key(c._name)):
      print ("Erreur: un contact avec le même nom ("+c._name+") existe déjà")
      print ("Utilisez --replacecontact et non --addcontact")
      return
    self._contacts[c._name]=c

  def write(self): 
    f=open(self._file_name,"w") # FIXME : all contacts lost if something goes wrong here
    pickle.dump(self._contacts,f)
    f.close()


# --------------------------------------------------------------------------
# Welcome to Derry, Maine
# --------------------------------------------------------------------------
def main():
  parser = argparse.ArgumentParser(description="""
    Permet d'utiliser l'option Notification SMS Free Mobile SMS depuis un PC
    """)
  parser.add_argument('--listcontacts', dest='listcontacts', action='store_true',
                      default=False,
                      help="Liste les contacts enregistrés")
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
  
  if (args.listcontacts):
    print ct
    sys.exit(0)

  if (args.addcontact):
    if ( (not args.name) or (not args.userid) or (not args.userpass) ):
      print ("Nom, ID et mot de passe sont nécessaires pour créer un compte!")
      sys.exit(1)
    print ("Ajout d'un contact")
    c=Contact(args.name    .decode('utf8'),
              args.userid  .decode('utf8'),
              args.userpass.decode('utf8'))
    print c
    ct.add(c)
    ct.write()
    print ct


if __name__ == '__main__':
  main()

