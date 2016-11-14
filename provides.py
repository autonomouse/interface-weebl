from charms.reactive import RelationBase
from charms.reactive import hook
from charms.reactive import scopes


class WeeblProvider(RelationBase):
    scope = scopes.GLOBAL

    @hook('{provides:weebl}-relation-{joined,changed}')
    def joined_changed(self):
        # Notify that we have an incoming request for data
        self.set_state('{relation_name}.connected')

    @hook('{provides:weebl}-relation-{departed,broken}')
    def departed_broken(self):
        self.remove_state('{relation_name}.connected')

    def provide_weebl_credentials(self, weebl_username, weebl_apikey):
        self.set_remote(scope=self.scope, data={
            'weebl_username': weebl_username,
            'weebl_apikey': weebl_apikey,
        })

    def weebl_url(self):
        return self.get_local('private-address')
