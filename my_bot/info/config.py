class ConfGuildCommands():
    """ Configuration for guild commands """

    def __init__(self, name, help):
        """ Init configuration with name and message """
        self.name = name
        self.help = help


conf_shl = ConfGuildCommands('shell', 'Display infos in shell -> #shell')
conf_own = ConfGuildCommands('owner', "The Owner-> #owner")
conf_mem = ConfGuildCommands('mems', "All members -> #mems")
conf_rol = ConfGuildCommands('roles', "All roles -> #roles")
conf_cat = ConfGuildCommands('cats', "All channel's categories -> #cats")
conf_cha = ConfGuildCommands('chans', 'All channels -> #chans')
conf_tcha = ConfGuildCommands('tchans', 'All text channels -> #tchans')
conf_vcha = ConfGuildCommands('vchans', 'All voice channels -> #vchans')
conf_pcha = ConfGuildCommands('pchans', 'All private channels -> #pchans')
conf_gcha = ConfGuildCommands('gchans', 'All group channels -> #gchans')
conf_ncha = ConfGuildCommands('nchans', 'All news channels -> #nchans')
conf_scha = ConfGuildCommands('schans', 'All store channels -> #schans')
conf_emo = ConfGuildCommands('emos', 'All emojis -> #emos')




# Configurations of commands -> {key: {'name': name, 'help': help text}}
def conf_dict(title, obj_type):
    """ return a dict with the name of a command and his help text,
    for the response the embed's title and obj_type for empty list msg """
    return {'title': title, 'obj_type': obj_type}


confs_guild = {
    'shl': conf_dict('shell', 'Display infos in shell -> #shell'),
    'own': conf_dict(
        'Owner', 'owner'),
    'mem': conf_dict(
        'Members', 'member'),
    'rol': conf_dict(
        'Roles', 'role'),
    'cat': conf_dict(
        'Channel Categories', 'channel category'),
    'cha': conf_dict(
        'Channels', 'channel'),
    'tcha': conf_dict(
        'Text Channels', 'text channel'),
    'vcha': conf_dict(
        'Voice Channels', 'voice channel'),
    'pcha': conf_dict(
        'Private Channels', 'private channel'),
    'gcha': conf_dict(
        'Group Channels', 'group channel'),
    'ncha': conf_dict(
        'News Channels', 'news channel'),
    'scha': conf_dict(
        'Store Channels', 'store channel'),
    'emo': conf_dict(
        'Emojis', 'emoji'), }

# confs_components = {
#     'rolmem': conf_dict(
#         'role_mems',
#         'Members with a role-> #role_mems "role name or id"'),
#     'catcha': conf_dict(
#         'cat_chans',
#         'Channels with a category-> #cat_chans "cat name or id"'),
#     'chamem': conf_dict(
#         'chan_mems',
#         'Auth Members on chan-> #chan_mems "chan name or id"')}