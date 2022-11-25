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
Hero = Player
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
</br>
</br>


#### show_effects
</br>
</br>



## Levels
## Items
## Effects
## Utils