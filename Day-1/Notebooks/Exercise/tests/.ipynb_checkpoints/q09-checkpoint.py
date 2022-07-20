test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum(train.PredGender)
          314.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(test.PredGender)
          152.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(AccGender,2)
          78.68
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
