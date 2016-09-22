# Interface weebl

This is a Juju charm interface layer. This interface is used for
connecting to a weebl environment unit.

## States

`{relation_name}.connected` - The relationship has been established, but not enough data has been sent to determine if we are ready to use it.

`{relation_name}.available` - We have the required information, we can now configure our consumer service.

### Examples

#### requires
Most charms will want to implement this interface as a weebl connection.
When implementing this interface as a requirer:

`metadata.yaml`
```yaml
  requires:
    weebl:
      interface: weebl
```

`layer.yaml`
```yaml
includes:
- interface:weebl
```

`reactive/thing.py`
```python
  @when('weebl.available')
  def get_url(weebl):
      return weebl.weebl_url()

  @when('weebl.available')
  def get_username(weebl):
      return weebl.weebl_username()

  @when('weebl.available')
  def get_apikey(weebl):
      return weebl.weebl_apikey()
```

#### provides
The weebl charm provides this interface. If you wanted to provide this interface in another layer:

`metadata.yaml`
```yaml
  provides:
    weebl:
      interface: weebl
```

`layer.yaml`
```yaml
includes:
- interface:weebl
```

`reactive/code.py`
```python
  @when('weebl.connected')
  def send_weebl_info(weebl):
      weebl.provide_weebl_credentials(
          weebl_username=config['username'],
          weebl_apikey=config['apikey'])
```

### Data

Weebl send's the following information, per unit

 - weebl_url
 - weebl_username
 - weebl_apikey

### Maintainers

- Darren Hoyland &lt;darren.hoyland@canonical.com&gt;
