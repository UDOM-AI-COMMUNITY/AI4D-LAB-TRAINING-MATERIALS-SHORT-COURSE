test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> perfectly_divisible(20,2)
          [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> perfectly_divisible(10,2)
          [0, 2, 4, 6, 8, 10]
          """,
          'hidden': False,
          'locked': False
        },
               {
          'code': r"""
          >>> perfectly_divisible(30,2)
          [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

