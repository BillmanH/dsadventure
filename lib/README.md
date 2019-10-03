# Charater attributes and defaults:


a weapon must have a `range`, `damage`, and an `id`. In order to be used in combat it must be listed in `charData['equipped_weapon']`. The ID is just a short random string. 
```
     c.equipment['weapons'] = [{'name':'basic bow',
                                   'id':'00000',
                                   'range':200,
                                   'damage':3,
                                   'damage_mod':1}]
```
