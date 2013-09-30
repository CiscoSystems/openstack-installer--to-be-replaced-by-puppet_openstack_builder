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

def import_environ_keys(metadata):
    for key,value in os.environ.items():
        if key[:8] == 'jenkins_':
            metadata[key[8:]] = value
    return metadata

def import_yaml(path):
    metadata = {}
    if os.path.exists(path+'/hiera_data/user.yaml'):
        with open(path+'/hiera_data/user.yaml', 'r') as f:
            y = yaml.load(f.read())
            if y:
                for key, value in y.items():
                    metadata[key] = value
    if os.path.exists(path+'/hiera_data/jenkins.yaml'):
        with open(path+'/hiera_data/jenkins.yaml', 'r') as f:
            y = yaml.load(f.read())
            if y:
                for key, value in y.items():
                    metadata[key] = value
    return metadata

def build_metadata(path):
    return import_environ_keys(import_yaml(path))
        
