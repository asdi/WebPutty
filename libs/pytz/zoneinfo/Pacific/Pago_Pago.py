'''tzinfo timezone information for Pacific/Pago_Pago.'''
from pytz.tzinfo import DstTzInfo
from pytz.tzinfo import memorized_datetime as d
from pytz.tzinfo import memorized_ttinfo as i

class Pago_Pago(DstTzInfo):
    '''Pacific/Pago_Pago timezone definition. See datetime.tzinfo for details'''

    zone = 'Pacific/Pago_Pago'

    _utc_transition_times = [
d(1,1,1,0,0,0),
d(1911,1,1,11,22,48),
d(1950,1,1,11,30,0),
d(1967,4,1,11,0,0),
d(1983,11,30,11,0,0),
        ]

    _transition_info = [
i(-40980,0,'LMT'),
i(-41400,0,'SAMT'),
i(-39600,0,'NST'),
i(-39600,0,'BST'),
i(-39600,0,'SST'),
        ]

Pago_Pago = Pago_Pago()

