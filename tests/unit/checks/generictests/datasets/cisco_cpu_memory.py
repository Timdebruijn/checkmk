# -*- encoding: utf-8
# yapf: disable
checkname = 'cisco_cpu_memory'

info = [
    [[u'11000', u'3343553', u'565879', u'284872']],
    [
        [u'1', u'Virtual Stack'],
        [u'25', u'Switch1 Container of Power Supply Bay'],
        [u'11000', u'Switch2 Supervisor 1 (virtual slot 11)']
    ]
]

discovery = {'': [(u'Switch2 Supervisor 1 (virtual slot 11)', {})]}

checks = {
    '': [
        (
            u'Switch2 Supervisor 1 (virtual slot 11)', {}, [
                (
                    0, 'Used (3.46 GB of 3.73 GB): 92.81%',
                    [('mem_used', 92.81207602536634, None, None, 0.0, 100.0)]
                )
            ]
        ),
        (
            u'Switch2 Supervisor 1 (virtual slot 11)', {
                'levels': (-2000, -1000)
            }, [
                (
                    2,
                    'Used (3.46 GB of 3.73 GB): 92.81% (warn/crit at 47.61%/73.81%)',
                    [
                        (
                            'mem_used', 92.81207602536634, 47.61387331970476,
                            73.80693665985238, 0.0, 100.0
                        )
                    ]
                )
            ]
        ),
        (
            u'Switch2 Supervisor 1 (virtual slot 11)', {
                'levels': (50.0, 90.0)
            }, [
                (
                    2,
                    'Used (3.46 GB of 3.73 GB): 92.81% (warn/crit at 50.0%/90.0%)',
                    [('mem_used', 92.81207602536634, 50.0, 90.0, 0.0, 100.0)]
                )
            ]
        ),
        (
            u'Switch2 Supervisor 1 (virtual slot 11)', {
                'levels': (-20.0, -10.0)
            }, [
                (
                    2,
                    'Used (3.46 GB of 3.73 GB): 92.81% (warn/crit at 80.0%/90.0%)',
                    [('mem_used', 92.81207602536634, 80.0, 90.0, 0.0, 100.0)]
                )
            ]
        )
    ]
}
