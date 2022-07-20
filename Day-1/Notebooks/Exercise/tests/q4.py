test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> longest_word('Hallo people of the world!')
          'people'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> longest_word('Welcome to DSA 2020 Arusha Tanzania!')
          'Tanzania!'
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
