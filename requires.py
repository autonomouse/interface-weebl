from charms.reactive import RelationBase
from charms.reactive import hook


class WeeblClient(RelationBase):

    auto_accessors = ['weebl_api', 'weebl_url', 'weebl_username',
                      'weebl_apikey', 'environment_uuid']

    @hook('{requires:weebl}-relation-{joined,changed}')
    def joined_changed(self):
        # Notify that we have an incoming request for data
        self.set_state('{relation_name}.connected')
        if self.get_remote('weebl_url') or self.get_remote('weebl_url'):
            self.set_state('{relation_name}.available')

    @hook('{requires:weebl}-relation-{departed,broken}')
    def departed_broken(self):
        self.remove_state('{relation_name}.connected')
        self.remove_state('{relation_name}.available')
