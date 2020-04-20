class GuildEmbedTestResult():
    """ class with GuildEmbedTest expected result   """

    @property
    def init_method(self):
        """ return the result expected for test_init"""
        return {
            'author': {
                'name': 'Guild Embed Test',
                'icon_url': 'https://url.com/icon.png'},
            'color': 1447446,
            'type': 'rich'}

    @property
    def add_stat(self):
        """ return the result expected for test_add_stat"""
        return [{'inline': True, 'name': 'Members', 'value': '5'}]

    @property
    def add_title_stats(self):
        """ return the result expected for test_add_title_stats """
        return {
            'title': 'id: 6',
            'fields': [
                {'inline': True, 'name': 'Members', 'value': '6'},
                {'inline': True, 'name': 'Roles', 'value': '3'},
                {'inline': True, 'name': 'Emojis', 'value': '4'},
                {'inline': True, 'name': 'Channel Categories', 'value': '2'},
                {'inline': True, 'name': 'Channels', 'value': '7'},
                {'inline': True, 'name': 'Text Channels', 'value': '3'},
                {'inline': True, 'name': 'Voice Channels', 'value': '2'},
                {'inline': True, 'name': 'News Channels', 'value': '1'},
                {'inline': True, 'name': 'Store Channels', 'value': '1'}],
            'footer': {'text': 'Owner: Jean-Pierre'}}

    @property
    def add_title_objs(self):
        """ return the result expected for test_add_title_objs """
        return {
            'title': 'Members',
            'fields': [
                {'inline': True, 'name': 'ID', 'value': '1\n3\n0\n2\n4\n5'},
                {
                    'inline': True, 'name': 'Name',
                    'value': 'Al\nBilly\nJean-Pierre\nJoe\nJohn\nMike'}],
            'footer': {'text': 'Total: 6'}}

    @property
    def add_emojis(self):
        """ return the result expected for test_add_emojis """
        return [
            {
                'inline': True, 'name': '\u200b',
                'value': '<:bad:20> bad\n\n<:strong:21> strong'},
            {
                'inline': True, 'name': '\u200b',
                'value': '<:cool:18> cool\n\n<:good:19> good'}]


class GuildShellTestResult():
    """ class with GuildShellTest expected result   """

    @property
    def add_list(self):
        """ return the result expected for test_add_list """
        return {
            'guild': '\n'.join([
                '\n##########  Guild ##########',
                '- 6 - Full guild\n']),
            'owner': '\n'.join([
                '\n##########  Owner ##########',
                '- 0 - Jean-Pierre\n']),
            'objs': '\n'.join([
                '\n########## 6 Members ##########',
                '- 1 - Al',
                '- 3 - Billy',
                '- 0 - Jean-Pierre',
                '- 2 - Joe',
                '- 4 - John',
                '- 5 - Mike\n'])}

    @property
    def add_emojis(self):
        """ return the result expected for test_add_emojis """
        return '\n'.join([
            '- <:cool:18> cool - <:good:19> good - <:bad:20> bad ',
            '- <:strong:21> strong '])

    @property
    def add_type_chans(self):
        """ return the result expected for test_add_type_chans """
        return '\n'.join([
            '### 2 Voice Channels',
            '- 14 - snack',
            '- 15 - studio\n'])

    @property
    def add_cats_chans(self):
        """ return the result expected for test_add_cats_chans """
        return '\n'.join([
            "\n\n########## CHANNELS BY CATEGORIES ##########",
            '\n##### No channel category #####',
            '### 1 Text Channels',
            '- 11 - reception',
            '### 1 News Channels',
            '- 12 - info point',
            '\n##### 1st floor #####',
            '### 2 Voice Channels',
            '- 14 - snack',
            '- 15 - studio',
            '### 1 Store Channels',
            '- 13 - shop',
            '\n##### 2nd floor #####',
            '### 2 Text Channels',
            '- 17 - boss office',
            '- 16 - meeting room\n'])

    @property
    def add_infos(self):
        """ return the result expected for test_add_infos """
        result = ''
        # guild owner members
        for value in self.add_list.values():
            result += value
        # roles categories
        result += '\n'.join([
            '\n########## 3 Roles ##########',
            '- 6 - @everyone',
            '- 7 - admin',
            '- 8 - staff',
            '\n########## 2 Channel Categories ##########',
            '- 9 - 1st floor',
            '- 10 - 2nd floor\n'])
        # channels
        result += '\n'.join([
            '\n########## 7 Channels ##########',
            '- 17 - boss office',
            '- 12 - info point',
            '- 16 - meeting room',
            '- 11 - reception',
            '- 13 - shop',
            '- 14 - snack',
            '- 15 - studio\n'])
        # text voice news store CHANNELS
        result += '\n'.join([
            '\n########## 3 Text Channels ##########',
            '- 17 - boss office',
            '- 16 - meeting room',
            '- 11 - reception',
            '\n########## 2 Voice Channels ##########',
            '- 14 - snack',
            '- 15 - studio',
            '\n########## 1 News Channels ##########',
            '- 12 - info point',
            '\n########## 1 Store Channels ##########',
            '- 13 - shop\n'])
        # emojis channels by categories
        result += '\n'.join([
            '\n########## 4 Emojis ##########',
            self.add_emojis])
        result += self.add_cats_chans
        return result


class InfoGuildCommandsTestResult():
    """ class with InfoGuildCommandsTest expected result   """
    @property
    def init_method(self):
        """ return the result expected for test_init - [(name, help), ...] """
        return [
            ('guild', "Guild's stats -> #guild"),
            ('owner', 'The Owner-> #owner'),
            ('mems', 'All members -> #mems'),
            ('roles', 'All roles -> #roles'),
            ('cats', "All channel's categories -> #cats"),
            ('chans', 'All channels -> #chans'),
            ('tchans', 'All text channels -> #tchans'),
            ('vchans', 'All voice channels -> #vchans'),
            ('nchans', 'All news channels -> #nchans'),
            ('schans', 'All store channels -> #schans'),
            ('emos', 'All emojis -> #emos'),
            ('shell', 'Infos in shell -> #shell')]

    @property
    def guild(self):
        """ return the result expected for test_guild (embed dict)"""
        embed_dict = GuildEmbedTestResult().add_title_stats
        icon_url = 'https://cdn.discordapp.com/icons/6/icon.png.webp?size=1024'
        embed_dict['author'] = {'name': 'Full guild', 'icon_url': icon_url}
        embed_dict['color'] = 1447446
        embed_dict['type'] = 'rich'
        return embed_dict

    @property
    def make_objs_embed(self):
        """ return the result expected for test_make_objs_embed (embed dict)"""
        embed_dict = GuildEmbedTestResult().init_method
        embed_dict.update(GuildEmbedTestResult().add_title_objs)
        sort_embed_dict = {}
        sort_embed_dict['footer'] = embed_dict['footer']
        sort_embed_dict['author'] = embed_dict['author']
        sort_embed_dict['fields'] = embed_dict['fields']
        sort_embed_dict['color'] = embed_dict['color']
        sort_embed_dict['type'] = embed_dict['type']
        sort_embed_dict['title'] = embed_dict['title']
        return embed_dict
