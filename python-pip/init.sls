# -*- coding: utf-8 -*-
# vim: set syntax=yaml ts=2 sw=2 sts=2 et :

##
# python-pip
# ==========
#
# Execute:
#   qubesctl state.sls python-pip vm
##

{%- from 'python-pip/map.yaml' import settings with context %}
{%- set pip_dependencies = [settings.python_pip] + [settings.python_dev] + [settings.python_virtualenv] + settings.build_essential %}

python-pip:
  pkg.installed:
    - names: {{ pip_dependencies }}

virtualenvwrapper:
  pip.installed:
    - require:
      - pkg: python-pip
