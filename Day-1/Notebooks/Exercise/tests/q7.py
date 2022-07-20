test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> get_nearest_farthest([1.5,0.5], [[1,2],[2,1],[2,3],[4,5],[6,7],[7,6],[6,8],[9,10]])
          ([2, 1], [9, 10])
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> get_nearest_farthest([1.5,0.5], [[1,2],[4,1],[2,3],[4,5],[6,7],[7,6],[6,8],[9,1]])
          ([1, 2], [6, 8])
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
