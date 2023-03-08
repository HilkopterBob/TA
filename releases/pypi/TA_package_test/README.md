# Documentation 

## Table of contents
- [Main Game](#main-game)
- [Entities](#entities)
- [Levels](#levels)
- [Items](#items)
- [Effects](#effects)
- [Utils](#utils)






## Main Game
dazu gibts noch nichts zu sagen tbh, soll aber cool werden i guess

## Entities
###### Import: Entities.py
Used to create entities like the player and npcs.
#### Methods:
- [set name](#set_name)
- [change health](#change_health)
- [add item](#add_item)
- [remove item by name](#remove_item_by_name)
- [remove item by index](#remove_item_by_index)
- [add effect](#add_effect)
- [show effects](#show_effects)
- [remove effect by name](#remove_effect_by_name)
- [remove effect by index](#remove_effect_by_index)
- ! all methods return False on failure
</br>
</br>

####  set_name
Starts promt to set the player.name by the player  
reads: self   
writes: self.name

##### usage:
```py
Hero = Entity()
Hero.set_name()
```    
</br>
</br>

#### change_health
Changes the Player.health by adding "value"  
reads: self
writes: self.health


##### usage:
```py
Hero = Entity()
Hero.change_health(-10)
```
</br>
</br>

#### add_item
Adds item to inventory by using the item class.

reads: self, iname, itype  
writes: self.inv  
##### usage:
```py
Hero = Entity()
Hero.add_item("item name","item type")
```
</br>
</br>


#### remove_item_by_name
Removes item from entity inventory by given name     
reads: self, iname  
writes: self.inv  
##### usage:
```py
Hero = Entity()
Hero.remove_item_by_name("Sword")
```
</br>
</br>


#### remove_item_by_index
Removes item from entity inventory by given index   
reads: self, iname  
writes: self.inv  
##### usage:
```py
Hero = Entity()
Hero.remove_item_by_index(0)    #removes first item from inventory
                                #if no index given → deletes last item from inventory
```
</br>
</br>


#### add_effect
Appends effect to corresponding list of effects.  
reads: self(obj), effect(obj)  
writes: entity(oby) → {geffects, beffects, eeffects} → obj.effects  
##### usage:  
```py
Hero = Entity()
poisoning = Effect()
Hero.add_effect(poisoning)
```

</br>
</br>


#### show_effects
Prints element.name of entity.effects[]  
reads: self(obj), names(bool → default True)  
writes: self(obj)  
##### usage:
```py
Hero = Entity()
poisoning = Effect()
Hero.add_effect(poisoning)
Hero.show_effects()         #shows name for every effect
Hero.show_effects(False)    #shows vars(effect) for every effect
```
</br>
</br>


#### remove_effect_by_name
Removes effect from entity by given name.  
reads: self(obj), ename(str)  
writes: self(obj)  
##### usage:
```py
Hero = Entity()
poisoning = Effect()
Hero.add_effect(poisoning)
Hero.remove_effect_by_name(poisoning.name)
```

#### remove_effect_by_index

##### usage:
</br>  
</br>  

#### change_stat

##### usage:
</br>  
</br>  

#### let_effects_take_effect

##### usage:
</br>  
</br>  


## Levels
## Items
## Effects
## Utils
