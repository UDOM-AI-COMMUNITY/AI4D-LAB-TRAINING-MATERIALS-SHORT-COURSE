test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> generate_accuracy(example_data.predicted, example_data.actual)
          50.0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> round(generate_accuracy(df.loc[0:2,'predicted'], df.loc[0:2,'actual']),2)
          33.3
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
