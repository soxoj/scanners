
class Scanner(object):

    name = "scanner_base_object"
    vuln_type = "default_vuln_type"
    user_options = {}
    Vulnerability_body_fields_to_web_interface = []

    def __init__(self, opts, target, metadata):
        self.metadata = metadata
        self.opts = opts
        self.target = target

    @staticmetod
    def circuit(target):
        '''
        Логика работы сканера.
        Принимает на вход объекты типа Metadata.
        Результатом работы должны быть экземпляры класса CVE.
        '''
        return Vulnerability()

    def check_start_condition(self):
        '''
        Проверка параметров которм должен соответствовать Target для запуска сканера
        True, если сканер должен запуститься. В другом случае False.
        '''
        return True

    class ScannerError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
