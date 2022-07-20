test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> flatten_lists([[2,13,44], [6,7]])
          [2, 6, 7, 13, 44]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> flatten_lists([[2,13,12], [6,7]])
          [2, 6, 7, 12, 13]
          """,
          'hidden': False,
          'locked': False
        },
               {
          'code': r"""
          >>> flatten_lists([[22,13,4], [67,7]])
          [4, 7, 13, 22, 67]
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