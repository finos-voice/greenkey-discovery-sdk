''' This contains the entity definition for a cardinal directions '''
from cleaning_functions import capitalize

DIRECTION = {
  'label': 'DIRECTION',
  'values': ('north', 'south', 'east', 'west'),
}

ADDRESS_NUMBER_PATTERN = [[['DIRECTION']]]

ENTITY_DEFINITION = {
  'patterns': ADDRESS_NUMBER_PATTERN,
  'extraTokens': (DIRECTION,),
  'extraCleaning': {
    'DIRECTION': capitalize,
  }
}

if __name__ == '__main__':
  import sys
  sys.path.append('../')
  from discovery_utils import validate_entity_definition
  validate_entity_definition(ENTITY_DEFINITION)
