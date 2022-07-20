test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ypoly(-1,1)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ypoly(1,1)
          9.0
          """,
          'hidden': False,
          'locked': False
        },
               {
          'code': r"""
          >>> ypoly(7,10)
          1412376249.0
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
