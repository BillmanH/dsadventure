# notebooks

All backend functions are developed in jupyter notebooks. The notebooks actually `import` the actual modules used in the production code. The only difference is that the notebooks provide a REPL runthrough of each function so that it can be examined and documented. 

## Stages of the world
* Geography - the creatoin of geological features and elevation.
* Cities and Nations - population, buildings and division into nation-states.
* Conflict - events and procedures that bring story to the world. 

### World Pickles
* worlds (and everything in them) are saved in `pickle` files (`p`)
actual user `world` objects are stored in `\pickles\` as `.pkl` rather than `p`

