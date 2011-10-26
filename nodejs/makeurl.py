#!/usr/bin/env python
import sys
import yaml
info = yaml.load(sys.stdin)
ports = dict((p['name'],p) for p in info['ports'])
print 'http://{0}/?ws_server={1}&ws_port={2}'.format(
	ports['dashboard']['url'].split('tcp://')[1],
	*ports['ws']['url'].split('tcp://')[1].split(':')
	)
