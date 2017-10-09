#!/bin/bash/env python
#encoding = utf-8
import os
import sys
import commands

# commands.getoutput('')
# commands.getstatusoutput('')

result = commands.getoutput('cd ../../sh; ./echodate.sh')
print result

result = commands.getstatusoutput('pwd')
print result[1]
print result[2]
