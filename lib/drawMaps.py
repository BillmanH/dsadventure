import altair as alt

def meltMap(df,value='value'):
    mapdata = df.melt()
    mapdata.columns = ['y',value]
    mapdata['x'] = df.unstack().index.codes[1]
    mapdata['key'] = mapdata['x'].apply(str) + ":" + mapdata['y'].apply(str)
    mapdata.index = mapdata['key']
    return mapdata.drop(['key'], axis=1)

def meltLandTypes(df,landscape):
    mapdata = meltMap(df)
    mapdata['terrain'] = mapdata['value'].apply(lambda x: landTypes(x,landscape))
    return mapdata

def mergeMaps(world):
    pass

def drawTerrainHeight(df):
    mapdata = meltMap(df)
    world = alt.Chart(mapdata).mark_rect().encode(
        x='x:O',
        y='y:O',
        color=alt.Color('value:Q',scale=alt.Scale(scheme="greens"))
    )
    return world

def drawTerrain(df,cities=None):
    world = alt.Chart(df).mark_rect().encode(
        x='x:O',
        y='y:O',        
        color=alt.Color('terrain',
                       scale=alt.Scale(
                domain=['land','mountain', 'ocean','city'],
                range=['green','brown', 'blue','black'])
                       )
    )
    return world


def drawRainFall(df):
    mapdata = meltMap(df)
    world = alt.Chart(mapdata).mark_rect().encode(
        x='x:O',
        y='y:O',
        color=alt.Color('value:Q',scale=alt.Scale(scheme="blues"))
    )
    return world

def landTypes(x,landscape):
    if x<=landscape.water_level:
        return 'ocean'
    if x>=landscape.mountain_level:
        return 'mountain'
    else:
        return 'land'

def allLandTypes(world,landscape):
    mapdata = meltMap(world['elevation'])
    mapdata['terrain'] = mapdata['value'].apply(lambda x: landTypes(x,landscape))
    return mapdata
    
def drawTerrainTypes(df,landscape):
    mapdata = meltMap(df)
    mapdata['terrain'] = mapdata['value'].apply(lambda x: landTypes(x,landscape))
    world = alt.Chart(mapdata).mark_rect().encode(
        x='x:O',
        y='y:O',
        color=alt.Color('terrain',
                       scale=alt.Scale(
                domain=['land','mountain', 'ocean'],
                range=['green','brown', 'blue'])
                       )
    )
    return world


def unstackWorld(df,col):
    df['key'] = df.index
    df['x'] = df['key'].apply(lambda x: int(str(x).split(":")[0]))
    df['y'] = df['key'].apply(lambda x: int(str(x).split(":")[1]))
    d = df[['x','y',col]].reset_index(drop=True)
    d = d[[c for c in df.columns if c in ['x','y',col]]]
    return d.pivot(index='x',columns='y')

def drawCities(df):
    df['key'] = df.index
    df['x'] = df['key'].apply(lambda x: int(str(x).split(":")[0]))
    df['y'] = df['key'].apply(lambda x: int(str(x).split(":")[1]))
    world = alt.Chart(df).mark_rect().encode(
        x='x:O',
        y='y:O',
        color=alt.Color('feature',
                       scale=alt.Scale(
                domain=['land','mountain', 'ocean','city'],
                range=['green','brown', 'blue','black'])
                       )
    )
    return world

def drawboarders(df):
    df['key'] = df.index
    df['x'] = df['key'].apply(lambda x: int(str(x).split(":")[0]))
    df['y'] = df['key'].apply(lambda x: int(str(x).split(":")[1]))
    world = alt.Chart(df.dropna(subset=['nation'])).mark_rect().encode(
        x='x:O',
        y='y:O',
        color=alt.Color('nation', scale=alt.Scale(scheme='category20b'))
    )
    return world