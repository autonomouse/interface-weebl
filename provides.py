from charms.reactive import RelationBase
from charms.reactive import hook


class WeeblProvider(RelationBase):

    @hook('{provides:weebl}-relation-{joined,changed}')
    def joined_changed(self):
        # Notify that we have an incoming request for data
        self.set_state('{relation_name}.connected')

    @hook('{provides:weebl}-relation-{departed,broken}')
    def departed_broken(self):
        self.remove_state('{relation_name}.connected')

    def provide_data(self, weebl_api=None, weebl_url=None, weebl_username=None,
                     weebl_apikey=None, environment_uuid=None):
        for conv in self.conversations():
            self.set_remote(scope=conv.scope, data={
                'weebl_api': weebl_api,
                'weebl_url': self.get_local('private-address'),  # or should this be 'public-address'?
                'weebl_username': weebl_username,
                'weebl_apikey': weebl_apikey,
                'environment_uuid': environment_uuid,
            })
