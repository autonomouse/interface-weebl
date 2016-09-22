from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes


class WeeblClient(RelationBase):
    scope = scopes.GLOBAL
    auto_accessors = ['weebl_username', 'weebl_apikey']

    @hook('{requires:weebl}-relation-{joined,changed}')
    def joined_changed(self):
        # Notify that we have an incoming request for data
        self.set_state('{relation_name}.connected')
        if self.get_remote('weebl_apikey'):
            self.set_state('{relation_name}.available')

    @hook('{requires:weebl}-relation-{departed,broken}')
    def departed_broken(self):
        self.remove_state('{relation_name}.connected')
        self.remove_state('{relation_name}.available')

    def weebl_url(self):
        return self.get_remote('private-address')
