py_health_checker
=================

Non blocking CLI tool to monitor uptime of a web server

Usage
'''''

::

    python -m py_health_checker -e="15 sec"
    
    
Arguments
'''''

::

  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Path to config file
  -e EVERY, --every EVERY
                        Run health checks every x time. Example: --every="10 min"


Instalation
'''''

Run from the project directory

::

    sudo python3 setup.py install

    
    
Config example
'''''

*config file can be provided with ``--config`` option*

.. code-block:: JSON

			{
				"channels": [
					{
						"type": "telegram",
						"bot_id": "382022228",
						"token": "AAHZnewtR3-_IYSDQRCWBVfaeceVKZ_22222",
						"chat_id": "328345576"
					}
				],
				"targets": [
					{
						"type": "http",
						"name": "DuckduckGo",
						"endpoint": "https://duckduckgo.com",
						"method": "GET",
						"checker": {
							"status_code": 200
						}
					}
				]
			}


Channels
'''''

**Currently only telegram is supported**. Support for other notification channels will be added in the near future

Targets
'''''

**HTTP only for now**. Support for other target types and checks will be added as well


Time units
'''''

Supported options are:

#. ``sec``
#. ``min`` *or* ``mins``
#. ``hour`` *or* ``hours``
#. ``day`` *or* ``days``
#. ``week`` *or* ``weeks``


*Valid Examples*:

#. ``py_health_checker --every="1 week"``
#. ``py_health_checker --every="7 sec"``
#. ``py_health_checker -e="17 min"``
#. ``py_health_checker -e="1 day"``
