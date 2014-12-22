===============================
Object System
===============================

.. image:: https://badge.fury.io/py/obj_sys.png
    :target: http://badge.fury.io/py/obj_sys
    
.. image:: https://travis-ci.org/weijia/obj_sys.png?branch=master
        :target: https://travis-ci.org/weijia/obj_sys

.. image:: https://pypip.in/d/obj_sys/badge.png
        :target: https://pypi.python.org/pypi/obj_sys


An object system.

* Free software: BSD license
* Documentation: http://obj_sys.readthedocs.org.

Features
--------

* Post URL:
    `https://tag4u.sinaapp.com/obj_sys/append_tags/?username={username}&password={password}&selected_url={url}&description={description}&tags={tags}`
    
* Query by tags:
    `http://tag4u.sinaapp.com/obj_sys/api/ufsobj/ufsobj/?format=json&username={username}&password={password}&tag=star`

* Query by URL:
    `http://tag4u.sinaapp.com/obj_sys/api/ufsobj/ufsobj/?format=json&username={username}&password={password}&ufs_url__contains=https://github.com/cmusphinx/pocketsphinx-android-demo`

* Query ufs object in tree:
    `http://tag4u.sinaapp.com/obj_sys/api/ufs_obj_in_tree/ufs_obj_in_tree/?format=json&username={username}&password={password}`
    
* Query ufs object in tree for certain parent:
    `http://tag4u.sinaapp.com/obj_sys/api/ufs_obj_in_tree/ufs_obj_in_tree/?format=json&parent_url=bar://EAN_13/6949566703847`
    `http://9.tag4u.sinaapp.com/obj_sys/api/ufs_obj_in_tree/ufs_obj_in_tree/?parent_url=bar://root&format=json`
     
* TODO
