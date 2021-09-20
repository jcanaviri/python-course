import logging as log

log.basicConfig(level=log.DEBUG, 
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('data.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('This is a debug message')
    log.info('This is a info message')
    log.warning('This is a warning message')
    log.error('This is a error message')
    log.critical('This is a critical message')
