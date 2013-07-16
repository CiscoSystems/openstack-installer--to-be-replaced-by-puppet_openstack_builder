#!/bin/bash
#
# specifies things that are specific to the
# vagrant multi-node deployment scenario
#

function destroy_allinone_vms() {
  # we need to kill any existing machines on the same
  # system that conflict with the ones we want to spin up
  for i in build-server  compute-server02 control-server ; do
    if VBoxManage list vms | grep $i; then
      VBoxManage controlvm    $i poweroff || true
      # this sleep statement is to fix an issue where
      # machines are still in a locked state after the
      # controlvm poweroff command should be completed
      sleep 1
      VBoxManage unregistervm $i --delete
    fi
  done
}

function deploy_allinone_vms() {
  # build a cache vm if one does not already exist
  if ! VBoxManage list vms | grep cache ; then
    vagrant up cache 2>&1 | tee -a cache.log.$datestamp
  fi

  vagrant up allinone 2>&1 | tee -a allinone.log.$datestamp
}
