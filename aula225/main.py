from log import LogFileMixin, LogPrintMixin
from eletronicos import Smartfone



galaxy_s = Smartfone('Galaxy S')
iphone = Smartfone('iPhone')

galaxy_s.ligar()
galaxy_s.desligar()