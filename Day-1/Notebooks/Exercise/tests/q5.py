test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> dictionalize([1,1,1,1,2,2,2,2,3,3,4,5,5])
          {1: 4, 2: 4, 3: 2, 4: 1, 5: 2}
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dictionalize([1,1,1,6,8,2,9,3,3,3,4,5,5])
          {1: 3, 6: 1, 8: 1, 2: 1, 9: 1, 3: 3, 4: 1, 5: 2}
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
