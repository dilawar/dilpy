import datetime
now = datetime.datetime.now().strftime('%Y%m%d%H%M')

__version__ = '0.7.%s' % now
