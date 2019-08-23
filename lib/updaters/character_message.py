def get_town(towns,name):
    t = [town for town in towns if town.name == name]
    if len(t) == 0:
        return None
    if len(t) == 1:
        return t[0]
    else:
        return t

def update_char_message(world):
    message = "this message"
    long_description = ""
    area = world.df_features.loc[world.Character.get_location_key()]
    if area.terrain =="town":
        long_description = str(get_town(world.towns,area.feature))
    message = f"{world.Character.name} is standing in {area.terrain}:{area.key}. {long_description}"
    return message
