import os
import logging
import logconfig

__filename = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                          '../logging.json')
logconfig.from_json(__filename)
