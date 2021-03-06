#!/usr/bin/python -u
SETTINGS=\
{'host': {'bootflags': {'default': 'default',
                        'name': 'boot_flags',
                        'type': 's'},
          'bootpolicy': {'default': 'ONETIME',
                         'name': 'boot_policy',
                         'type': 's'},
          'powercap': {'default': 0,
                       'max': 1000,
                       'min': 0,
                       'name': 'power_cap',
                       'type': 'i',
                       'unit': 'watts'},
          'powerpolicy': {'default': 'ALWAYS_POWER_ON',
                          'name': 'power_policy',
                          'type': 's'},
          'restrictedmode': {'default': False,
                             'name': 'restricted_mode',
                             'type': 'b'},
          'sysstate': {'default': '', 'name': 'system_state', 'type': 's'}}}
