#!/usr/bin/env python
"""
    stack-builder.metadata
    ~~~~~~~~~~~~~~~~~~~~~~

    This module will load in relevant environment variables
    and config from the scenario yaml in order to create a
    dictionary of metadata that will be used to build shell
    scripts, populate hiera data for puppet, and drive the
    creation of appropriate openstack resources for the
    specified scenario. Environment variables will
    override yaml data.
"""
import os
import yaml

def import_environ_keys(metadata, prefix):
    """
    Import any environment variables with the correct
    prefix into the metadata dictionary
    """
    for key,value in os.environ.items():
        if key[:8] == prefix:
            metadata[key[8:]] = value
    return metadata

def import_yaml(path, files):
    """
    """
    metadata = {}

    for filename in files:
        if os.path.exists(path+filename+'.yaml'):
            with open(path+filename+'.yaml', 'r') as f:
                y = yaml.load(f.read())
                if y:
                    for key, value in y.items():
                        metadata[key] = value
    return metadata

def build_metadata(path, scenario, config):
    """
    Create a metadata dictionary from yaml
    and environment variables
    """
    if config == "config":
        prefix = 'osi_config_'
        files = ['config']
        return import_environ_keys(import_yaml(path+'/'), prefix)
    if config == 'user':
        prefix = 'osi_user_'
        files = ['user', 'jenkins', 'user.common', 'user.'+scenario]
        return import_environ_keys(import_yaml(path+'/hiera_data/'), prefix)
    else:
        print "Invalid config type: choose from 'user' and 'config'"

