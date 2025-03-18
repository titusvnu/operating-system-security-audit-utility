from tempfile import TemporaryFile

logging_file = TemporaryFile(prefix='!', mode='w', delete=False, suffix='.log', newline='',)

