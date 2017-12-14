# lazy-log-filter
Python log filter implementation

In order to use these filters, you will likely use dictconfig or the
pip package logconfig and implement a configuration like this.

<pre>
{
	"version": 1,
	"disable_existing_loggers": false,
	"formatters": {
		"simple": {
			"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
		},
		"detailed": {
			"format": "[%(filename)s:%(lineno)s - %(funcName)5s()] %(asctime)s - %(name)s - %(levelname)s - %(message)s"
		}
	},
	"filters": {
		"debug_only": {
			"()": "log.filters.level.SingleLevelFilter",
			"passlevel": 10,
			"reject": false
		},
		"testing_only": {
			"()": "log.filters.patterns.string.StringLevelFilter",
			"pattern_accepted": "test",
			"passlevel": 10,
			"reject": false
		}
	},
	"handlers": {
		"console": {
			"class": "logging.StreamHandler",
			"level": "INFO",
			"formatter": "detailed",
			"stream": "ext://sys.stdout"
		},
		"testing_file_handler": {
			"class": "logging.handlers.RotatingFileHandler",
			"level": "DEBUG",
			"formatter": "simple",
			"filename": "euler-one-testing-debug.log",
			"filters": ["testing_only"],
			"maxBytes": 10000000,
			"backupCount": 5,
			"encoding": "utf8"
		},
		"debug_file_handler": {
			"class": "logging.handlers.RotatingFileHandler",
			"level": "DEBUG",
			"formatter": "simple",
			"filename": "euler-one-debug.log",
			"filters": ["debug_only"],
			"maxBytes": 10000000,
			"backupCount": 5,
			"encoding": "utf8"
		},
		"info_file_handler": {
			"class": "logging.handlers.RotatingFileHandler",
			"level": "INFO",
			"formatter": "simple",
			"filename": "euler-one-info.log",
			"maxBytes": 10000000,
			"backupCount": 5,
			"encoding": "utf8"
		},
		"error_file_handler": {
			"class": "logging.handlers.RotatingFileHandler",
			"level": "WARNING",
			"formatter": "simple",
			"filename": "euler-one-error.log",
			"maxBytes": 10000000,
			"backupCount": 5,
			"encoding": "utf8"
		}
	},
	"loggers": {
		"run": {
			"level": "DEBUG"
		}
	},
	"root": {
		"level": "DEBUG",
		"handlers": [
			"info_file_handler",
			"error_file_handler",
			"debug_file_handler",
			"testing_file_handler",
			"console"
		]
	}
}
</pre>