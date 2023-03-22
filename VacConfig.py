import appdaemon.plugins.hass.hassapi as hass
import os
import sys
import yaml
import jinja2

import pydevd_pycharm


class VacConfig(hass.Hass):

    def initialize(self):
        jloader = jinja2.FileSystemLoader(searchpath=f'{self.app_dir}/vac_config')
        vacuum_tpl = jinja2.Environment(loader=jloader).get_template("vacuum.yml.j2")
        config = self.args.get('config',{})
        for key, val in config.items():
            val['zone'].append(1)  # 1 clean
        with open(f'{self.app_dir}/vac_config/hass_config/config.yml', 'w') as f:
            f.write(yaml.safe_dump(yaml.safe_load(vacuum_tpl.render(config=config)),
                                   default_flow_style=False))
