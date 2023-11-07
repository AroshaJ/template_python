


class global_paramenters(object):
    

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(global_paramenters, cls).__new__(cls)
            print('initialising global parameters class')
        return cls.instance
