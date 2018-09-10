#!/bin/bash
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/oracle/12.1/client64/lib/
export QUERYFILTER="NAME='druid'"
python /home/gpadmin/pushpredicate.py
