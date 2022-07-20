test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sum(train.PredGenderAge13)
          351.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(test.PredGenderAge13)
          168.0 
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> sum(train.PredGenderAge18)
          385.0
          """,
          'hidden': False,
          'locked': False
        },        
        {
          'code': r"""
          >>> sum(test.PredGenderAge18)
          182.0
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

