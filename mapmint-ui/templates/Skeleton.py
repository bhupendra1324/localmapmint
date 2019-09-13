#!/usr/bin/env python
# -*- coding: UTF-8 -*-




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Cheetah.compat import unicode
import zoo
import zoo
import mm_access

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '3.2.3'
__CHEETAH_versionTuple__ = (3, 2, 3, 'final', 0)
__CHEETAH_genTime__ = 1563016932.9066021
__CHEETAH_genTimestamp__ = 'Sat Jul 13 16:52:12 2019'
__CHEETAH_src__ = 'Skeleton.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Jul 11 12:29:27 2019'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class Skeleton(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(Skeleton, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write('''<!DOCTYPE html> 
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="description" content="''')
        _v = VFN(VFFSL(SL,"zoo",True),"_",False)("MapMint: Professional SDI manager") # '$zoo._("MapMint: Professional SDI manager")' on line 13, col 35
        if _v is not None: write(_filter(_v, rawExpr='$zoo._("MapMint: Professional SDI manager")')) # from line 13, col 35.
        write('''">
<meta name="keywords" content="MapMint, SDI, Geospatial, Web GIS, GIS, WPS, WMS, WFS, WCS, ZOO-Project, ZOO, ZOO WPS, MapServer, GDAL, OSGeo, FOSS4G, OGC, OWS">
<meta name="copyright" content="''')
        _v = VFFSL(SL,"conf",True)["provider"]["providerName"] # '$conf["provider"]["providerName"]' on line 15, col 33
        if _v is not None: write(_filter(_v, rawExpr='$conf["provider"]["providerName"]')) # from line 15, col 33.
        write('''">
<meta name="author" content="''')
        _v = VFFSL(SL,"conf",True)["provider"]["providerName"] # '$conf["provider"]["providerName"]' on line 16, col 30
        if _v is not None: write(_filter(_v, rawExpr='$conf["provider"]["providerName"]')) # from line 16, col 30.
        write('''">
<link rel="shortcut icon" href="''')
        _v = VFFSL(SL,"conf",True)["main"]["mmAddress"] # '$conf["main"]["mmAddress"]' on line 17, col 33
        if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["mmAddress"]')) # from line 17, col 33.
        write('''/favicon.ico" />
<link rel="alternate" type="application/rss+xml" title="MapMint RSS Feed" href="''')
        _v = VFFSL(SL,"conf",True)["main"]["applicationAddress"] # '$(conf["main"]["applicationAddress"])' on line 18, col 81
        if _v is not None: write(_filter(_v, rawExpr='$(conf["main"]["applicationAddress"])')) # from line 18, col 81.
        write('''public/rss" />
<title>''')
        _v = VFFSL(SL,"page_title",True) # '$page_title' on line 19, col 8
        if _v is not None: write(_filter(_v, rawExpr='$page_title')) # from line 19, col 8.
        write('''</title>
''')
        for f in VFFSL(SL,"ocss",True): # generated from line 20, col 1
            write('''<link type="text/css" rel="stylesheet" href="''')
            if VFFSL(SL,"f",True)[0:7]=='http://': # generated from line 21, col 46
                _v = VFFSL(SL,"f",True) # '$f' on line 21, col 69
                if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 21, col 69.
            else: # generated from line 21, col 71
                _v = VFFSL(SL,"conf",True)["main"]["mmAddress"] # '$conf["main"]["mmAddress"]' on line 21, col 77
                if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["mmAddress"]')) # from line 21, col 77.
                write('''/css/''')
                _v = VFFSL(SL,"f",True) # '$f' on line 21, col 108
                if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 21, col 108.
            write('''" />
''')
        write('''

''')
        for f in VFFSL(SL,"css",True): # generated from line 26, col 1
            write('''<link type="text/css" rel="stylesheet" ''')
            if ("senv" in VFN(VFFSL(SL,"conf",True),"keys",False)() and "loggedin" in VFN(VFFSL(SL,"conf",True)["senv"],"keys",False)() and VFFSL(SL,"conf",True)["senv"]["loggedin"]): # generated from line 27, col 40
                write('''media="screen" title="''')
                if "adminTheme" in VFN(VFFSL(SL,"conf",True)["mm"],"keys",False)(): # generated from line 27, col 160
                    _v = VFFSL(SL,"conf",True)["mm"]["adminTheme"] # '$conf["mm"]["adminTheme"]' on line 27, col 199
                    if _v is not None: write(_filter(_v, rawExpr='$conf["mm"]["adminTheme"]')) # from line 27, col 199.
                else: # generated from line 27, col 224
                    _v = VFFSL(SL,"f",True) # '$f' on line 27, col 230
                    if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 27, col 230.
                write('''"''')
            write(''' href="''')
            if VFFSL(SL,"f",True)[0:7]=='http://': # generated from line 27, col 256
                _v = VFFSL(SL,"f",True) # '$f' on line 27, col 279
                if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 27, col 279.
            else: # generated from line 27, col 281
                _v = VFFSL(SL,"conf",True)["main"]["mmAddress"] # '$conf["main"]["mmAddress"]' on line 27, col 287
                if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["mmAddress"]')) # from line 27, col 287.
                write('''/css/''')
                if "adminTheme" in VFN(VFFSL(SL,"conf",True)["mm"],"keys",False)(): # generated from line 27, col 318
                    _v = VFFSL(SL,"conf",True)["mm"]["adminTheme"] # '$conf["mm"]["adminTheme"]' on line 27, col 357
                    if _v is not None: write(_filter(_v, rawExpr='$conf["mm"]["adminTheme"]')) # from line 27, col 357.
                else: # generated from line 27, col 382
                    _v = VFFSL(SL,"f",True) # '$f' on line 27, col 388
                    if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 27, col 388.
            write('''" id="''')
            if "adminTheme" in VFN(VFFSL(SL,"conf",True)["mm"],"keys",False)(): # generated from line 27, col 412
                _v = VFFSL(SL,"conf",True)["mm"]["adminTheme"] # '$conf["mm"]["adminTheme"]' on line 27, col 451
                if _v is not None: write(_filter(_v, rawExpr='$conf["mm"]["adminTheme"]')) # from line 27, col 451.
            else: # generated from line 27, col 476
                _v = VFFSL(SL,"f",True) # '$f' on line 27, col 482
                if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 27, col 482.
            write('''" />
''')
        write('''<link type="text/css" rel="stylesheet" href="''')
        _v = VFFSL(SL,"conf",True)["main"]["mmAddress"] # '$conf["main"]["mmAddress"]' on line 29, col 46
        if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["mmAddress"]')) # from line 29, col 46.
        write('''/new-themes/themes/default/loader.css" /> 
<!--[if IE]>
        <link rel="stylesheet" type="text/css" href="''')
        _v = VFFSL(SL,"conf",True)["main"]["mmAddress"] # '$conf["main"]["mmAddress"]' on line 31, col 54
        if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["mmAddress"]')) # from line 31, col 54.
        write('''/css/all-ie-only.css" />
<![endif]-->

''')
        if "jsCache" in VFN(VFFSL(SL,"conf",True)["main"],"keys",False)() and VFFSL(SL,"conf",True)["main"]["jsCache"]=="prod": # generated from line 34, col 1
            if len(VFFSL(SL,"js",True))>0 and VFFSL(SL,"js",True)[len(VFFSL(SL,"js",True))-1]=="ckeditor.js": # generated from line 35, col 1
                finalJS = VFFSL(SL,"js",True)[len(VFFSL(SL,"js",True))-1]
            else: # generated from line 37, col 1
                finalJS = ""
            ljs = ['flexigrid.js']+VFFSL(SL,"js",True)+['MLayout.js']
            write('''<script type="text/javascript" src="''')
            _v = VFFSL(SL,"conf",True)["main"]["mmAddress"] # '$conf["main"]["mmAddress"]' on line 41, col 37
            if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["mmAddress"]')) # from line 41, col 37.
            write('''/js/''')
            for f in ["modernizr.custom","jquery-2.0.3.min","jquery-ui-1.10.3",'jquery.notifyBar','jquery.easyui.min','jquery.layout-latest']: # generated from line 41, col 67
                _v = VFFSL(SL,"f",True) # '${f}' on line 41, col 199
                if _v is not None: write(_filter(_v, rawExpr='${f}')) # from line 41, col 199.
                write('''.js,''')
            write('''"></script>

''')
            if len(VFFSL(SL,"ljs",True))>0: # generated from line 43, col 1
                write('''<script type="text/javascript" src="''')
                _v = VFFSL(SL,"conf",True)["main"]["mmAddress"] # '$conf["main"]["mmAddress"]' on line 44, col 37
                if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["mmAddress"]')) # from line 44, col 37.
                write('''/js/''')
                for f in VFFSL(SL,"ljs",True): # generated from line 44, col 67
                    if VFFSL(SL,"finalJS",True)!=VFFSL(SL,"f",True): # generated from line 44, col 83
                        _v = VFFSL(SL,"f",True) # '$f' on line 44, col 100
                        if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 44, col 100.
                        write(''',''')
                write('''"></script>
''')
                if VFFSL(SL,"finalJS",True)!="": # generated from line 45, col 1
                    write('''<script src="''')
                    _v = VFFSL(SL,"conf",True)["main"]["mmAddress"] # '$conf["main"]["mmAddress"]' on line 46, col 14
                    if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["mmAddress"]')) # from line 46, col 14.
                    write('''/js/''')
                    _v = VFFSL(SL,"finalJS",True) # '$finalJS' on line 46, col 44
                    if _v is not None: write(_filter(_v, rawExpr='$finalJS')) # from line 46, col 44.
                    write('''"></script>
''')
            write('''

''')
            for f in VFFSL(SL,"js1",True): # generated from line 51, col 1
                write('''<script type="text/javascript" src="''')
                _v = VFFSL(SL,"conf",True)['main']['serverAddress'] # "$conf['main']['serverAddress']" on line 52, col 37
                if _v is not None: write(_filter(_v, rawExpr="$conf['main']['serverAddress']")) # from line 52, col 37.
                write('''?request=Execute&service=WPS&version=1.0.0&Identifier=template.display&DataInputs=tmpl=''')
                _v = VFFSL(SL,"f",True) # '$f' on line 52, col 154
                if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 52, col 154.
                write(''';module=''')
                _v = VFFSL(SL,"mmodule",True) # '$mmodule' on line 52, col 164
                if _v is not None: write(_filter(_v, rawExpr='$mmodule')) # from line 52, col 164.
                write('''&RawDataOutput=Result@mimeType=text/plain"></script>
''')
            write('''

''')
            for f in VFFSL(SL,"js2",True): # generated from line 57, col 1
                write('''<script type="text/javascript" src="''')
                _v = VFFSL(SL,"f",True) # '$f' on line 58, col 37
                if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 58, col 37.
                write('''"></script>
''')
            write('''

''')
            if len(VFFSL(SL,"js3",True))>0: # generated from line 62, col 1
                for f in VFFSL(SL,"js3",True): # generated from line 63, col 1
                    write('''<script type="text/javascript" src="''')
                    _v = VFFSL(SL,"conf",True)["main"]["publicationUrl"] # '$conf["main"]["publicationUrl"]' on line 64, col 37
                    if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["publicationUrl"]')) # from line 64, col 37.
                    write('''/''')
                    _v = VFFSL(SL,"f",True) # '$f' on line 64, col 69
                    if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 64, col 69.
                    write('''"></script>
''')
            write('''
''')
        else: # generated from line 68, col 1
            for f in ["jquery-2.0.3.min","jquery-ui-1.10.3",'jquery.notifyBar','jquery.easyui.min','jquery.layout-latest']: # generated from line 69, col 1
                write('''<script type="text/javascript" src="''')
                _v = VFFSL(SL,"conf",True)["main"]["mmAddress"] # '$conf["main"]["mmAddress"]' on line 70, col 37
                if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["mmAddress"]')) # from line 70, col 37.
                write('''/js/''')
                _v = VFFSL(SL,"f",True) # '${f}' on line 70, col 67
                if _v is not None: write(_filter(_v, rawExpr='${f}')) # from line 70, col 67.
                write('''.js"></script>
''')
            write('''
''')
            ljs = ['flexigrid.js']+VFFSL(SL,"js",True)+['MLayout.js']
            for f in VFFSL(SL,"ljs",True): # generated from line 74, col 1
                write('''<script type="text/javascript" src="''')
                _v = VFFSL(SL,"conf",True)["main"]["mmAddress"] # '$conf["main"]["mmAddress"]' on line 75, col 37
                if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["mmAddress"]')) # from line 75, col 37.
                write('''/js/''')
                _v = VFFSL(SL,"f",True) # '$f' on line 75, col 67
                if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 75, col 67.
                write('''"></script>
''')
            write('''
''')
            for f in VFFSL(SL,"js1",True): # generated from line 78, col 1
                write('''<script type="text/javascript" src="''')
                _v = VFFSL(SL,"conf",True)['main']['serverAddress'] # "$conf['main']['serverAddress']" on line 79, col 37
                if _v is not None: write(_filter(_v, rawExpr="$conf['main']['serverAddress']")) # from line 79, col 37.
                write('''?request=Execute&service=WPS&version=1.0.0&Identifier=template.display&DataInputs=tmpl=''')
                _v = VFFSL(SL,"f",True) # '$f' on line 79, col 154
                if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 79, col 154.
                write(''';module=''')
                _v = VFFSL(SL,"mmodule",True) # '$mmodule' on line 79, col 164
                if _v is not None: write(_filter(_v, rawExpr='$mmodule')) # from line 79, col 164.
                write('''&RawDataOutput=Result@mimeType=text/plain"></script>
''')
            write('''

''')
            for f in VFFSL(SL,"js2",True): # generated from line 84, col 1
                write('''<script type="text/javascript" src="''')
                _v = VFFSL(SL,"f",True) # '$f' on line 85, col 37
                if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 85, col 37.
                write('''"></script>
''')
            write('''
''')
            for f in VFFSL(SL,"js3",True): # generated from line 88, col 1
                write('''<script type="text/javascript" src="''')
                _v = VFFSL(SL,"conf",True)["main"]["publicationUrl"] # '$conf["main"]["publicationUrl"]' on line 89, col 37
                if _v is not None: write(_filter(_v, rawExpr='$conf["main"]["publicationUrl"]')) # from line 89, col 37.
                write('''/''')
                _v = VFFSL(SL,"f",True) # '$f' on line 89, col 69
                if _v is not None: write(_filter(_v, rawExpr='$f')) # from line 89, col 69.
                write('''"></script>
''')
            write('''
''')
        write('''
</head>
<body>

''')
        try: # generated from line 97, col 1
            verr = VFFSL(SL,"errorMsg",True)
        except: # generated from line 99, col 1
            verr = None
        if VFFSL(SL,"mmodule",True)!="public": # generated from line 102, col 1
            write('''<div class="loader-container"> 
<div id="loader"> 
</div> 
</div> 

''')
            if ("senv" in VFN(VFFSL(SL,"conf",True),"keys",False)() and "loggedin" in VFN(VFFSL(SL,"conf",True)["senv"],"keys",False)() and "lastname" in VFN(VFFSL(SL,"conf",True)["senv"],"keys",False)() and VFFSL(SL,"conf",True)["senv"]["loggedin"]!="false") and not(VFFSL(SL,"verr",True)): # generated from line 108, col 1
                write('''<div class="ui-layout-north">

<h1 class="ttitle"><span class="logo"></span>Map<span class="mint">Mint</span></h1>

<ul id="nav">

''')
                if VFFSL(SL,"conf",True)["mm"]["indexes"]=="true": # generated from line 115, col 1
                    menu = ['Dashboard','Distiller','Territories','Indexes','Themes','Documents','Manager','Publisher']
                else: # generated from line 117, col 1
                    if VFFSL(SL,"conf",True)["mm"]["documents"]=="true": # generated from line 118, col 1
                        menu = ['Dashboard','Distiller','Manager','Themes','Documents','Publisher']
                    else: # generated from line 120, col 1
                        menu = ['Dashboard','Distiller','Manager','Themes','Publisher']
                write('''
''')
                for a in VFFSL(SL,"menu",True): # generated from line 125, col 1
                    write('''    <li class="current">
''')
                    if VFFSL(SL,"inputs",True)['tmpl']['value']==VFFSL(SL,"a",True): # generated from line 127, col 1
                        write('''      <a href="''')
                        _v = VFFSL(SL,"a",True) # '$a' on line 128, col 16
                        if _v is not None: write(_filter(_v, rawExpr='$a')) # from line 128, col 16.
                        write('''" id="''')
                        _v = VFFSL(SL,"a",True) # '${a}' on line 128, col 24
                        if _v is not None: write(_filter(_v, rawExpr='${a}')) # from line 128, col 24.
                        write('''_button" class="ui-state-active">
''')
                    else: # generated from line 129, col 1
                        write('''      <a href="''')
                        _v = VFFSL(SL,"a",True) # '$a' on line 130, col 16
                        if _v is not None: write(_filter(_v, rawExpr='$a')) # from line 130, col 16.
                        write('''" id="''')
                        _v = VFFSL(SL,"a",True) # '${a}' on line 130, col 24
                        if _v is not None: write(_filter(_v, rawExpr='${a}')) # from line 130, col 24.
                        write('''_button">
''')
                    write('''    ''')
                    _v = VFN(VFFSL(SL,"zoo",True),"_",False)(VFFSL(SL,"a",True)) # '$zoo._($a)' on line 132, col 5
                    if _v is not None: write(_filter(_v, rawExpr='$zoo._($a)')) # from line 132, col 5.
                    write('''</a>
    </li>
''')
                write('''
  </ul>

</div>

<div class="admin">
    <h2 class="ad">''')
                _v = VFFSL(SL,"conf",True)["senv"]["firstname"] # '$conf["senv"]["firstname"]' on line 141, col 20
                if _v is not None: write(_filter(_v, rawExpr='$conf["senv"]["firstname"]')) # from line 141, col 20.
                write(''' ''')
                _v = VFFSL(SL,"conf",True)["senv"]["lastname"] # '$conf["senv"]["lastname"]' on line 141, col 47
                if _v is not None: write(_filter(_v, rawExpr='$conf["senv"]["lastname"]')) # from line 141, col 47.
                write('''</h2>
<ul class="sets">
                <li class="sett"><a href="#" id="users_admin" title="" onclick="System.UserPreferences()">''')
                _v = VFN(VFFSL(SL,"zoo",True),"_",False)("Preferences") # '$zoo._("Preferences")' on line 143, col 107
                if _v is not None: write(_filter(_v, rawExpr='$zoo._("Preferences")')) # from line 143, col 107.
                write('''</a></li>
''')
                groups = mm_access.getGroup(VFFSL(SL,"conf",True))
                if VFN(VFFSL(SL,"groups",True),"count",False)("admin")>0: # generated from line 146, col 1
                    write('''                <li class="user"><a href="#" id="user_management" title="" onclick="System.UserManagement()">''')
                    _v = VFN(VFFSL(SL,"zoo",True),"_",False)("Users management") # '$zoo._("Users management")' on line 147, col 110
                    if _v is not None: write(_filter(_v, rawExpr='$zoo._("Users management")')) # from line 147, col 110.
                    write('''</a></li>
''')
                write('''                <li class="logt"><a href="#" id="logout" title="">''')
                _v = VFN(VFFSL(SL,"zoo",True),"_",False)("Log out") # '$zoo._("Log out")' on line 149, col 67
                if _v is not None: write(_filter(_v, rawExpr='$zoo._("Log out")')) # from line 149, col 67.
                write('''</a></li>
        </ul>
        
</div>

''')
        write('''
''')
        _v = VFFSL(SL,"body",True) # '$body' on line 157, col 1
        if _v is not None: write(_filter(_v, rawExpr='$body')) # from line 157, col 1.
        write('''

''')
        if VFFSL(SL,"mmodule",True)!="public" and ("senv" in VFN(VFFSL(SL,"conf",True),"keys",False)() and VFFSL(SL,"conf",True)["senv"]["loggedin"]!="false" and "firstname" in VFN(VFFSL(SL,"conf",True)["senv"],"keys",False)()) and not(VFFSL(SL,"verr",True)): # generated from line 159, col 1
            write('''<div class="ui-layout-south"> 
  <p class="credits">&copy; copyright <a href="''')
            _v = VFFSL(SL,"conf",True)["provider"]["providerSite"] # '$conf["provider"]["providerSite"]' on line 161, col 48
            if _v is not None: write(_filter(_v, rawExpr='$conf["provider"]["providerSite"]')) # from line 161, col 48.
            write('''">''')
            _v = VFFSL(SL,"conf",True)["provider"]["providerName"] # '$conf["provider"]["providerName"]' on line 161, col 83
            if _v is not None: write(_filter(_v, rawExpr='$conf["provider"]["providerName"]')) # from line 161, col 83.
            write('''</a></p>
<!--<div class="progress_box_call"></div>-->\t
<div id="progress_bar" class="ui-progress-bar ui-container">
<div class="ui-progress" style="width: 79%;">
  <span class="ui-label" style="display:none;"><b class="value">79%</b></span>
</div>
</div>
''')
        else: # generated from line 168, col 1
            if not("nofooter" in VFN(VFFSL(SL,"conf",True)["mm"],"keys",False)()) or (VFFSL(SL,"conf",True)["mm"]["nofooter"]!="true" and "nofooter" in VFN(VFFSL(SL,"conf",True)["mm"],"keys",False)()): # generated from line 169, col 1
                write('''<ul class="credits">
<li>&copy; copyright <a href="''')
                _v = VFFSL(SL,"conf",True)["provider"]["providerSite"] # '$conf["provider"]["providerSite"]' on line 171, col 31
                if _v is not None: write(_filter(_v, rawExpr='$conf["provider"]["providerSite"]')) # from line 171, col 31.
                write('''">''')
                _v = VFFSL(SL,"conf",True)["provider"]["providerName"] # '$conf["provider"]["providerName"]' on line 171, col 66
                if _v is not None: write(_filter(_v, rawExpr='$conf["provider"]["providerName"]')) # from line 171, col 66.
                write('''</a></li>|&#160;&#160;<li><a href="http://www.mapmint.com">''')
                _v = VFN(VFFSL(SL,"zoo",True),"_",False)("Terms of use") # '$zoo._("Terms of use")' on line 171, col 158
                if _v is not None: write(_filter(_v, rawExpr='$zoo._("Terms of use")')) # from line 171, col 158.
                write('''</a></li>
</ul>
''')
        write('''
</div>
</body>
</html>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    js1 = ["main_js"] 

    js3 = [] 

    mmodule = "Distiller"

    css = ["green"]

    js2 =[]

    js2 =[]

    _mainCheetahMethod_for_Skeleton = 'respond'

## END CLASS DEFINITION

if not hasattr(Skeleton, '_initCheetahAttributes'):
    templateAPIClass = getattr(Skeleton,
                               '_CHEETAH_templateClass',
                               Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(Skeleton)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit https://cheetahtemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=Skeleton()).run()


